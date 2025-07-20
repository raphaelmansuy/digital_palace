# Deploy AWS Stack with CDK

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

## Objective


# TIL: Deploying an AWS Stack with CDK (2025-01-14)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Deploy AWS infrastructure with code** – Use AWS CDK and YAML/TypeScript to automate cloud stack creation, configuration, and management.

---

## The Pain Point

Manual AWS resource setup is error-prone and slow. CDK lets you define infrastructure as code, making deployments repeatable and version-controlled.

---

## Summary

AWS CDK enables you to define and deploy cloud infrastructure using code (TypeScript, Python, etc.), making your deployments reproducible, maintainable, and version-controlled. This guide shows how to use YAML for configuration and TypeScript for stack logic, with practical troubleshooting and security tips.

---

## Step-by-Step Guide

### 1. YAML-Based Configuration

Define your AWS resources in a YAML file:
```yaml
account:
  id: "XXXXX"
  region: "us-west-1"
  name: "magicstack"

vpc:
  name: "magicstack"
  id: "vpc-XXX"
  cidr_block: "172.31.0.0/16"
  max_azs: 2
  nat_gateways: 0
  public_subnet_cidr_mask: 24
  private_subnet_cidr_mask: 24
  enable_dns_hostnames: true
  enable_dns_support: true
  subnet_configuration:
    - name: "public"
      type: "PUBLIC"
      cidr_mask: 24
    - name: "private"
      type: "PRIVATE_WITH_EGRESS"
      cidr_mask: 24

  services:
    - webserver:
        name: "magicstack-webserver"
        count: 1
        type: "t4g.nano"
        tags:
          Name: "magicstack"
          Project: "magicstack"
          Environment: "dev"
          Owner: "magicstack"
          CostCenter: "magicstack"
        volume:
          size: 30gb
        ssh:
          authorized_public_keys: 
            - "~/.ssh/id_rsa.pub"
        security_groups:
          - "magicstack"
        public_ip: true
        authorized_public_ports:
          - 443
          - 22
```

### 2. CDK TypeScript Stack

