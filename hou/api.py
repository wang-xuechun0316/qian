import time
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/')
def get_current_time():
    return{'time':time.time()}
if __name__=='__main__':
    app.run()

