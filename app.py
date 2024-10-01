from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/https', methods=['GET', 'POST'])
def https_trigger():
    log_data = {
        'method': request.method,
        'headers': dict(request.headers),
        'query_params': request.args,
        'body': request.data.decode('utf-8') if request.data else None
    }
    app.logger.info(f"HTTPS Trigger: {log_data}")
    return 'HTTPS trigger received', 200

@app.route('/scheduler', methods=['POST'])
def scheduler_trigger():
    timestamp = datetime.utcnow().isoformat()
    payload = request.data.decode('utf-8') if request.data else None
    app.logger.info(f"Scheduler Trigger at {timestamp} with payload: {payload}")
    return 'Scheduler trigger executed', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
