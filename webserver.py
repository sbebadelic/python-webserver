from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    for i in range(1, 10000):
        result += i ** 2
    return f"Hello, wafaewfraewfarld! {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)