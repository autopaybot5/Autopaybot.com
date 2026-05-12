import requests
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

# Use current date as unique identifier
today = datetime.now().strftime("%Y-%m-%d")
day_of_year = datetime.now().timetuple().tm_yday
topic_index = day_of_year % len(topics)
selected = topics[topic_index]

# Generate unique filename with date
filename_base = selected['topic'].lower()
filename_base = re.sub(r'[^a-z0-9\s-]', '', filename_base)
filename_base = re.sub(r'\s+', '-', filename_base).strip('-')
filename = f"blog-{filename_base}.html"

# Skip if already exists
if os.path.exists(filename):
    print(f"Already exists: {filename} — skipping, picking next topic")
    topic_index = (topic_index + 1) % len(topics)
    selected = topics[topic_index]
    filename_base = selected['topic'].lower()
    filename_base = re.sub(r'[^a-z0-9\s-]', '', filename_base)
    filename_base = re.sub(r'\s+', '-', filename_base).strip('-')
    filename = f"blog-{filename_base}.html"
print(f"Topic: {selected['topic']}")
print(f"Filename: {filename}")

headers = {
  "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
  "Content-Type": "application/json"
}

data = {
  "model": "llama-3.3-70b-versatile",
  "messages": [
    {
      "role": "system",
      "content": "You are an expert blog writer for autopaybot.com. Write complete SEO blog posts in clean HTML only. No markdown. No explanation. Only valid HTML output starting with <!DOCTYPE html>."
    },
    {
      "role": "user",
      "content": f"""Write a 1000 word SEO blog post for autopaybot.com.
Topic: {selected['topic']}
Keyword: {selected['keyword']}

Output ONLY complete valid HTML starting with <!DOCTYPE html> — nothing else before or after.

Use this exact structure:

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{selected['topic']} | AutoPayBot</title>
<meta name="description" content="Learn {selected['keyword']} with this free step-by-step guide from AutoPayBot.">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#050508;color:#e2e2f0;font-family:'DM Sans',sans-serif;font-size:16px;line-height:1.7;}}
nav{{position:fixed;top:0;left:0;right:0;height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;background:rgba(5,5,8,0.95);border-bottom:1px solid #1a1a28;z-index:100;}}
.logo{{font-family:'Bebas Neue',sans-serif;font-size:22px;color:white;text-decoration:none;letter-spacing:0.08em;}}
.logo span{{color:#a855f7;}}
.back{{font-size:13px;color:#6b6b8a;text-decoration:none;}}
.back:hover{{color:#e2e2f0;}}
.wrap{{max-width:740px;margin:0 auto;padding:100px 24px 80px;}}
.cat{{font-family:monospace;font-size:11px;color:#a855f7;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:16px;}}
h1{{font-family:'Bebas Neue',sans-serif;font-size:clamp(36px,6vw,52px);color:white;line-height:1.05;margin-bottom:20px;}}
.meta{{font-size:13px;color:#6b6b8a;margin-bottom:32px;padding-bottom:24px;border-bottom:1px solid #1a1a28;}}
h2{{font-family:'Bebas Neue',sans-serif;font-size:28px;color:white;margin:40px 0 14px;}}
p{{color:#c0c0d8;margin-bottom:18px;font-size:16px;}}
ul,ol{{padding-left:24px;margin-bottom:18px;}}
li{{color:#c0c0d8;margin-bottom:10px;line-height:1.7;}}
strong{{color:white;}}
a{{color:#a855f7;text-decoration:none;border-bottom:1px solid rgba(168,85,247,0.3);}}
.callout{{background:rgba(124,58,237,0.08);border-left:3px solid #7c3aed;padding:20px 24px;border-radius:0 8px 8px 0;margin:28px 0;}}
.callout p{{margin:0;}}
.cta{{background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.3);border-radius:12px;padding:32px;text-align:center;margin-top:48px;}}
.cta h3{{font-family:'Bebas Neue',sans-serif;font-size:28px;color:white;margin-bottom:10px;}}
.cta p{{color:#6b6b8a;margin-bottom:18px;}}
.btn{{display:inline-block;background:#7c3aed;color:white;padding:12px 28px;border-radius:8px;font-size:15px;font-weight:600;text-decoration:none;}}
footer{{text-align:center;padding:40px 24px;color:#6b6b8a;font-size:13px;border-top:1px solid #1a1a28;margin-top:60px;}}
</style>
</head>
<body>
<nav>
<a class="logo" href="index.html">Auto<span>Pay</span>Bot</a>
<a class="back" href="index.html">← Back to Home</a>
</nav>
<div class="wrap">
<div class="cat">Tutorial · Payment Automation</div>
<h1>[Write compelling H1 title about {selected['topic']}]</h1>
<div class="meta">⏱ 8 min read · Free tools only · Updated 2025</div>
[Write 150 word introduction with {selected['keyword']} in first sentence]
<div class="callout"><p>⚡ <strong>Quick Summary:</strong> [2 sentence summary of what reader will learn]</p></div>
<h2>WHY THIS MATTERS</h2>
[Write 2 detailed paragraphs about why this problem matters for freelancers and small businesses]
<h2>BEST FREE TOOLS</h2>
[Write about 3 specific free tools relevant to {selected['topic']} — name, what it does, why use it]
<h2>STEP BY STEP GUIDE</h2>
[Write numbered list with 6 detailed actionable steps]
<h2>FREQUENTLY ASKED QUESTIONS</h2>
<p><strong>Q: [Relevant question 1 about {selected['keyword']}]</strong></p>
<p>[Detailed answer in 2-3 sentences]</p>
<p><strong>Q: [Relevant question 2]</strong></p>
<p>[Detailed answer]</p>
<p><strong>Q: [Relevant question 3]</strong></p>
<p>[Detailed answer]</p>
<h2>CONCLUSION</h2>
[Write conclusion paragraph recommending autopaybot.com resources]
<div class="cta"><h3>GET THE FREE CHECKLIST</h3><p>27 steps to automate your payments completely — free download.</p><a class="btn" href="index.html#newsletter">Download Free →</a></div>
</div>
<footer>© 2025 AutoPayBot.com · <a href="index.html">Home</a> · All guides are free</footer>
</body>
</html>"""
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

if response.status_code != 200:
  print(f"API Error: {response.text}")
  exit(1)

result = response.json()
html_content = result['choices'][0]['message']['content']

# Clean markdown if present
if '```html' in html_content:
  html_content = html_content.split('```html')[1].split('```')[0].strip()
elif '```' in html_content:
  html_content = html_content.split('```')[1].split('```')[0].strip()

# Fix logo if AI wrote it wrong
html_content = html_content.replace(
  'AutoPayBot Logo',
  'Auto<span>Pay</span>Bot'
)

# Save file
with open(filename, 'w', encoding='utf-8') as f:
  f.write(html_content)

print(f"Saved: {filename}")

# Update index.html with new blog card
try:
  with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

  new_card = f'''
    <a href="{filename}" class="blog-card fade-up">
      <div class="blog-thumb thumb-1">💳</div>
      <div class="blog-body">
        <div class="blog-cat">Tutorial</div>
        <div class="blog-title">{selected['topic']}</div>
        <div class="blog-meta">8 min read · Payment Automation</div>
        <span class="blog-arrow">Read Guide →</span>
      </div>
    </a>'''

  # Try multiple replace patterns
replaced = False
for pattern in [
    '<a href="#" class="blog-card fade-up" onclick="showModal(event)">',
    'onclick="showModal(event)">',
    '<!-- NEW BLOG CARDS HERE -->',
]:
    if pattern in index_content:
        index_content = index_content.replace(pattern, new_card + '\n    ' + pattern, 1)
        replaced = True
        break

if not replaced:
    print("Pattern not found in index.html — card not added")
  with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

  print("Homepage updated!")
except Exception as e:
  print(f"Homepage update skipped: {e}")
