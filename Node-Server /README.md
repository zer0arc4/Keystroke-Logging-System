# Server (Node.js)

A lightweight Node.js and Express backend designed to receive, timestamp, and log incoming data strings to a local text file. This server provides a real-time web interface to view logs directly in the browser with auto-refresh functionality.

## Features

* **RESTful POST Endpoint:** Accepts JSON payloads and appends them to a persistent log file.
* **Live Web Viewer:** A dedicated GET route to view the data buffer with a 3-second auto-refresh.
* **Automated Timestamping:** Every entry is logged with a localized system timestamp and username.
* **Error Resilience:** Basic error handling for file system operations to prevent server crashes.

## Tech Stack
* **Runtime:** Node.js
* **Framework:** Express.js
* **Storage:** Native fs (File System) module

## Prerequisites
Before you begin, ensure you have met the following requirements:
* [Node.js](https://nodejs.org/) (v14.x or higher recommended)
* npm or yarn installed

## Installation & Setup

1. **Clone the repository**
```
git clone https://github.com/zer0arc4/Node-Server.git
 ```
2. **Install the dependencies:**
```
sudo apt update
sudo apt upgrade
sudo apt install nodejs
sudo apt install npm
sudo npm init -y
sudo npm install express
sudo npm install 
sudo reboot
```
3. **Run the server**
```
node server.js
```
4. **Access the dashboard**
```
http://localhost:8080
```

## How It Works
1. Client sends keystroke data via HTTP POST
2. Server receives and validates data
3. Adds timestamp and username
4. Stores data in keyboard_capture.txt
5. Displays logs in browser (auto-refresh)

## Sample Output
[03/28/2026, 10:15:23 AM]=[User:zer0rc4]  
hello world  
password123

## ⚠️ Important Note on Security
This server is designed for local development and debugging. If you plan to deploy this to a public server:  
* **Enable HTTPS:** Protect data in transit.  
* **Add Authentication:** Implement middleware to ensure only authorized clients can POST or GET logs.  
* **Sanitize Output:** The current viewer renders raw data; ensure you escape HTML if logging untrusted input to prevent XSS.

## Keylogger 
You can find the Python Keyloger here :

https://github.com/zer0arc4/Python-Keylogger.git

## Author
Developed by : **zer0arc4**  
If you find this project useful, consider giving it a star ⭐
