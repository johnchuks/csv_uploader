from datetime import datetime
from flask import Flask, render_template
from db.mongo import MongoDatabase

app = Flask(__name__)

@app.route('/logs')
def get_temperature_logs():
    temperature_log_collection = MongoDatabase("temperature-logs")
    request_log_Collection = MongoDatabase("request-logs")
    results = []
    logs = temperature_log_collection.query()
    for log in logs:
        results.append(log)

    new_request_log = {
        "timestamp": datetime.utcnow(),
        "url": "/logs",
        "message": 'Temperature logs retrieved'
    }
    request_log_Collection.insert_one(new_request_log)
    return render_template('temperature_logs.html', results=results)


if __name__ == '__main__':
    app.run()
