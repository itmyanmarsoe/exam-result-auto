import requests
import json
import os

BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_process():
    try:
        # PDF Raw Link
        raw_pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"

        # JSON Data
        result_data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (Bot စမ်းသပ်မှု)", "href": raw_pdf_url}]}
        json_content = json.dumps(result_data, ensure_ascii=False)

        # Blogger API v3 URL (www. ပါရပါမည်၊ ကြယ်ပွင့်များ မပါရပါ)
        # API Key ကို URL ထဲမှာ တစ်ခါတည်း တွဲထည့်လိုက်တဲ့ နည်းလမ်းဖြစ်ပါတယ်
        post_url = f"https://googleapis.com{BLOG_ID}/posts?key={API_KEY}"

# ပြီးရင် အောက်က line ကို ဒီအတိုင်း ပြောင်းပါ
        r = requests.post(post_url, json=payload) 

        # Post တင်မည့် အချက်အလက်များ
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": "<pre>" + json_content + "</pre>"
        }
        
        # API ခေါ်ယူခြင်း
        r = requests.post(post_url, params={'key': API_KEY}, json=payload)
        
        if r.status_code == 200:
            print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
        else:
            print("Error Code: " + str(r.status_code))
            print("Message: " + r.text)

    except Exception as e:
        print("Bot Error: " + str(e))

if __name__ == "__main__":
    auto_process()
