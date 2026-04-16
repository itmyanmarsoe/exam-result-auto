import smtplib
from email.mime.text import MIMEText
import json

# ၁။ Myo ရဲ့ အချက်အလက်များ (ဤနေရာတွင် အမှန်အတိုင်း ပြင်ပေးပါ)
SENDER_EMAIL = "maungsoe1988@gmail.com" # Myo ရဲ့ Gmail
APP_PASSWORD = " yunl nnvk rwil" # အခုရတဲ့ စာလုံး ၁၆ လုံး password
# Blogger Settings > Email > 'Post using email' တွင် သတ်မှတ်ထားသော email ကို ထည့်ပါ
BLOGGER_EMAIL = "poemstoremyan.xxxx@blogger.com" 

def send_to_blogger(content_json):
    # Post Title ကို "2026" ဟု ပေးခြင်း (App က ဤ Title ကို ရှာပါသည်)
    subject = "2026" 
    body = json.dumps(content_json, ensure_ascii=False)
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = soe41959.exam2026@blogger.com

    try:
        # Gmail SMTP Server မှတစ်ဆင့် ပို့ခြင်း
        with smtplib.SMTP_SSL('://gmail.com', 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, BLOGGER_EMAIL, msg.as_string())
        print("Blogger ဆီသို့ အောင်စာရင်း လှမ်းပို့လိုက်ပါပြီရှင်!")
    except Exception as e:
        print("Error တက်နေပါသည်:", str(e))

# စမ်းသပ်ရန် အောင်စာရင်း Data (App Format အတိုင်း)
sample_data = {
    "year": 2026,
    "years": [
        {
            "no": "၁။",
            "name": "ရန်ကုန်တိုင်း (Automation)",
            "cities": [{"no": "က", "name": "နမူနာမြို့နယ်", "href": "https://google.com"}]
        }
    ]
}

if __name__ == "__main__":
    send_to_blogger(sample_data)
