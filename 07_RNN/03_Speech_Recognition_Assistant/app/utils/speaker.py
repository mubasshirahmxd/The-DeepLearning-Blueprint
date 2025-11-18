import pyttsx3

_engine = None

def init(voice_rate=150, voice_id=None):
    """
    Initialize the pyttsx3 engine once. Optionally set voice_rate and voice_id (part of voice name).
    """
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty('rate', voice_rate)
        if voice_id is not None:
            voices = _engine.getProperty('voices')
            for v in voices:
                if voice_id.lower() in v.name.lower():
                    _engine.setProperty('voice', v.id)
                    break

def speak(text, block=True):
    """
    Speak text out loud. If block=False it will queue the speech (but pyttsx3 is synchronous by default).
    """
    global _engine
    if _engine is None:
        init()
    _engine.say(text)
    if block:
        _engine.runAndWait()

def stop():
    global _engine
    if _engine is not None:
        _engine.stop()
