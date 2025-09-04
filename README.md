# devbootLLM - Local Code Execution Environment

This project transitions the devbootLLM application from a front-end only simulation to a full-stack application with a local server for executing code. This allows users to run actual Java and Python code securely in an isolated environment.

## Project Structure

Here is the file structure for the project:

```
/devbootllm-app/
|-- public/
|   |-- index.html         # The front-end web application
|-- Dockerfile            # Instructions to build the Docker container
|-- package.json          # Node.js project dependencies
|-- server.js             # The local Express.js server for code execution
```

### Explanation of Components:

- **/devbootllm-app/**: The root directory for your project.
- **public/**: This folder holds all static front-end files, primarily index.html.
- **server.js**: The Node.js and Express.js backend. It exposes API endpoints (/run/java, /run/python) that receive code, save it to a temporary file, execute it using a child process, capture the output, and send it back to the front-end.
- **package.json**: The standard manifest file for a Node.js project, listing dependencies like express.
- **Dockerfile**: A script to automatically build a container image with Node.js, the Java Development Kit (JDK), and Python installed. This creates a consistent and portable development environment.

## How to Run

Follow these steps to build the Docker image and run the application.

### Prerequisites

You must have Docker Desktop installed and running on your system (Windows, macOS, or Linux).

### 1. Build the Docker Image

Open your terminal (PowerShell, Command Prompt, or any Linux/macOS terminal), navigate to the root devbootllm-app directory, and run the following command. This will create a Docker image named devbootllm-app based on the Dockerfile.

```bash
docker build -t devbootllm-app .
```

> **Note:** The `.` at the end of the command is important as it specifies the build context.

### 2. Run the Docker Container

Once the image is built, run the container with the command below. This will start the server and make the application available on port 3000.

**For Windows (PowerShell):**
```powershell
docker run -p 3000:3000 -v "${PWD}:/usr/src/app" -v "/usr/src/app/node_modules" --rm devbootllm-app
```

## Using Local Ollama

The AI assistant can use a local Ollama instance. To enable it:

- Install Ollama from https://ollama.com and ensure it runs on port 11434.
- Pull at least one model, for example: `ollama pull llama3.1`
- Start this app as usual. In the AI panel, pick a model from the dropdown. If no models appear, click refresh.

Container note:

- If you run this app in Docker and Ollama is on the host, set the env var `OLLAMA_URL` so the container can reach the host service:
  - macOS/Windows: `-e OLLAMA_URL=http://host.docker.internal:11434`
  - Linux (Docker Desktop): `-e OLLAMA_URL=http://host.docker.internal:11434` (enable host.docker.internal), or connect via your host IP.

Examples:

**Windows (PowerShell):**
```powershell
docker run -p 3000:3000 -e OLLAMA_URL=http://host.docker.internal:11434 -v "${PWD}:/usr/src/app" -v "/usr/src/app/node_modules" --rm devbootllm-app
```

**macOS or Linux:**
```bash
docker run -p 3000:3000 -e OLLAMA_URL=http://host.docker.internal:11434 -v "$(pwd):/usr/src/app" -v /usr/src/app/node_modules --rm devbootllm-app
```

- `-p 3000:3000`: Maps port 3000 from the container to port 3000 on your local machine.
- `-v ...`: Mounts your local code directory into the container, allowing you to edit files locally and see changes instantly without rebuilding the image.
- `--rm`: Automatically removes the container when you stop it (e.g., by pressing Ctrl+C in the terminal).

### 3. Access the Application

With the container running, open your web browser and navigate to:

```
http://localhost:3000
```

You should now see the devbootLLM application running and ready to execute code.
