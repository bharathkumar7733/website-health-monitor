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

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.11 | Core runtime |
| **FastAPI** | 0.139 | REST API framework with async support |
| **Uvicorn** | 0.51 | ASGI server |
| **Pydantic** | 2.x | Request/response validation and serialization |
| **Requests** | 2.34 | Outbound HTTP health checks |
| **python-dotenv** | 1.2 | Environment variable management |
| **Threading** | stdlib | Daemon thread for continuous monitoring loop |

### Frontend
| Technology | Purpose |
|---|---|
| **HTML5 / CSS3** | Glassmorphism dashboard UI |
| **Vanilla JavaScript** | Async fetch API calls, live polling every 5 seconds |
| **FastAPI StaticFiles** | Serves the frontend directly — no separate web server needed |

### Integrations & Infrastructure
| Technology | Purpose |
|---|---|
| **ServiceNow REST API** | ITSM incident lifecycle — search & create via `/api/now/table/incident` |
| **Docker** | Containerised deployment with a single command |
| **Python Logging** | File-based structured logging to `logs/monitor.log` |

---

## 📡 API Reference

Base URL: `http://localhost:8000`
Interactive docs: `http://localhost:8000/docs`

### Endpoints

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/` | Serves the web dashboard | None |
| `POST` | `/monitor/check` | Run a single health check | None |
| `POST` | `/monitor/start` | Start continuous background monitoring | None |
| `POST` | `/monitor/stop` | Stop the background monitoring thread | None |
| `GET` | `/monitor/status` | Get current monitoring state & last result | None |

---

### `POST /monitor/check`

Performs an immediate health check and raises/returns a ServiceNow incident if the site is DOWN.

**Request body:**
```json
{
  "url": "https://www.example.com"
}
```

**Response — site UP:**
```json
{
  "status": "UP",
  "status_code": 200,
  "message": "Website is Healthy",
  "incident_number": null,
  "incident_action": null
}
```

**Response — site DOWN (new incident):**
```json
{
  "status": "DOWN",
  "status_code": 503,
  "message": "Server Error (503)",
  "incident_number": "INC0010042",
  "incident_action": "New incident created"
}
```

**Response — site DOWN (existing incident):**
```json
{
  "status": "DOWN",
  "status_code": null,
  "message": "Request Timed Out",
  "incident_number": "INC0010042",
  "incident_action": "Existing incident returned"
}
```

---

### `POST /monitor/start`

Starts a background daemon thread that checks the URL at the given interval.

**Request body:**
```json
{
  "url": "https://www.example.com",
  "interval": 30
}
```

**Response:**
```json
{
  "message": "Monitoring started",
  "url": "https://www.example.com",
  "interval": 30
}
```

**Error (already running):** `400 Bad Request` — `"Monitoring is already running"`

---

### `POST /monitor/stop`

Signals the monitoring thread to stop after its current sleep cycle.

**Response:**
```json
{
  "message": "Monitoring stopped"
}
```

---

### `GET /monitor/status`

Returns the current monitoring state, target URL, interval, and the last health check result.

**Response:**
```json
{
  "running": true,
  "url": "https://www.example.com",
  "interval": 30,
  "last_result": {
    "status": "UP",
    "status_code": 200,
    "message": "Website is Healthy"
  }
}
```
