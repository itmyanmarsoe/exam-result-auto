import requests
import json
import os

# GitHub Secrets ကနေ Data ယူမယ်
BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')
TARGET_URL = "https://myanmarexam.org"

def auto_process():
    try:
        # ၁။ Website မှ Data ကို စစ်ဆေးခြင်း
        # မှတ်ချက် - Website တည်ဆောက်ပုံပေါ်မူတည်ပြီး ဤနေရာတွင် Scraper logic အနည်းငယ်ပြင်ရပါမည်
        response = requests.get(TARGET_URL)
        
        if response.status_code == 200:
            # ၂။ Project format အတိုင်း JSON ပြောင်းလဲခြင်း
            result_data = {
                "years": [
                    {
                        "name": "Grade 12 အောင်စာရင်း ၂၀၂၆",
                        "href": "https://github.com/itmyanmarsoe/exam-result-auto/blob/main/result.pdf"
                    }
                ]
            }
            json_content = json.dumps(result_data, ensure_ascii=False)

            # ၃။ Blogger API v3 ဖြင့် Post တင်ခြင်း
            post_url = f"https://googleapis.com{BLOG_ID}/posts/"
            payload = {
                "kind": "blogger#post",
                "title": "2026", # App က သိမည့် ခေါင်းစဉ်
                "content": json_content
            }
            
            params = {'key': API_KEY}
            r = requests.post(post_url, params=params, json=payload)
            
            if r.status_code == 200:
                print("စက္ကန့်ပိုင်းအတွင်း အောင်မြင်စွာ Post တင်ပြီးပါပြီ။")
            else:
                print("Error:", r.text)
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    auto_process()

