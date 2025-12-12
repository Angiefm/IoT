# IoT Capstone Project - Environmental Monitoring API

#### Authors: Oscar Muñoz & Gustavo Vargas

## Description
This project implements a API for an Environmental Monitoring System. It collects, decodes, and exposes real-time environmental metrics (specifically temperature) for industrial settings. The system uses a FastAPI backend with SQLite storage and integrates with Node-RED for data flow management.

## Features
- **Real-time Data**: Retrieve the latest environmental sensor readings.
- **Historical Data**: Access a history of temperature recordings.
- **Data Ingestion**: Accept raw sensor data (hex encoded) via API.
- **Data Decoding**: Automatically decodes hex payloads into readable temperature values.
- **Node-RED Integration**: Ready-to-use flow for MQTT to API communication.

## Getting Started

### Prerequisites
- Python 3.8+
- Docker (for Node-RED)

### Installation
1. Clone the repository.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Start the FastAPI server using uvicorn:
```bash
uvicorn app:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Documentation

### Base URL
`http://127.0.0.1:8000`

### Endpoints

#### 1. Health Check
Returns a welcome message and service description.
- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "message": "IoT Final Capstone Project – Environmental Monitoring API. This service collects, decodes, and exposes real-time environmental metrics for industrial settings."
  }
  ```

#### 2. Get Latest Environment Data
Retrieves the most recent sensor reading.
- **URL**: `/environment`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "device": "device_id",
    "timestamp": "2023-10-27T10:00:00",
    "temperature": 25.5
  }
  ```

#### 3. Get History
Retrieves the last 10 temperature readings.
- **URL**: `/environment/history`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "temp": 25.5,
      "time": "2023-10-27T10:00:00"
    },
    {
      "temp": 24.8,
      "time": "2023-10-27T09:55:00"
    }
  ]
  ```

#### 4. Submit Sensor Data
Ingests raw sensor data. The `hexData` field is expected to contain the encoded sensor values.
- **URL**: `/environment`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "data": {
      "device": "device_id",
      "timestamp": "2023-10-27T10:00:00",
      "hexData": "41cc0000" 
    }
  }
  ```
- **Response**:
  ```json
  {
    "message": "success"
  }
  ```

## Node-RED Integration

### Setup
Run Node-RED using Docker:
```bash
docker run -it -p 1880:1880 -v node_red_data:/data --name iot_capstone nodered/node-red
```

- **Flow Editor**: [http://127.0.0.1:1880/](http://127.0.0.1:1880/)
- **Dashboard**: [http://127.0.0.1:1880/ui](http://127.0.0.1:1880/ui)

### Flow Configuration
Import the following JSON into Node-RED to configure the MQTT subscription and API interaction.

<details>
<summary>Click to expand Node-RED Flow JSON</summary>
</details>