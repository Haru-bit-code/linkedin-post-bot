# 🤖 LinkedIn Post Bot

## What it does

LinkedIn Post Bot is an automated AI-powered system that runs 24/7 and delivers fresh AI/ML project ideas directly to Telegram every day.

The bot continuously generates unique project concepts, structured project briefs, and ready-to-post LinkedIn captions to help developers stay consistent with content creation, portfolio building, and public learning.

It is designed for:

* Developers building in public
* Students learning AI/ML
* Content creators sharing daily progress
* Anyone looking for portfolio-worthy project inspiration

---

## Why I built it

Coming up with good project ideas consistently is difficult.

Most developers either:

* run out of ideas,
* repeat common beginner projects,
* or struggle to write professional LinkedIn posts around their work.

I built this project to automate that process.

The goal was to create a system that:

* generates practical AI/ML project ideas,
* formats them into readable content,
* and sends them automatically every day without manual effort.

---

## Tech Stack

* Python
* Telegram Bot API
* Groq API
* Scheduler / Automation
* Environment Variables (`dotenv`)
* VPS / Cloud Deployment

---

## Project Structure

```bash
linkedin-post-bot/
│
├── main.py               # Main automation runner
├── idea_generator.py          # AI project idea generation
├── notifier.py    # Sends messages to Telegram
├── post_writer.py            # Prompt templates
├── scheduler.py          # Daily scheduling logic
├── .env                  # Environment variables
├── requirements.txt
└── README.md
```

---

## How to run locally

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd linkedin-post-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add environment variables

Create a `.env` file and add your credentials.

### 6. Run the bot

```bash
python main.py
```

---

## Environment Variables

```env
GROQ_API_KEY=your_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
START_DATE
```

---

## Deployment

This project can run continuously on:

* VPS servers
* Railway
* Render
* AWS EC2
* DigitalOcean
* Raspberry Pi

Recommended setup:

* Use a Linux VPS
* Run the bot with `screen`, `tmux`, or `systemd`
* Store secrets using environment variables

---

## What I learned

Through this project, I learned:

* How to automate AI workflows
* Prompt engineering for structured outputs
* Telegram bot integration
* Running long-term background Python services
* Scheduling recurring AI tasks
* Organizing scalable Python project structures
* Handling API-based automation systems

This project also improved my understanding of how AI tools can be combined into practical real-world automation systems.
