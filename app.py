import time
import sys

from microdotphat import write_string, scroll, show
from multiprocessing import Process, Value

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    write_string('Hello World!', offset_x=0)
    return 'Hello World!'

def scroll_loop(args):
    while True:
        scroll()
        show()
        time.sleep(1)

if __name__ == '__main__':
    write_string('', offset_x=0)
    recording_on = Value('b', True)
    p = Process(target=scroll_loop, args=(recording_on,))
    p.start()
    app.run(debug=True, use_reloader=False)
    p.join()
