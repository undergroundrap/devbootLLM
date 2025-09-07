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

### 2. Run the Docker Container (Hardened)

Once the image is built, start the server with a hardened container configuration that isolates it from your host to prevent any code from harming your machine.

Recommended (Windows/macOS/Linux):
```bash
docker run --rm \
  -p 3000:3000 \
  -e OLLAMA_URL=http://host.docker.internal:11434 \
  -e LMSTUDIO_URL=http://host.docker.internal:1234 \
  --read-only \
  --tmpfs /tmp:rw,noexec,nodev,nosuid,size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --pids-limit 128 \
  --memory 512m \
  --cpus 1 \
  devbootllm-app
```

Windows PowerShell (copy/paste):

```
docker run --rm `
  -p 3000:3000 `
  -e OLLAMA_URL=http://host.docker.internal:11434 `
  -e LMSTUDIO_URL=http://host.docker.internal:1234 `
  -v "$($PWD.Path):/usr/src/app:ro" `
  --read-only `
  --tmpfs "/tmp:rw,noexec,nodev,nosuid,size=64m" `
  --cap-drop ALL `
  --security-opt "no-new-privileges" `
  --pids-limit 128 `
  --memory 512m `
  --cpus 1 `
  devbootllm-app
```

Windows CMD (Command Prompt):

```
docker run --rm ^
  -p 3000:3000 ^
  -e OLLAMA_URL=http://host.docker.internal:11434 ^
  -e LMSTUDIO_URL=http://host.docker.internal:1234 ^
  -v "%cd%:/usr/src/app:ro" ^
  --read-only ^
  --tmpfs "/tmp:rw,noexec,nodev,nosuid,size=64m" ^
  --cap-drop ALL ^
  --security-opt "no-new-privileges" ^
  --pids-limit 128 ^
  --memory 512m ^
  --cpus 1 ^
  devbootllm-app
```

Notes:
- No host directories are mounted. This prevents untrusted code from modifying files on your PC.
- Filesystem is read-only; the app only writes to an in-memory `/tmp` with `noexec`, `nodev`, and `nosuid`.
- Container runs as a non-root user (from the image) with zero Linux capabilities and no privilege escalation.
- Basic resource limits (CPU, memory, PIDs) are enforced to mitigate abuse.

## Using Local Ollama

The AI assistant can use a local Ollama instance. To enable it:

- Install Ollama from https://ollama.com and ensure it runs on port 11434.
- Pull at least one model, for example: `ollama pull llama3.1`
- Start this app as usual. In the AI panel, pick a model from the dropdown. If no models appear, click refresh.

Container note:

- If you run this app in Docker and Ollama is on the host, set the env var `OLLAMA_URL` so the container can reach the host service:
  - macOS/Windows: `-e OLLAMA_URL=http://host.docker.internal:11434`
  - Linux (Docker Desktop): `-e OLLAMA_URL=http://host.docker.internal:11434` (enable host.docker.internal), or connect via your host IP.

If you need live-editing during development and accept higher risk, you may mount the project directory read-only:

```bash
docker run --rm \
  -p 3000:3000 \
  -e OLLAMA_URL=http://host.docker.internal:11434 \
  -e LMSTUDIO_URL=http://host.docker.internal:1234 \
  -v "${PWD}:/usr/src/app:ro" \
  --read-only \
  --tmpfs /tmp:rw,noexec,nodev,nosuid,size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --pids-limit 128 \
  --memory 512m \
  --cpus 1 \
  devbootllm-app
```

PowerShell variant for the hot‑reload (read‑only bind) run:

```
docker run --rm `
  -p 3000:3000 `
  -e OLLAMA_URL=http://host.docker.internal:11434 `
  -e LMSTUDIO_URL=http://host.docker.internal:1234 `
  -v "$($PWD.Path):/usr/src/app:ro" `
  --read-only `
  --tmpfs "/tmp:rw,noexec,nodev,nosuid,size=64m" `
  --cap-drop ALL `
  --security-opt "no-new-privileges" `
  --pids-limit 128 `
  --memory 512m `
  --cpus 1 `
  devbootllm-app
```

- `-p 3000:3000`: Maps port 3000 from the container to port 3000 on your local machine.
- `--rm`: Automatically removes the container when you stop it.
- `-v "${PWD}:/usr/src/app:ro"`: Optional, read-only bind mount for hot-reload workflows.

Windows tips:
- Use ``-v "$($PWD.Path):/usr/src/app:ro"`` in PowerShell so Docker sees your Windows path.
- Keep the `--tmpfs` value quoted as a single argument: `"/tmp:rw,noexec,nodev,nosuid,size=64m"`.
- If port 3000 is busy, use `-p 3100:3000` and open `http://localhost:3100`.

## Using LM Studio (Local)

The AI assistant can also connect to an LM Studio local server (OpenAI-compatible API).

- Install LM Studio and start the local server (default: `http://127.0.0.1:1234`).
- In the AI panel, choose `Provider: LM Studio`, then pick a model from the dropdown. Click refresh if needed.
- Optionally, configure the backend to a different URL via the `LMSTUDIO_URL` environment variable.

Docker examples (add alongside `OLLAMA_URL` if you use both):

```bash
docker run --rm \
  -p 3000:3000 \
  -e LMSTUDIO_URL=http://host.docker.internal:1234 \
  devbootllm-app
```

PowerShell example:

```
docker run --rm `
  -p 3000:3000 `
  -e LMSTUDIO_URL=http://host.docker.internal:1234 `
  devbootllm-app
```

### Security Hardening Summary

- Backend enforces code size limits and execution timeouts for Java and Python.
- Java runs with `-Xmx64m` to cap heap usage; both languages run in `/tmp` and are cleaned up.
- Container runs as non-root with a read-only filesystem and tight kernel capability set.
- No host filesystem is writable by the container in the recommended run mode.

### 3. Access the Application

With the container running, open your web browser and navigate to:

```
http://localhost:3000
```

You should now see the devbootLLM application running and ready to execute code.
