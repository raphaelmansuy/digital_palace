---
title: "Steampipe"
slug: "steampipe"
category: "tool"
tags: [sql, cloud, devops, open-source, data, api, zero-etl]
last_updated: "2025-07-22"
status: "active"
---

# Steampipe

Steampipe is an open-source tool that lets you query APIs, cloud services, SaaS platforms, and more using SQL. It provides a zero-ETL approach, allowing you to access live data from over 140 sources without the need for data pipelines or synchronization.

## Key Features
- Query cloud, SaaS, and API data with standard SQL
- Zero-ETL: no data movement or sync required
- 500+ plugins for AWS, Azure, GCP, GitHub, Kubernetes, and more
- Use as a CLI, Postgres FDW, or SQLite extension
- Open source (AGPLv3), developed by Turbot
- Active community and plugin ecosystem

## Use Cases
- Compliance and security audits
- Cloud cost and resource management
- Operations and monitoring
- Data exploration and reporting

## Getting Started
- [Official Website](https://steampipe.io/)
- [Documentation](https://steampipe.io/docs)
- [GitHub Repository](https://github.com/turbot/steampipe)
- [Plugin Hub](https://hub.steampipe.io/)
- [Community Slack](https://turbot.com/community/join)

## Example Query
```sql
select name, runtime from aws_lambda_function;
```

## Related Tools
- [Powerpipe](https://powerpipe.io/): Dashboards for DevOps
- [Flowpipe](https://flowpipe.io/): Workflow automation for DevOps
- [Tailpipe](https://tailpipe.io/): Open source SIEM for log analysis



## Steampipe MCP Integration

Steampipe supports the [Model Context Protocol (MCP)](./mcp.md), a standard for connecting AI assistants and tools to live data sources. With MCP, Steampipe can act as a bridge between SQL-based data access and AI agents, enabling:

- Secure, real-time data access for AI assistants (e.g., Claude Desktop, Cursor, Continue)
- Integration with the broader MCP ecosystem for tool and data interoperability
- Use of Steampipe as an MCP server for querying APIs, cloud, and SaaS data via standardized protocols

**Learn more:**

- [Steampipe MCP Documentation](https://steampipe.io/docs/query/mcp)
- [Model Context Protocol (MCP) Overview](./mcp.md)
- [Official MCP Site](https://modelcontextprotocol.io/)


## References

- [Steampipe Blog](https://steampipe.io/blog)
- [Steampipe Changelog](https://steampipe.io/changelog)
- [Turbot Pipes](https://turbot.com/pipes)

---
*For more, see the [AI Tools Master Directory](../tools/ai-tools-master-directory.md) and [Concepts Index](./README.md).*
