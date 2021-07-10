from datetime import datetime

def sample_responses(input_text):
    user_text = str(input_text).lower()

    if user_text in ("hello","hey","hi","sup"):
        return "hey! How's it going?"

    if user_text in ("who are you","who are you?"):
        return "I am a bot"

    if user_text in("time", "time?"):
        now= datetime.now()
        date_time=now.strftime("%d/%m/%y, %H:%M: %S")

        return str(date_time)
    else:
        return "I don't understand you"
