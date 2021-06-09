import time
import sys

from microdotphat import write_string, scroll, show
from multiprocessing import Process

from flask import Flask
app = Flask(__name__)


def scroll_loop():
    while True:
        scroll()
        show()
        time.sleep(0.05)


with app.app_context():
    write_string('Waiting...')

    p = Process(target=scroll_loop)
    p.start()


@app.route('/')
def hello_world():
    write_string('Hello World!')
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    p.join()
