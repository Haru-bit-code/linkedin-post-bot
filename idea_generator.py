from groq import Groq
import config
import os

client = Groq(api_key=config.GROQ_API_KEY)

def generate_idea(day):
    
    if os.path.exists("project_used.txt"):
        with open("project_used.txt", "r") as f:
            project_used = f.read()
    else:
        project_used = "None yet"
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""
You are an AI/ML project idea generator.

Your task is to generate ONE unique, realistic, portfolio-worthy AI/ML project idea that is practical, beginner-to-intermediate friendly, and useful in real-world scenarios.

The idea should:
- Feel modern and relevant in today's AI industry
- Solve a real problem or improve an existing workflow
- Be possible to build with publicly available tools/APIs
- Be impressive enough for LinkedIn, GitHub, resumes, or internships
- Avoid generic beginner projects unless there is a creative twist
- Include a simple explanation of the project thinking process
- Be concise but valuable

The LinkedIn caption should:
- Sound natural and human
- Feel like a genuine build-in-public developer post
- Avoid cringe/motivational language
- Be short, professional, and engaging
- Include relevant hashtags

Return the response in this EXACT format only:

PROJECT BRIEF
─────────────
Project Name:
What it does:
Tech Stack:
How to think about it:
Where to start:

LINKEDIN CAPTION
────────────────
Day {day} |
[caption]

#hashtags

IMPORTANT RULES:
- Do NOT repeat or resemble these existing projects:
{project_used}

- Do NOT add extra sections
- Do NOT use markdown
- Do NOT explain outside the format
- Keep the project realistic and buildable
- Prefer AI agents, automation, data analysis, recommendation systems, computer vision, NLP, or productivity-based ideas"""

},
            
            
            
            { "role": "user", "content": f"""
You are an AI/ML project idea generator.

Your task is to generate ONE unique, realistic, portfolio-worthy AI/ML project idea that is practical, beginner-to-intermediate friendly, and useful in real-world scenarios.

The idea should:
- Feel modern and relevant in today's AI industry
- Solve a real problem or improve an existing workflow
- Be possible to build with publicly available tools/APIs
- Be impressive enough for LinkedIn, GitHub, resumes, or internships
- Avoid generic beginner projects unless there is a creative twist
- Include a simple explanation of the project thinking process
- Be concise but valuable

The LinkedIn caption should:
- Sound natural and human
- Feel like a genuine build-in-public developer post
- Avoid cringe/motivational language
- Be short, professional, and engaging
- Include relevant hashtags

Return the response in this EXACT format only:

PROJECT BRIEF
─────────────
Project Name:
What it does:
Tech Stack:
How to think about it:
Where to start:

LINKEDIN CAPTION
────────────────
Day {day} |
[caption]

#hashtags

IMPORTANT RULES:
- Do NOT repeat or resemble these existing projects:
{project_used}

- Do NOT add extra sections
- Do NOT use markdown
- Do NOT explain outside the format
- Keep the project realistic and buildable
- Prefer AI agents, automation, data analysis, recommendation systems, computer vision, NLP, or productivity-based ideas
"""
}
        ]
    )   
    
    result = response.choices[0].message.content
    
    with open("project_used.txt", "a") as f:
        title = result.split("\n")[0]
        f.write(f"{title}\n") 
    
    return result  