Use TypeScript to read the YAML config and deploy resources:
```typescript
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as yaml from 'yaml';
import { EC2Client, ImportKeyPairCommand } from '@aws-sdk/client-ec2';
import * as os from 'os';
import * as fs from 'fs';

const config = yaml.parse(fs.readFileSync('./stack.yaml', 'utf8'));

export class AwsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, {
      ...props,
      env: {
        account: config.account.id,
        region: config.account.region
      }
    });

    // Configure AWS SDK region
    const ec2Client = new EC2Client({ region: config.account.region });

    this.initializeStack().catch(error => {
      console.error('Stack initialization failed:', error);
      throw error;
    });
  }

  private async initializeStack() {
    // Validate region configuration
    if (!config.account?.region) {
      console.error('❌ Region Configuration Error: No region specified in stack.yaml');
      throw new Error('Region must be specified in stack.yaml');
    }
    console.log(`✅ Region Configuration: ${config.account.region}`);

    if (this.node.tryGetContext('region') && this.node.tryGetContext('region') !== config.account.region) {
      console.error(`❌ Region Mismatch: 
        stack.yaml specifies ${config.account.region}, 
        but CDK context specifies ${this.node.tryGetContext('region')}`);
      throw new Error(`Region mismatch: stack.yaml specifies ${config.account.region} but CDK context specifies ${this.node.tryGetContext('region')}`);
    }

    // Try to look up the VPC, and create it if not found
    let vpc: ec2.Vpc;
    try {
      console.log(`🔍 Attempting to look up existing VPC: ${config.vpc.name}`);
      
      // First, try to find by VPC ID 
      vpc = ec2.Vpc.fromLookup(this, 'VPC', {
        vpcId: config.vpc.id
      }) as ec2.Vpc;
      
      console.log(`✅ Existing VPC found by ID: ${config.vpc.id}`);
    } catch (error) {
      console.warn(`⚠️ VPC not found. Creating new VPC: ${config.vpc.name}`);
      console.error('VPC Lookup Error:', error);
      
      // Log subnet configurations
      const rawSubnetConfigs = config.vpc.subnet_configuration || [];
      console.log(`📝 Raw Subnet Configurations: ${JSON.stringify(rawSubnetConfigs, null, 2)}`);

      const subnetConfigurations: ec2.SubnetConfiguration[] = rawSubnetConfigs.map((subnet: { 
        cidr_mask?: number, 
        name: string, 
        type: string 
      }) => {
        const subnetConfig = {
          cidrMask: subnet.cidr_mask || 24,
          name: subnet.name,
          subnetType: subnet.type === 'PUBLIC' 
            ? ec2.SubnetType.PUBLIC 
            : subnet.type === 'PRIVATE_WITH_EGRESS'
              ? ec2.SubnetType.PRIVATE_WITH_EGRESS
              : subnet.type === 'PRIVATE_ISOLATED'
                ? ec2.SubnetType.PRIVATE_ISOLATED
                : ec2.SubnetType.PRIVATE_WITH_EGRESS, // Default to PRIVATE_WITH_EGRESS
        };
        
        console.log(`🌐 Processed Subnet Configuration: 
          Name: ${subnetConfig.name}
          CIDR Mask: ${subnetConfig.cidrMask}
          Type: ${subnetConfig.subnetType}`);
        
        return subnetConfig;
      });

      // Log VPC creation parameters
      const vpcCreationParams = {
        vpcName: config.vpc.name,
        cidrBlock: config.vpc.cidr_block || 'Auto-assigned',
        maxAzs: config.vpc.max_azs || 2,
        natGateways: config.vpc.nat_gateways || 1,
        dnsHostnames: config.vpc.enable_dns_hostnames ?? true,
        dnsSupport: config.vpc.enable_dns_support ?? true,
      };
      
      console.log(`🏗️ VPC Creation Parameters: ${JSON.stringify(vpcCreationParams, null, 2)}`);

      vpc = new ec2.Vpc(this, 'MagicStackVPC', {
        vpcName: config.vpc.name,
        ipAddresses: config.vpc.cidr_block 
          ? ec2.IpAddresses.cidr(config.vpc.cidr_block) 
          : undefined,
        maxAzs: config.vpc.max_azs || 2,
        natGateways: config.vpc.nat_gateways || 1,
        enableDnsHostnames: config.vpc.enable_dns_hostnames ?? true,
        enableDnsSupport: config.vpc.enable_dns_support ?? true,
        subnetConfiguration: subnetConfigurations.length > 0 
          ? subnetConfigurations 
          : [
              {
                cidrMask: config.vpc.public_subnet_cidr_mask || 24,
                name: 'public',
                subnetType: ec2.SubnetType.PUBLIC,
              },
              {
                cidrMask: config.vpc.private_subnet_cidr_mask || 24,
                name: 'private',
                subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
              }
            ],
      });

      if (config.vpc.cidr_block) {
        cdk.Tags.of(vpc).add('aws-cdk:cidr', config.vpc.cidr_block);
      }

      console.log(`✅ New VPC Created: ${config.vpc.name}`);
    }

    const securityGroup = new ec2.SecurityGroup(this, 'WebServerSecurityGroup', {
      vpc,
      securityGroupName: config.vpc.services[0].webserver.security_groups[0],
    });

    // Dynamically add ingress rules from YAML configuration
    const authorizedPorts = config.vpc.services[0].webserver.authorized_public_ports || [];
    authorizedPorts.forEach((port: number) => {
      securityGroup.addIngressRule(
        ec2.Peer.anyIpv4(), 
        ec2.Port.tcp(port), 
        `Allow access to port ${port}`
      );
    });

    const role = new iam.Role(this, 'WebServerRole', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'),
    });

    // Optional key pair handling
    let keyName: string | undefined = undefined;
    let publicKeyContent: string | undefined = undefined;
    try {
      // Handle tilde expansion for the public key path
      const publicKeyPath = config.vpc.services[0].webserver.ssh.authorized_public_keys[0].replace('~', os.homedir());
      keyName = publicKeyPath.split('/').pop()?.replace('.pub', '');

      // Read the public key content
      publicKeyContent = fs.readFileSync(publicKeyPath, 'utf8').trim();

      // Optional: Import key pair to AWS if it doesn't exist
      const ec2Client = new EC2Client({ region: config.account.region });
      try {
        await ec2Client.send(new ImportKeyPairCommand({
          KeyName: keyName,
          PublicKeyMaterial: Buffer.from(publicKeyContent)
        }));
        console.log(`✅ Key pair ${keyName} imported successfully`);
      } catch (importError: any) {
        if (importError.name === 'InvalidKeyPair.Duplicate') {
          console.log(`ℹ️ Key pair ${keyName} already exists`);
        } else {
          console.warn(`⚠️ Key pair import failed: ${importError.message}`);
          keyName = undefined;
        }
      }
    } catch (error) {
      console.warn('⚠️ No SSH key configured or key import failed. Proceeding without key pair.');
    }

    const instance = new ec2.Instance(this, 'WebServerInstance', {
      instanceType: new ec2.InstanceType(config.vpc.services[0].type),
      machineImage: ec2.MachineImage.latestAmazonLinux2023(),
      vpc,
      securityGroup,
      role,
      keyName,
      vpcSubnets: {
        subnetType: ec2.SubnetType.PUBLIC,
      },
    });

    // Add user data to add the public key to authorized_keys
    if (keyName) {
      instance.addUserData(
        'mkdir -p /home/ec2-user/.ssh',
        'chmod 700 /home/ec2-user/.ssh',
        `echo "${publicKeyContent}" >> /home/ec2-user/.ssh/authorized_keys`,
        'chmod 600 /home/ec2-user/.ssh/authorized_keys',
        'chown -R ec2-user:ec2-user /home/ec2-user/.ssh'
      );
    }

    instance.instance.addPropertyOverride('Tags', config.vpc.services[0].tags);

    // Capture and output public IP
    const publicIp = instance.instancePublicIp;
    const ipData = {
      instanceId: instance.instanceId,
      publicIp: publicIp,
      timestamp: new Date().toISOString()
    };
    
    // Write to JSON file
    fs.writeFileSync('./instance-ips.json', JSON.stringify(ipData, null, 2));
    
    // Output to console
    new cdk.CfnOutput(this, 'InstancePublicIp', {
      value: publicIp,
      description: 'Public IP of the created EC2 instance'
    });
  }
}
```

