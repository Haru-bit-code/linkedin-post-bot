from idea_generator import generate_idea
from notifier import send_message
from datetime import date
import config


start = date.fromisoformat(config.START_DATE)
today = date.today()
day = (today - start).days + 1

def run():
    idea = generate_idea(day)
    send_whatsapp(idea)



if __name__ == "__main__":
    run()