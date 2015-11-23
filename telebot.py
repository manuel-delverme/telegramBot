# -*- coding: UTF-8 -*-
import telepot
import time
import requests
import hashlib
import pprint
from time import gmtime, strftime
molly = telepot.Bot(open("api_key").read()[:-1])

watchers = set()
manuel_id = 45571984

def log_message(msg):
    molly.sendMessage(manuel_id, pprint.pformat(msg))

def handle_message(msg):
    global watchers
    global molly
    user_id = msg['from']['id']
    try:
        msg_txt = msg['text']
    except KeyError:
        log_message("failed to parse the message")
        log_message(msg)
        return

    msg_txt = msg_txt.split(maxsplit=1)
    cmd = msg_txt[0]

    if cmd[0] == "/":
        cmd = cmd[1:]
    cmd = cmd.lower()

    if  cmd == "watch":
        watchers.add(user_id)
        molly.sendMessage(user_id, "added you to watchers")
        pprint.pprint(watchers)

    elif cmd == "!watch":
        try:
            watchers.remove(user_id)
        except KeyError as e:
            molly.sendMessage(user_id, "you can't unwatch!")
            log_message(e)
            log_message(msg)

    elif cmd == "spam":
        global oldHash
        oldHash = ""

    elif cmd == "ping":
        global checks
        molly.sendMessage(manuel_id, "{}; pong".format(checks))

    elif msg_txt is not None:
        molly.sendMessage(manuel_id, "someone is harrassing me")
        molly.sendMessage(manuel_id, pprint.pformat(msg))

def getHash():
    request = requests.get("http://led.delen.polito.it/direct_access/bookingstu.asp")
    end_static = request.content.find(b"<!-- - - - - - - - - - - fine corpo - - - - - - - - - - -->")
    return hashlib.md5(request.content[:end_static]).hexdigest()



molly.notifyOnMessage(handle_message)
oldHash = getHash()
checks = 0
while True:
    newHash = getHash()
    if newHash != oldHash:
        for watcher_id in watchers:
            molly.sendMessage(watcher_id, "BOOKING CHANGED!")
        oldHash = newHash
    time.sleep(3*60)  # 3 min
    checks += 1
    if checks == 3*20:
        checks = 0
        molly.sendMessage(manuel_id, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
