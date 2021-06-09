import time
import sys

from microdotphat import write_string, scroll, show
from multiprocessing import Process

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    write_string('Hello World!')
    return 'Hello World!'

def scroll_loop():
    while True:
        scroll()
        show()
        time.sleep(1)

if __name__ == '__main__':
    write_string('Waiting...')

    p = Process(target=scroll_loop)
    p.start()

    app.run()

    p.join()
