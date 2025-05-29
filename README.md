# CollabinHTML

### What is it?

A basic web app that lets multiple users add HTML snippets live. Everyone sees new code instantly on the page. The HTML bits are saved to a file so they don’t vanish when the server restarts. (Live Version at http://37.27.51.34:3421/)

### How to run it

1. Install Python 3 if you don’t have it.
2. Install the required packages:

```
pip install flask flask-socketio
```

3. Run the server:

```
python your_script_name.py
```

4. Go to `http://localhost:3421` in your browser.

### How to use it

* Type your HTML in the input box.
* Press `Enter` to submit.
* Press `Shift+Enter` for a newline.
* Submitted HTML appears live on the page for everyone.
* All submitted HTML is saved in `saved_html.txt`.

---

### ⚠️ SECURITY WARNING: XSS Risk

This app **does not sanitize** any user input.

That means users can submit **malicious HTML/JS**, like:

```html
<script>alert("owned")</script>
```

This will **actually run** on everyone’s browser. So yeah — don't run this on a public server unless you're cool with trolls injecting sketchy scripts.

This app is for learning or internal use only. If you plan to make it public, you **MUST** add input sanitization or filtering. Seriously. Since I love chaos; I didn't sanitize input and allowed users to run whatever code they want! So be warned and use this at your OWN risk!!!

---

### Tech Stack

* Python + Flask
* Flask-SocketIO
* Vanilla JS frontend
