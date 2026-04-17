import requests
import json
import os

# GitHub Secrets မှ BLOG_ID နှင့် API_KEY ကို အလိုအလျောက် ယူပါမည်
BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_process():
    try:
        # ၁။ PDF တည်နေရာ (လူကြီးမင်း ပြောသလို လုံးဝအမှန်ဖြစ်သည်)
        raw_pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"

        # ၂။ JSON Data ပုံစံအမှန်
        result_data = {
            "years": [
                {
                    "name": "၂၀၂၆ အောင်စာရင်း (Bot စမ်းသပ်မှု)",
                    "href": raw_pdf_url
                }
            ]
        }
        json_content = json.dumps(result_data, ensure_ascii=False)

        # ၃။ Blogger API v3 လိပ်စာအမှန် (Blogger က လက်ခံရန် ဤပုံစံအတိုင်း အတိအကျ လိုအပ်ပါသည်)
        post_url = "https://googleapis.com" + str(BLOG_ID) + "/posts/"
        
        # Post တင်မည့် အချက်အလက်များ
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": "<pre>" + json_content + "</pre>"
        }
        
        # Blogger API ဆီသို့ ပို့လွှတ်ခြင်း
        r = requests.post(post_url, params={'key': API_KEY}, json=payload)
        
        if r.status_code == 200:
            print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
        else:
            # အကယ်၍ မရခဲ့ပါက အကြောင်းရင်းကို ဤနေရာတွင် ဖော်ပြပေးပါမည်
            print("Error Code: " + str(r.status_code))
            print("Message: " + r.text)

    except Exception as e:
        print("Bot Error: " + str(e))

if __name__ == "__main__":
    auto_process()
