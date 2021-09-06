import time
from microdotphat import write_string, scroll, show


def scroll_loop():
    while True:
        scroll()
        show()
        time.sleep(0.05)


write_string('Waiting...')

if __name__ == '__main__':
    scroll_loop()
