# Affiliate links dictionary
AFFILIATE_LINKS = {
    "make.com": "https://www.make.com/?via=autopaybot",
    "zapier": "https://zapier.com/?via=autopaybot", 
    "canva": "https://www.canva.com/join/autopaybot",
    "hostinger": "https://hostinger.in/?REFERRALCODE=autopaybot",
    "freshbooks": "https://www.freshbooks.com/?ref=autopaybot",
    "lemonsqueezy": "https://www.lemonsqueezy.com/?aff=autopaybot",
    "stripe": "https://stripe.com",
    "paypal": "https://paypal.com",
    "gocardless": "https://gocardless.com",
    "notion": "https://notion.so/?ref=autopaybot",
    "airtable": "https://airtable.com/?ref=autopaybot",
}

def inject_affiliate_links(html_content):
    import re
    for tool, link in AFFILIATE_LINKS.items():
        # Replace first mention of each tool with affiliate link
        pattern = rf'(?<!["\'/])({re.escape(tool)})(?!["\'/])'
        replacement = f'<a href="{link}" target="_blank" rel="noopener">{tool}</a>'
        html_content = re.sub(pattern, replacement, html_content, count=1, flags=re.IGNORECASE)
    return html_content
