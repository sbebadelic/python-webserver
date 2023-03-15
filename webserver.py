from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    return f"Hello, wafaewfraewfarld! {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)