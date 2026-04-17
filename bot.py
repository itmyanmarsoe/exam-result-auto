import requests
import json
import os

# GitHub Secrets ထဲက Key တွေကို လုံလုံခြုံခြုံ ယူသုံးမယ်
BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_process():
    try:
        # ၁။ PDF Raw Link
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

        # ၃။ Blogger API v3 URL (လိပ်စာအမှန် ပြင်ဆင်ပြီးသား)
        post_url = f"https://googleapis.com{BLOG_ID}/posts/"
        
        # Post တင်မည့် အချက်အလက်များ
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": f"<pre>{json_content}</pre>"
        }
        
        # API Key ဖြင့် Blogger သို့ ပို့လွှတ်ခြင်း
        # မျက်တောင်ဖွင့်ပိတ် Error မတက်အောင် API_KEY ကို တိုက်ရိုက်သုံးထားပါတယ်
        r = requests.post(post_url, params={'key': API_KEY}, json=payload)
        
        if r.status_code == 200:
            print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
        else:
            print(f"Error Code: {r.status_code}")
            print(f"Message: {r.text}")

    except Exception as e:
        print(f"Bot Error: {str(e)}")

if __name__ == "__main__":
    auto_process()
