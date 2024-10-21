from flask import Flask, render_template
from weather.scheduler import start_scheduler
from database import mongo_init

app = Flask(__name__)

# Initialize MongoDB
mongo_init(app)

# Start the scheduler to pull data at intervals
start_scheduler()

@app.route('/')
def index():
    # Render the frontend
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
