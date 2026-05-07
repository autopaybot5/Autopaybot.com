import requests
import json
import os
import re
from datetime import datetime

topics = [
  {"topic": "How to Automate Invoice Collection Using a Free Bot", "keyword": "automate invoice bot free"},
  {"topic": "Best Payment Automation Tools for Freelancers 2025", "keyword": "payment automation freelancers"},
  {"topic": "Setting Up Automatic Payment Reminders No Code", "keyword": "automatic payment reminders free"},
  {"topic": "How to Stop Chasing Late Payments With Automation", "keyword": "stop late payments automation"},
  {"topic": "Make.com vs Zapier for Payment Automation", "keyword": "make.com vs zapier payments"},
  {"topic": "How to Build a WhatsApp Payment Reminder Bot", "keyword": "whatsapp payment reminder bot"},
  {"topic": "Stripe Automation 7 Workflows You Can Set Up Today", "keyword": "stripe automation workflows"},
  {"topic": "Free Invoice Automation Workflow Template", "keyword": "invoice automation template free"},
  {"topic": "AI Chatbots That Collect Payments Full Guide", "keyword": "AI chatbot collect payments"},
  {"topic": "GoCardless Review Best for Automated Bank Transfers", "keyword": "gocardless review automated"},
  {"topic": "How to Automate PayPal Invoices Using AI", "keyword": "automate paypal invoices AI"},
  {"topic": "Payment Automation for Agencies Save 10 Hours Week", "keyword": "payment automation agencies"},
  {"topic": "How to Create a Recurring Payment Bot Without Code", "keyword": "recurring payment bot no code"},
  {"topic": "Failed Payment Recovery How to Automate Dunning", "keyword": "automate dunning failed payments"},
  {"topic": "Best No Code Tools to Accept Payments Without Developer", "keyword": "no code accept payments"},
  {"topic": "How to Send Automated Payment Reminders for Free", "keyword": "automated payment reminders free"},
  {"topic": "Stripe vs Paddle vs LemonSqueezy Which Automates Best", "keyword": "stripe paddle lemonsqueezy compare"},
  {"topic": "How to Auto Generate Invoices From Google Forms", "keyword": "auto generate invoices google forms"},
  {"topic": "Payment Automation for SaaS Founders Full Guide", "keyword": "saas payment automation guide"},
  {"topic": "How Freelancers Are Using AI to Get Paid Faster", "keyword": "AI freelancers get paid faster"},
]

day_of_year = datetime.now().timetuple().tm_yday
topic_index = day_of_year % len(topics)
selected = topics[topic_index]

print(f"Topic: {selected['topic']}")

headers = {
  "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
  "Content-Type": "application/json"
}

data = {
  "model": "llama-3.3-70b-versatile",
  "messages": [
    {
      "role": "system",
      "content": "You are an expert blog writer for autopaybot.com. Write complete SEO blog posts in clean HTML only. No markdown. No explanation. Only valid HTML output."
    },
    {
      "role": "user",
      "content": f"""Write a 1000 word SEO blog post for autopaybot.com.
Topic: {selected['topic']}
Keyword: {selected['keyword']}

Output ONLY complete valid HTML starting with <!DOCTYPE html> — nothing else.

Include:
- Dark theme CSS styling (background #050508, text #e2e2f0, accent #a855f7)
- Nav bar with AutoPayBot logo linking to index.html
- H1 title
- Introduction with keyword in first sentence
- H2: WHY THIS MATTERS (2 paragraphs)
- H2: BEST FREE TOOLS (3 tools with descriptions)
- H2: STEP BY STEP GUIDE (numbered list 5-7 steps)
- H2: FAQ (3 questions with answers)
- Conclusion paragraph
- CTA box linking to index.html#newsletter
- Footer linking to index.html"""
    }
  ],
  "max_tokens": 3000,
  "temperature": 0.7
}

response = requests.post(
  "https://api.groq.com/openai/v1/chat/completions",
  headers=headers,
  json=data,
  timeout=60
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text[:500]}")

if response.status_code != 200:
  print("API Error — exiting")
  exit(1)

result = response.json()
html_content = result['choices'][0]['message']['content']

# Clean HTML — remove any markdown if present
if '```html' in html_content:
  html_content = html_content.split('```html')[1].split('```')[0]
elif '```' in html_content:
  html_content = html_content.split('```')[1].split('```')[0]

# Generate filename
filename = selected['topic'].lower()
filename = re.sub(r'[^a-z0-9\s-]', '', filename)
filename = re.sub(r'\s+', '-', filename).strip('-')
filename = f"blog-{filename}.html"

with open(filename, 'w', encoding='utf-8') as f:
  f.write(html_content)

print(f"Saved: {filename}")
