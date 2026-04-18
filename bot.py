import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import os

def send_to_blogger():
    try:
        # ၁။ အချက်အလက်များ ပြင်ဆင်ခြင်း
        gmail_user = "soe41959@gmail.com" 
        gmail_password = os.environ.get('GMAIL_PASSWORD')
        blogger_email = "soe41959.exam2026@blogger.com" 
        
        # ၂။ JSON Data (Project Format အတိုင်း)
        raw_pdf_url = "https://raw.githubusercontent.com/kaungkhantjc/exam/refs/heads/master/2025/SHN-082.pdf"
        result_data = {
            "years": [
                {
                    "name": "Grade 12 အောင်စာရင်း ၂၀၂၆",
                    "href": raw_pdf_url
                }
            ]
        }
        json_content = json.dumps(result_data, ensure_ascii=False)

        # ၃။ Email စာသား ပြင်ဆင်ခြင်း
        # Blogger က JSON စာသားကို အမှန်အတိုင်း သိစေရန် <pre> tag ခံရပါမည်
        msg_body = f"<html><body><pre>{json_content}</pre></body></html>"
        msg = MIMEText(msg_body, 'html', 'utf-8')
        
        # ၄။ ပို့စ်ခေါင်းစဉ် (Blogger ပို့စ်ခေါင်းစဉ် ဖြစ်လာပါမည်)
        msg['Subject'] = Header("2026", 'utf-8')
        msg['From'] = gmail_user
        msg['To'] = blogger_email

        # ၅။ Gmail Server မှတစ်ဆင့် ပို့လွှတ်ခြင်း
        server = smtplib.SMTP_SSL('://gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        
        print("အောင်မြင်စွာ ပို့ပြီးပါပြီ။ ခဏနေရင် Blog မှာ ပို့စ်အသစ် ရောက်လာပါလိမ့်မယ်ရှင်။")

    except Exception as e:
        print(f"Error occur: {str(e)}")

if __name__ == "__main__":
    send_to_blogger()
