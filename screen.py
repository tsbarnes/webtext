import time
from microdotphat import write_string, scroll, show
import posix_ipc


write_string('Waiting...')

mq = posix_ipc.MessageQueue("/webtext_ipc", flags=posix_ipc.O_CREAT)
mq.block = False

if __name__ == '__main__':
    while True:
        scroll()
        show()
        try:
            message = mq.receive(timeout=10)
        except posix_ipc.BusyError:
            message = None

        if message:
            write_string(" " + message[0].decode() + " ")

        time.sleep(1)
