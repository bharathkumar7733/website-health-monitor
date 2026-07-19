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
