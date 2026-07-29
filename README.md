<div align="center">

# 🌐 Website Health Monitor

### Real-time website availability monitoring with automated ServiceNow incident management

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![ServiceNow](https://img.shields.io/badge/ServiceNow-ITSM-62D84E?style=for-the-badge&logo=servicenow&logoColor=white)](https://developer.servicenow.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> **Monitor any website. Detect outages instantly. Auto-create ServiceNow incidents.**
> A production-style monitoring tool built with FastAPI, a real-time dashboard, and full ITSM integration.

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏗️ Architecture](#️-architecture)
- [📡 API Reference](#-api-reference)
- [🚀 Quick Start](#-quick-start)
- [🐳 Docker Deployment](#-docker-deployment)
- [📸 Screenshots](#-screenshots)
- [🎬 Demo Video](#-demo-video)
- [📁 Project Structure](#-project-structure)
- [🏷️ Resume Bullet Points](#️-resume-bullet-points)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Instant Health Check** | One-click HTTP check with status code, latency classification, and error diagnosis |
| 🔄 **Continuous Monitoring** | Background daemon thread polls a URL at configurable intervals (10s → 5min) |
| 🎫 **Incident Deduplication** | Searches ServiceNow for an existing active incident before creating a new one |
| 🚨 **Auto Incident Creation** | Automatically raises P2 incidents in ServiceNow when a site goes DOWN |
| 📊 **Live Dashboard** | Vanilla JS frontend polls `/monitor/status` every 5 seconds — no page refresh needed |
| 🐳 **Docker Ready** | Single `docker run` command gets the full stack running |
| 📝 **Structured Logging** | Timestamped log file with INFO / WARNING / ERROR levels in `logs/monitor.log` |
| ⚡ **Auto Docs** | FastAPI auto-generates interactive Swagger UI at `/docs` |
