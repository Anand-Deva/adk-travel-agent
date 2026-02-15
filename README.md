# ADK Project: Docker & Kubernetes Deployment Guide

This repository is developed using Google Agent Development Kit (ADK) and and openAI application for a **Travel Plan Agent** designed to help users plan trips. 

This guide explains how to containerize the application using `uv` and deploy it to a local Kubernetes (Minikube) cluster.

---

## 🚀 1. Docker Image & Kubernetes deployment 

The Dockerfile uses a multi-stage approach with `uv` to ensure a fast, lightweight, and reproducible environment.

### Prerequisites
- **Docker Desktop** installed and running.
- Ensure the `pyproject.toml` includes `google-adk` in the dependencies.

### Build the Image
From the root of the project (where the Dockerfile is located), run:
```bash
docker build -t <image_name>:<tag> .
```

### Sideloading to Minikube
Sideload the image to minikube "built-in" registries
```bash
minikube image load <image_name>:<tag>
```
### Deploy Kubernetes Deployment & Service
Deploy the K8 resources
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
### Access the Application
Minikube operates in an isolated environment,a tunnel need to reach the service
```bash
minikube service adk-service
```
