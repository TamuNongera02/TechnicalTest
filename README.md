# Technical Test

This project demonstrates setting up VMs, MicroK8s clusters, Temporal.io, and Neo4j instances, along with deploying a simple Temporal.io workflow.

## Components

1. VM Setup:
   - Setting up 2 Virtual Machines created using VirtualBox.
   - Ubuntu is installed as the operating system.

2. MicroK8s:
   - MicroK8s is used to create a lightweight Kubernetes environment.

3. Temporal.io:
   - Temporal.io is used for reliable workflow orchestration.
   - Docker Compose is used to deploy Temporal services.

4. Neo4j:
   - Neo4j is a graph database used to manage connected data.

## Connectivity

- MicroK8s:
  - Add-ons like DNS, Dashboard, Storage, and Ingress are enabled for connectivity and service discovery.
- Temporal.io:
  - Deployed using Docker Compose, accessible via `http://localhost:8088`.
- Neo4j:
  - Accessible via `http://localhost:7474`.

## Workflow Logic

- Simple Workflow:
  - The workflow initiates a single activity that returns a greeting message.
- Activity:
  - The activity logs a message and returns a greeting.

## Challenges and Solutions

- Challenges: Ensuring all services start correctly and communicate effectively.
  - Solution: Used Docker Compose for Temporal services to manage dependencies and service startup.
- Challenge: Managing different versions of dependencies.
  - Solution: Utilized virtual environments and containerization to isolate environments.

## Why These Technologies

- MicroK8s: Lightweight Kubernetes suitable for development and testing environments.
- Temporal.io: Provides reliable and scalable workflow orchestration.
- Neo4j: Efficiently manages and queries highly connected data.

## Running the Project


