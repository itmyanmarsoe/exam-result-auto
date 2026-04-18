import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import os

def send_to_blogger():
    try:
        gmail_user = "soe41959@gmail.com" 
        gmail_password = os.environ.get('GMAIL_PASSWORD')
        blogger_email = "soe41959.exam2026@blogger.com" 
        
        raw_pdf_url = "https://githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"
        result_data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (စမ်းသပ်ချက်)", "href": raw_pdf_url}]}
        json_content = json.dumps(result_data, ensure_ascii=False)

        msg_body = "<html><body><pre>" + json_content + "</pre></body></html>"
        msg = MIMEText(msg_body, 'html', 'utf-8')
        msg['Subject'] = Header("2026", 'utf-8')
        msg['From'] = gmail_user
        msg['To'] = blogger_email

        server = smtplib.SMTP('gmail.com', 587)
        server.starttls() 
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        
        print("အောင်မြင်စွာ ပို့ပြီးပါပြီ။")

    except Exception as e:
        print("Error occur: " + str(e))

if __name__ == "__main__":
    send_to_blogger()
