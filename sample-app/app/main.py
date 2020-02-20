import socket
from flask import Flask
app = Flask(__name__)

@app.route("/cadastro")
def hello():
    html = "<h3>AWS Sample App!</h3><br/>" \
            "<h2>cadastro v0.0 </h2>" \
           "<b>Hostname:</b> {hostname}<br/>"

    return html.format(hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
