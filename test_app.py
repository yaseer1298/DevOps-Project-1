import requests
import multiprocessing
import time
import app
from app import app as _app

def run_app():
    _app.run(host="0.0.0.0", port=5000)

def test_root_endpoint():
    # start the Flask app in another process for the test
    p = multiprocessing.Process(target=run_app, daemon=True)
    p.start()
    time.sleep(1)  # give the server a moment to start
    try:
        r = requests.get("http://127.0.0.1:5000/")
        assert r.status_code == 200
        assert r.json().get("message") == "hello from flask"
    finally:
        p.terminate()
        p.join(timeout=1)
