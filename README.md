# Website Health Monitor

A lightweight website health monitoring application built with FastAPI and integration with ServiceNow for incident management.

## Prerequisites

- Python 3.10+
- A ServiceNow Developer Instance

## Setup Instructions

1. Copy `.env.example` to `.env` and fill in your ServiceNow credentials:
   ```bash
   cp .env.example .env
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Features

- **Single Health Check**: Immediately query a website's health state.
- **Continuous Monitoring**: Run monitoring on a daemon thread at regular intervals.
- **ServiceNow Integration**: Automatically searches for existing incidents or creates new ones if a website goes down.
