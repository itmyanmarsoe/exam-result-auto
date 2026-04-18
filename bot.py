import requests
import json
import os

def auto_process():
    try:
        # ၁။ Secrets ထဲကနေ Key တွေကို ယူမယ်
        BLOG_ID = os.environ.get('BLOG_ID')
        API_KEY = os.environ.get('BLOGGER_API_KEY')

        # ၂။ PDF Link နှင့် JSON Data
        raw_pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"
        result_data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (စမ်းသပ်ချက်)", "href": raw_pdf_url}]}
        json_content = json.dumps(result_data, ensure_ascii=False)

        # ၃။ Blogger API URL (v3)
        post_url = f"https://googleapis.com{BLOG_ID}/posts/"
        
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": f"<pre>{json_content}</pre>"
        }
        
        # ၄။ တိုက်ရိုက် ပို့လွှတ်ခြင်း (၅ စက္ကန့်အတွင်း ပြီးပါသည်)
        r = requests.post(post_url, params={'key': API_KEY}, json=payload, timeout=20)
        
        if r.status_code == 200:
            print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
        else:
            print(f"Error Code: {r.status_code}")
            print(f"Message: {r.text}")

    except Exception as e:
        print(f"Bot Error: {str(e)}")

if __name__ == "__main__":
    auto_process()
