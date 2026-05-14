from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)

def write_post(idea, day):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": """You are writing LinkedIn posts on behalf of a developer 
doing a daily project challenge. They have a Physics MSc 
background and are transitioning into AI and data science. 
Write in first person. Tone must be casual, honest, and 
conversational. Never sound corporate or like marketing."""},

{"role": "user", "content": f"""Day {day} of my daily project challenge.

Write a short LinkedIn post about this project idea: {idea}

Keep it:
- start with "Day {day} of my project challenge"
- casual and natural sounding
- written in first person
- short and readable
- not AI sounding


Include:
- a hook as the first line
- 2-3 short paragraphs
- end with a question or takeaway
- relevant hashtags at the end
- Start with a strong professional hook
- Clearly explain the main idea or experience
- Include key insights, lessons, or outcomes
- Sound natural, confident, and human
- Avoid sounding overly robotic or motivational
- Keep paragraphs short and readable
- End with a thoughtful closing or question for engagement

Tone:

- Professional
- Clear
- Modern
- Slightly conversational
- Suitable for LinkedIn audience

Structure:

- Hook
- Context / Problem
- What was done / learned
- Key takeaway
- Closing line or engagement question

details to include:list out this

- Tools used: [TOOLS]
- Technologies: [TECH]
- Results achieved: [RESULTS]
- Personal learning: [LEARNING]

Length:

- Around 180 words"""}
        ]
    )
    return response.choices[0].message.content