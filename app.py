from flask import Flask, render_template, request
import posix_ipc


app = Flask(__name__)
mq = posix_ipc.MessageQueue("/webtext_ipc")
mq.block = False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mq.send(request.form["text"], timeout=10)
        return 'Sent to screen!'
    else:
        return render_template('index.html')


@app.route('/test')
def hello_world():
    mq.send('Hello World!', timeout=10)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
