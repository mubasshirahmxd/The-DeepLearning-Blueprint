# streamlit_app.py
import streamlit as st
import time
import threading
from utils import listener as listener_mod
from utils import speaker as speaker_mod
from utils import commands as commands_mod
import utils.config as config
import re

st.set_page_config(page_title="Speech Assistant UI", layout="wide")

# ---- helper: reuse match_command from your assistant but small copy here ----
def match_command(text):
    if not text: 
        return None, None
    t = text.lower().strip()
    t = re.sub(r'\b' + re.escape(config.HOTWORD) + r'\b', '', t).strip()
    t = re.sub(r'[^\w\s]', '', t).strip()
    if not t: return None, None
    if t.startswith('play '): return 'play', t
    if t.startswith('search '): return 'search', t
    if 'wikipedia' in t: return 'wikipedia', t
    if 'time' in t or 'what time' in t: return 'time', t
    if t.startswith('open '): return 'open', t
    return None, t

# ---- session state ----
if "history" not in st.session_state:
    st.session_state.history = []  # list of (timestamp, recognized_text, intent, action_result)

if "listening" not in st.session_state:
    st.session_state.listening = False

# ---- UI layout ----
st.title("🔊 Speech Assistant — Streamlit UI")
col1, col2 = st.columns([2, 1])

with col2:
    st.markdown("### Settings")
    mic_index = st.number_input("Mic index (None = auto)", min_value=-1, max_value=64, value=-1, step=1)
    if mic_index == -1:
        selected_mic = None
    else:
        selected_mic = int(mic_index)
    if st.button("List microphones"):
        names = listener_mod.list_mics()
        st.write("Microphones (index: name):")
        for i, n in enumerate(names):
            st.write(f"{i} — {n}")

    st.markdown("---")
    if st.button("Initialize TTS"):
        speaker_mod.init()
        st.success("TTS initialized")

    st.markdown("**Hotword**: `" + config.HOTWORD + "`")
    st.markdown("---")
    st.markdown("### Manual Controls")
    manual_text = st.text_input("Type a command (or press Listen below and speak)", "")
    if st.button("Run typed command"):
        # process typed command immediately (no listen)
        text = manual_text.strip().lower()
        if text:
            if config.HOTWORD in text:
                text = text.replace(config.HOTWORD, "").strip()
            intent, payload = match_command(text)
            res = "no_action"
            if intent == 'play':
                res = commands_mod.cmd_play(payload, speaker_mod.speak)
            elif intent == 'search':
                res = commands_mod.cmd_search(payload, speaker_mod.speak)
            elif intent == 'wikipedia':
                res = commands_mod.cmd_wikipedia(payload, speaker_mod.speak)
            elif intent == 'time':
                res = commands_mod.cmd_time(payload, speaker_mod.speak)
            elif intent == 'open':
                res = commands_mod.cmd_open_website(payload, speaker_mod.speak)
            else:
                speaker_mod.speak("Sorry, I didn't understand that command.")
            st.session_state.history.insert(0, (time.strftime("%H:%M:%S"), text, intent, str(res)))
            st.experimental_rerun()

with col1:
    st.markdown("### Live Controls & Status")
    listen_button = st.button("🎤 Listen once")
    continuous = st.checkbox("Continuous listening (every 5s)", value=False)
    status_text = st.empty()
    recognized = st.empty()
    action_area = st.empty()

    # show history
    st.markdown("### Recent Activity")
    history_table = st.empty()
    def render_history():
        if st.session_state.history:
            rows = [
                {"time": t, "recognized": txt, "intent": it, "result": r}
                for (t, txt, it, r) in st.session_state.history[:30]
            ]
            history_table.table(rows)
        else:
            history_table.write("No activity yet.")

    render_history()

# ---- listening worker function ----
def do_listen_once(mic_index=None):
    status_text.info("Adjusting & listening...")
    text = listener_mod.listen(timeout=6, phrase_time_limit=8, mic_index=mic_index)
    if text is None:
        status_text.warning("No speech recognized (timeout or unclear).")
        return None, None
    status_text.success("Recognized: " + text)
    intent, payload = match_command(text)
    result = None
    if intent == 'play':
        result = commands_mod.cmd_play(payload, speaker_mod.speak)
    elif intent == 'search':
        result = commands_mod.cmd_search(payload, speaker_mod.speak)
    elif intent == 'wikipedia':
        result = commands_mod.cmd_wikipedia(payload, speaker_mod.speak)
    elif intent == 'time':
        result = commands_mod.cmd_time(payload, speaker_mod.speak)
    elif intent == 'open':
        result = commands_mod.cmd_open_website(payload, speaker_mod.speak)
    else:
        speaker_mod.speak("Sorry, I didn't understand. You can type a command too.")
    st.session_state.history.insert(0, (time.strftime("%H:%M:%S"), text, intent, str(result)))
    render_history()
    return text, result

# ---- handle listen button ----
if listen_button:
    # run the blocking listener in another thread to avoid freezing Streamlit UI
    t = threading.Thread(target=do_listen_once, kwargs={"mic_index": selected_mic}, daemon=True)
    t.start()

# ---- continuous listening handler ----
if continuous:
    if not st.session_state.listening:
        st.session_state.listening = True
        def continuous_worker():
            try:
                while st.session_state.listening:
                    do_listen_once(mic_index=selected_mic)
                    time.sleep(1.0)  # small pause - increase if noisy
            except Exception as e:
                st.error(f"Continuous listen stopped: {e}")
                st.session_state.listening = False
        threading.Thread(target=continuous_worker, daemon=True).start()
    else:
        st.info("Continuous listening already running.")
else:
    # stop continuous listening if it was on
    if st.session_state.listening:
        st.session_state.listening = False
        st.info("Stopping continuous listening...")

st.caption("Run locally (streamlit run streamlit_app.py). Server-side mic capture only works when running on the same machine that has the microphone.")
