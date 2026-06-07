# Keystroke Logging System

A cybersecurity-focused educational project that demonstrates how keystroke data can be captured, transmitted, stored, and viewed using a client-server architecture.

This project consists of two independent components:

- **Python Keylogger** – Captures keystrokes and sends them to a remote server.
- **Node.js Server** – Receives, timestamps, stores, and displays captured data through a web interface.

> **Educational Purpose Only**
>
> This project was developed for cybersecurity learning, research, and demonstration purposes in a controlled environment. It is intended to help students and security enthusiasts understand how monitoring systems work and how such techniques may be detected, analyzed, and mitigated.

---

## Project Architecture

```text
┌─────────────────┐
│ Python Keylogger│
│                 │
│ • Capture Keys  │
│ • Get Username  │
│ • Buffer Data   │
└────────┬────────┘
         │ HTTP POST
         ▼
┌─────────────────┐
│ Node.js Server  │
│                 │
│ • Receive Data  │
│ • Add Timestamp │
│ • Save Logs     │
│ • Display Logs  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Log File        │
│                 │
│ keyboard_       │
│ capture.txt     │
└─────────────────┘
```

---

## Components

### Python Keylogger

Responsible for:

- Capturing keyboard input
- Capturing the current username
- Buffering keystroke data
- Sending data to the server via HTTP
- Running in the background

**Directory**
```text
Python-Keylogger/
```

### Node.js Server

Responsible for:

- Receiving client data
- Processing incoming requests
- Adding timestamps
- Storing logs in a text file
- Providing a browser-based log viewer

**Directory**
```text
node-server/
```

---

## Technologies Used

### Client Side

- Python
- pynput
- requests
- threading
- json
- getpass

### Server Side

- Node.js
- Express.js
- File System (fs)

---

## Repository Structure

```text
Keystroke-Logging-System/
│
├── Python-Keylogger/
│   ├── keylogger.py
│   ├── requirements.txt
│   └── README.md
│
├── node-server/
│   ├── server.js
│   ├── commands.txt
│   └── README.md
│
└── README.md
```

---

## Workflow

1. User types on the keyboard.
2. Python client captures keystrokes.
3. Data is buffered and processed.
4. Client sends the data to the Node.js server via HTTP POST.
5. Server receives the data.
6. Timestamp and username are added.
7. Data is stored in `keyboard_capture.txt`.
8. Logs can be viewed through the browser dashboard.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/zer0arc4/Keystroke-Logging-System.git
cd Keystroke-Logging-System
```

### Setup Node Server

```bash
cd node-server

npm install

node server.js
```

Server will start at:

```text
http://localhost:8080
```

### Setup Python Client

Open another terminal:

```bash
cd Python-Keylogger

pip install -r requirements.txt

python keylogger.py
```

---

## Sample Log Output

```text
[03/28/2026, 10:15:23 AM]=[User:zer0arc4]
hello world

[03/28/2026, 10:17:02 AM]=[User:zer0arc4]
testing data transfer
```

---

## Features

### Python Keylogger

- Real-time keystroke capture
- Username collection
- Data buffering
- HTTP-based transmission
- Background execution

### Node.js Server

- RESTful POST endpoint
- Live browser log viewer
- Automatic timestamping
- Persistent log storage
- Basic error handling

---

## Learning Objectives

This project demonstrates:

- Keyboard event monitoring
- Client-server communication
- HTTP requests
- Data logging
- File handling
- Web server development
- Cybersecurity monitoring concepts

---

## Security Considerations

The public version intentionally excludes advanced offensive techniques such as:

- Persistence mechanisms
- Process injection
- Evasion techniques
- Anti-analysis features
- Credential extraction

For deployments outside a local lab environment, consider implementing:

- HTTPS
- Authentication
- Authorization
- Access controls
- Input validation
- Log sanitization
- Secure storage practices

---

## Documentation

Additional setup and usage instructions are available inside:

- `Python-Keylogger/README.md`
- `node-server/README.md`

---

## Disclaimer

This project is intended solely for educational, research, and cybersecurity training purposes in environments where explicit authorization has been granted.

The author is not responsible for any misuse, unauthorized deployment, or activities that violate applicable laws, regulations, or organizational policies.

---

## Author

**Alakati Rithesh Chandra (zer0arc4)**

GitHub: https://github.com/zer0arc4

If you find this project useful, consider giving it a ⭐ on GitHub.
