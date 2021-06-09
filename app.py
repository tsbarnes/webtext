import time
import sys

from microdotphat import write_string, scroll, show
from multiprocessing import Process

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    write_string('Hello World!', offset_x=0)
    return 'Hello World!'


def apploop():
    app.run()


if __name__ == '__main__':
    p = Process(target=apploop)
    p.start()

    write_string('Waiting...', offset_x=0)
    while True:
        scroll()
        show()
        time.sleep(1)

    p.join()
