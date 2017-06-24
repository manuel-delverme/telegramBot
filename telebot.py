# -*- coding: UTF-8 -*-
import telepot
import time
import requests
import hashlib
import pprint
from time import gmtime, strftime

manuel_id = 45571984

class Secretary(object):
    def __init__(self, key):
        self.sekretai = telepot.Bot(key)
        self.sekretai.notifyOnMessage(self.handle_message)

    def log_message(self, msg):
        self.sekretai.sendMessage(manuel_id, pprint.pformat(msg))

    def handle_message(msg):
        user_id = msg['from']['id']
        try:
            msg_txt = msg['text']
            intent = msg['intent']
            target = msg['target']
        except KeyError:
            log_message("failed to parse the message")
            log_message(msg)
            return

        msg_txt = msg_txt.split(maxsplit=1)
        cmd = msg_txt[0]

        if cmd[0] == "/":
            cmd = cmd[1:]
        cmd = cmd.lower()

        if cmd == "ping":
            self.sekretai.sendMessage(manuel_id, "{}; pong".format(checks))

    def handle_knowledge(self):
        pass

    def spin(sefl):
        while True:
            self.sekretai.sendMessage(watcher_id, "BOOKING CHANGED!")
            sleep(1)


if __name__ == "__main__":
    with open("api_key") as fin:
        bot = Secretary(fin.read()[:-1])
    bot.spin()
