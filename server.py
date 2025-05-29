from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

DATA_FILE = "saved_html.txt"

def load_chunks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def save_chunk(chunk):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(chunk.replace('\n', ' ') + "\n")

@app.route('/')
def index():
    chunks = load_chunks()
    saved_html = "\n".join(chunks)
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
  <title>CollabinHTML</title>
  <style>
    #htmlInput {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  </style>
</head>
<body>

  <textarea id="htmlInput" placeholder="Type HTML code and contribute to this page!&#10;Shift+Enter = newline&#10;Enter = add your HTML to the page" rows="5" cols="50"></textarea>
  <div id="output">{{ saved_html|safe }}</div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.6.1/socket.io.min.js"></script>
  <script>
    const socket = io();
    const textarea = document.getElementById("htmlInput");
    const output = document.getElementById("output");

    textarea.addEventListener("keydown", function(e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        const html = textarea.value.trim();
        if (html.length === 0) return;
        socket.emit('new_html', html);
        textarea.value = "";
      }
    });

    socket.on('update_html', function(html) {
      const div = document.createElement("div");
      div.innerHTML = html;
      output.appendChild(div);
    });
  </script>

</body>
</html>''', saved_html=saved_html)

@socketio.on('new_html')
def handle_new_html(html):
    save_chunk(html)
    emit('update_html', html, broadcast=True)

if __name__ == '__main__':
    print("Starting CollabinHTML server, have fun!")
    socketio.run(app, debug=False, host="0.0.0.0", port=3421)

