import requests
import json
import os

BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_process():
    try:
        # PDF Raw Link
        raw_pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"

        # JSON Data (Perfect Format)
        result_data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (Test)", "href": raw_pdf_url}]}
        json_content = json.dumps(result_data, ensure_ascii=False)

        # API URL (အမှန်က ဤအတိုင်း ဖြစ်ရပါမည်)
        post_url = f"https://googleapis.com{BLOG_ID}/posts/"
        
        # Post အချက်အလက်များ
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": f"<pre>{json_content}</pre>"
        }
        
        # API Key ဖြင့် တိုက်ရိုက်ပို့ခြင်း
        r = requests.post(post_url, params={'key': API_KEY}, json=payload)
        
        if r.status_code == 200:
            print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို ပြန်စစ်ကြည့်ပါရှင်။")
        else:
            # အကယ်၍ မရခဲ့ပါက ဤနေရာတွင် အမှားကို ဖော်ပြပေးပါမည်
            print(f"Error Code: {r.status_code}")
            print(f"Message: {r.text}")

    except Exception as e:
        print(f"Bot Error: {str(e)}")

if __name__ == "__main__":
    auto_process()
