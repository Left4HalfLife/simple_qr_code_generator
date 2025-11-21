# Simple QR Code Generator

A simple Flask web application for generating QR codes from text or URLs. The app runs in a Docker container and provides a clean, user-friendly interface.

## Features

- Generate QR codes from any text or URL
- Clean, responsive web interface
- Runs in a Docker container
- Accessible on port 5003

## Prerequisites

- Docker installed on your system
- No other services running on port 5003

## Building the Docker Container

To build the Docker image, run the following command from the project directory:

```bash
docker build -t simple-qr-generator .
```

## Running the Docker Container

### Run in headless mode (detached):

```bash
docker run -d -p 5003:5003 --name qr-generator simple-qr-generator
```

This will:
- Run the container in detached mode (`-d`)
- Map port 5003 on your host to port 5003 in the container (`-p 5003:5003`)
- Name the container `qr-generator` (`--name qr-generator`)

### Run in foreground mode (with logs):

```bash
docker run -p 5003:5003 --name qr-generator simple-qr-generator
```

## Accessing the Application

Once the container is running, open your web browser and navigate to:

```
http://localhost:5003
```

## Using the Application

1. Enter any text or URL in the text box
2. Click "Generate QR Code"
3. Your QR code will be displayed on the page
4. You can scan the QR code with any QR code reader

## Managing the Container

### Stop the container:
```bash
docker stop qr-generator
```

### Start the container again:
```bash
docker start qr-generator
```

### Remove the container:
```bash
docker rm qr-generator
```

### View logs:
```bash
docker logs qr-generator
```

### View real-time logs:
```bash
docker logs -f qr-generator
```

## Development

### Running without Docker

If you want to run the application without Docker:

1. Install Python 3.11 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access at `http://localhost:5003`

## Project Structure

```
.
├── app.py              # Flask application
├── templates/
│   └── index.html      # Web interface
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .dockerignore       # Docker ignore file
└── README.md           # This file
```

## License

This project is open source and available under the MIT License.
