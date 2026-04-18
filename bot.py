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
        raw_pdf_url = "https://raw.githubusercontent.com/kaungkhantjc/exam/refs/heads/master/2025/SHN-082.pdf"
        result_data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (Email စနစ်)", "href": raw_pdf_url}]}
        json_content = json.dumps(result_data, ensure_ascii=False)

        # ၃။ Email ပြင်ဆင်ခြင်း
        msg_body = f"<html><body><pre>{json_content}</pre></body></html>"
        msg = MIMEText(msg_body, 'html', 'utf-8')
        msg['Subject'] = Header("2026", 'utf-8')
        msg['From'] = gmail_user
        msg['To'] = blogger_email

        # ၄။ Gmail Server သို့ ပိုမိုခိုင်မာသော နည်းလမ်းဖြင့် ချိတ်ဆက်ခြင်း
        server = smtplib.SMTP('://gmail.com', 587)
        server.starttls() # TLS လုံခြုံရေးစနစ် သုံးခြင်း
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        
        print("အောင်မြင်စွာ ပို့ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")

    except Exception as e:
        print(f"Error occur: {str(e)}")

if __name__ == "__main__":
    send_to_blogger()