### 3. Project Config

Example `package.json` for CDK project:
```json
{
  "name": "aws",
  "version": "0.1.0",
  "bin": {
    "aws": "bin/aws.js"
  },
  "scripts": {
    "build": "tsc",
    "watch": "tsc -w",
    "test": "jest",
    "cdk": "cdk"
  },
  "devDependencies": {
    "@aws-sdk/client-ec2": "^3.726.1",
    "@types/aws-sdk": "^0.0.42",
    "@types/jest": "^29.5.14",
    "@types/node": "22.7.9",
    "@types/yaml": "^1.9.6",
    "aws-cdk": "2.175.1",
    "jest": "^29.7.0",
    "ts-jest": "^29.2.5",
    "ts-node": "^10.9.2",
    "typescript": "~5.6.3"
  },
  "dependencies": {
    "aws-cdk-lib": "2.175.1",
    "constructs": "^10.0.0"
  }
}
```

---

## Troubleshooting

- If VPC lookup fails, check your YAML for correct VPC ID and region.
- For SSH key issues, ensure the public key path is valid and accessible.
- Use CDK context and tags to debug resource creation and configuration.
- See [AWS CDK documentation](https://docs.aws.amazon.com/cdk/) for advanced usage.

---

## Security Considerations

1. **Use IAM roles** for least-privilege access to resources.
2. **Store secrets securely** (never hardcode in code or YAML).
3. **Restrict security group rules** to only necessary ports and IPs.
4. **Audit resource tags** for cost and compliance tracking.
5. **Rotate SSH keys** and credentials regularly.

---

## Related Resources

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [Infrastructure as Code Concepts](https://www.thoughtworks.com/insights/blog/infrastructure-code-revisited)
- [AWS Security Best Practices](https://docs.aws.amazon.com/general/latest/gr/aws-security-best-practices.html)

---

*⚡ Pro tip: Use YAML for configuration and TypeScript for logic to keep your AWS stacks modular, maintainable, and easy to audit!*
