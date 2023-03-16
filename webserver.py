from flask import Flask
import socket
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis-service', port=6379)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    result = 0
    for i in range(1, 100000):
        result += i ** 2
    cache.incr('hits')
    
    return f"Hello, wafaewfraewfarld! {ip_address} with hitcount {cache.get('hits')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)