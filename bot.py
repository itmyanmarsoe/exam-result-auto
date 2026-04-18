import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import os
def send_to_blogger():
try:
# ၁။ အချက်အလက်များ
gmail_user = "soe41959@gmail.com"
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = "soe41959.exam2026@blogger.com"
# ၂။ JSON Data
raw_pdf_url = "githubusercontent.com"
result_data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (Email စနစ်)", "href": raw_pdf_url}]}
json_content = json.dumps(result_data, ensure_ascii=False)
# ၃။ Email ပြင်ဆင်ခြင်း
msg_body = f"{json_content}"
msg = MIMEText(msg_body, 'html', 'utf-8')
msg['Subject'] = Header("2026", 'utf-8')
msg['From'] = gmail_user
msg['To'] = blogger_email
# ၄။ Gmail Server လိပ်စာအမှန် (gmail.com ဟု အတိအကျ ဖြစ်ရပါမည်)
server = smtplib.SMTP('gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()
