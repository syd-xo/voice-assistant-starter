
from datetime import datetime
from zoneinfo import ZoneInfo
import webbrowser

def respond(user_text: str) -> str:
    text = user_text.lower().strip()

    if "time" in text:
        now = datetime.now(ZoneInfo("Africa/Nairobi"))
        return f"The time is {now.strftime('%I:%M %p')}."
    if "date" in text or "day" in text:
        today = datetime.now(ZoneInfo("Africa/Nairobi"))
        return f"Today is {today.strftime('%A, %B %d, %Y')}."
    if text.startswith("open "):
        site = text.split("open ", 1)[1].strip()
        if not site:
            return "Which website should I open?"
        if not site.startswith("http"):
            site = "https://" + site
        webbrowser.open(site)
        return f"Opening {site}."
    # Fallback: echo
    return f"You said: {user_text}"
