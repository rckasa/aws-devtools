import socket
from flask import Flask
app = Flask(__name__)

@app.route("/teste-python")
def hello():
    html = "<h3>AWS Sample App!</h3><br/>" \
            "<h2>teste-python v0.0 </h2>" \
           "<b>Hostname:</b> {hostname}<br/>" \
            "My Password is: secret123"

    return html.format(hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
