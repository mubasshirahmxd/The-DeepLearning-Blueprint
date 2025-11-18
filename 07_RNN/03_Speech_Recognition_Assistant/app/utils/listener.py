import speech_recognition as sr
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("listener")

def list_mics():
    names = sr.Microphone.list_microphone_names()
    logger.info("Available microphones:")
    for i, n in enumerate(names):
        logger.info(f"  {i}: {n}")
    return names

def try_open_mic(device_index):
    """Return sr.Microphone instance if open succeeds, else raise."""
    try:
        mic = sr.Microphone(device_index=device_index)
        # try entering context to ensure stream is created
        with mic as source:
            # test if stream exists
            if getattr(source, "stream", None) is None:
                raise RuntimeError("Microphone opened but source.stream is None")
            return device_index
    except Exception as e:
        raise e

def find_working_mic(preferred_index=None):
    names = sr.Microphone.list_microphone_names()
    # Try preferred first
    candidates = []
    if preferred_index is not None:
        candidates.append(preferred_index)
    # then try obvious indices near 0..len-1
    candidates += list(range(len(names)))
    seen = set()
    for i in candidates:
        if i in seen or i is None:
            continue
        seen.add(i)
        try:
            logger.info(f"Trying microphone index {i}: {names[i] if i < len(names) else 'N/A'}")
            try_open_mic(i)
            logger.info(f"Working microphone found: {i} - {names[i]}")
            return i
        except Exception as e:
            logger.warning(f"Mic index {i} failed: {e}")
    raise RuntimeError("No working microphone found. Check drivers, PyAudio installation, or permissions.")

def listen(timeout=5, phrase_time_limit=7, recognizer=None, mic_index=None, energy_threshold=None):
    """
    Robust listener:
    - If mic_index fails, tries other devices
    - Avoids calling adjust_for_ambient_noise if the audio source doesn't expose a stream
    """
    r = recognizer or sr.Recognizer()
    # get a working mic index
    try:
        working_index = find_working_mic(preferred_index=mic_index)
    except Exception as e:
        logger.error("No microphone available: %s", e)
        return None

    try:
        with sr.Microphone(device_index=working_index) as mic:
            logger.info("Opened microphone %s", working_index)
            if energy_threshold:
                r.energy_threshold = energy_threshold
            # adjust for ambient noise only if stream present
            try:
                logger.info("Adjusting for ambient noise...")
                r.adjust_for_ambient_noise(mic, duration=1.0)
            except AssertionError as ae:
                logger.warning("adjust_for_ambient_noise failed (stream issue): %s", ae)
            except Exception as ex:
                logger.warning("adjust_for_ambient_noise warning: %s", ex)

            logger.info("Listening...")
            audio = r.listen(mic, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logger.info("Recognizing...")
            text = r.recognize_google(audio)
            logger.info("Recognized: %s", text)
            return text.lower()
    except sr.WaitTimeoutError:
        logger.info("Listening timed out.")
        return None
    except sr.UnknownValueError:
        logger.info("Could not understand audio.")
        return None
    except sr.RequestError as e:
        logger.error("Speech recognition request error: %s", e)
        return None
    except Exception as e:
        logger.exception("Unexpected error while listening:")
        return None
