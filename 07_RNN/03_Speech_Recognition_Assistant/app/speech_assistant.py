#!/usr/bin/env python3
import time
from utils.listener import listen
from utils.speaker import init, speak
import utils.commands as commands
import utils.config as config
import re

def match_command(text):
    """
    Basic intent matcher. Returns (intent, payload).
    """
    if not text:
        return None, None
    t = text.lower().strip()
    # remove hotword if present (word-boundary safe)
    t = re.sub(r'\b' + re.escape(config.HOTWORD) + r'\b', '', t).strip()

    # Normalize multiple spaces/punctuation
    t = re.sub(r'[^\w\s]', '', t).strip()

    if not t:
        return None, None
    if t.startswith('play '):
        return 'play', t
    if t.startswith('search '):
        return 'search', t
    if 'wikipedia' in t:
        return 'wikipedia', t
    if 'time' in t or 'what time' in t:
        return 'time', t
    if t.startswith('open '):
        return 'open', t
    return None, t

def run():
    init(voice_rate=150)
    speak("Hello, I am your assistant. Say 'Alexa' followed by a command to begin.")
    while True:
        print("Awaiting command... (say 'Alexa' then your command)")
        text = listen(timeout=config.LISTEN_TIMEOUT, phrase_time_limit=config.PHRASE_TIME_LIMIT, mic_index=config.MIC_INDEX)
        if text is None:
            time.sleep(0.2)
            continue
        intent, payload = match_command(text)
        print("Heard:", text, "Intent:", intent)
        if intent == 'play':
            commands.cmd_play(payload, speak)
        elif intent == 'search':
            commands.cmd_search(payload, speak)
        elif intent == 'wikipedia':
            commands.cmd_wikipedia(payload, speak)
        elif intent == 'time':
            commands.cmd_time(payload, speak)
        elif intent == 'open':
            commands.cmd_open_website(payload, speak)
        else:
            speak("Sorry, I didn't understand. Try saying play, search, wikipedia, time, or open.")

if __name__ == '__main__':
    run()
