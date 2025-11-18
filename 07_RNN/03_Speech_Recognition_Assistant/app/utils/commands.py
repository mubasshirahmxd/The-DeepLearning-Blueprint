import webbrowser
import pywhatkit as pk
import wikipedia
from datetime import datetime

def cmd_play(text, speak_func=None):
    """Play a song on YouTube using pywhatkit.playonyt"""
    query = text.replace('play', '').strip()
    if not query:
        if speak_func: speak_func("Please tell me the song name to play.")
        return "no_query"
    if speak_func: speak_func(f"Playing {query} on YouTube")
    try:
        pk.playonyt(query)
        return f"playing:{query}"
    except Exception as e:
        if speak_func: speak_func("Sorry, I couldn't play that.")
        return f"error:{e}"

def cmd_search(text, speak_func=None):
    """Open a Google search in the default browser"""
    query = text.replace('search', '').strip()
    if not query:
        if speak_func: speak_func("Please provide a search query.")
        return "no_query"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    if speak_func: speak_func(f"Here are the search results for {query}")
    return f"search:{query}"

def cmd_wikipedia(text, speak_func=None):
    """Get a short Wikipedia summary and speak it"""
    query = text.replace('wikipedia', '').strip()
    if not query:
        if speak_func: speak_func("Please specify a topic for Wikipedia.")
        return "no_query"
    try:
        summary = wikipedia.summary(query, sentences=2)
        if speak_func: speak_func(summary)
        return summary
    except Exception as e:
        if speak_func: speak_func("I couldn't find information on that topic.")
        return f"error:{e}"

def cmd_time(text, speak_func=None):
    """Tell the current local time"""
    now = datetime.now().strftime("%I:%M %p")
    if speak_func: speak_func(f"The current time is {now}")
    return now

def cmd_open_website(text, speak_func=None):
    """
    Open a website like 'open youtube' or 'open github'.
    If the last word matches a known site, open mapped URL, otherwise attempt to open as-is.
    """
    parts = text.split()
    if len(parts) < 2:
        if speak_func: speak_func("Please say open followed by the website name.")
        return "no_query"
    site = parts[-1]
    mapping = {
        'youtube': 'https://www.youtube.com',
        'google': 'https://www.google.com',
        'github': 'https://github.com'
    }
    url = mapping.get(site.lower(), f"https://{site}")
    webbrowser.open(url)
    if speak_func: speak_func(f"Opening {site}")
    return f"open:{site}"
