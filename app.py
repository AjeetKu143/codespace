from flask import Flask
import subprocess
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Ajeet Kumar"
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout

    return f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
