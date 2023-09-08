# How to create a Python environment

## Information

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 07/09/2023 | 07/09/2023 | 1.0.0   |

## Problem

There are several reasons why you may need to start from a fresh Python environment. One common reason is to resolve dependency conflicts, which can occur when different packages or libraries require different versions of the same dependency. Starting from a fresh environment allows you to install the necessary dependencies without any conflicts.

Another reason is to ensure that the environment is set up correctly for a specific project or task. Different projects may require different versions of Python or different packages, and starting from a fresh environment ensures that the environment is configured correctly.

## Solution

To create a fresh Python environment with conda, you can use the following steps:

1. Open a terminal or command prompt.
2. Enter the command `conda create --name newenv python=3.9`, replacing `newenv` with the name you want to give your new environment.
3. Once the environment is created, activate it using the command `conda activate newenv`.
4. You can now install the necessary packages and dependencies for your project using `conda install` or `pip`.

Starting from a fresh environment with conda ensures that your environment is set up correctly and helps to avoid dependency conflicts, making it easier to work on your project.

### **Create a Fresh Environment**

It's often easier to start with a clean environment when resolving dependency conflicts. If you're using `conda`, you can create a new environment using the following command

```bash
conda create --name newenv python=3.9

```

### Activate the new environment

```bash
conda activate newenv

```

## Conda vs Miniforge

Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. It allows you to create, manage, and maintain isolated environments containing different versions of Python and/or different packages or libraries. This can be useful for managing dependencies and ensuring that your projects have the necessary environment to run correctly. Conda also provides a way to install, run, and update packages and dependencies in these environments using either the command line or a graphical user interface.

| Comparison Point | Conda | Miniforge |
| --- | --- | --- |
| Package Management | Conda provides package management functionality to create and manage isolated environments containing different versions of Python and/or different packages or libraries. | Miniforge is built on top of Conda and provides the same package management functionality as Conda. |
| Ease of Use | Conda is relatively easy to use, with both a command line interface and a graphical user interface available. | Miniforge is also easy to use, with both a command line interface and a graphical user interface available. |
| Speed | Conda can be slow to update and install packages due to its reliance on network connections and package repositories. | Miniforge is designed to be faster than Conda, with optimized package builds and faster download speeds. |
| Size | Conda has a larger installation size and higher storage requirements due to its inclusion of a full Python distribution and many pre-built packages. | Miniforge has a smaller installation size and lower storage requirements due to its focus on a minimal installation with only a few essential packages. |
| Compatibility | Conda is compatible with Windows, macOS, and Linux operating systems. | Miniforge is compatible with Windows, macOS, and Linux operating systems. |
| Customization | Conda provides a high degree of customization, with the ability to create custom environments and install packages from multiple sources. | Miniforge provides a similar level of customization, with the ability to create custom environments and install packages from multiple sources. |

Based on these comparison points, both Conda and Miniforge are strong options for package and environment management. Conda may be a better choice if you require a larger package repository or need more flexibility in terms of package sources and customization. Miniforge may be a better choice if you prioritize speed and a smaller footprint.
