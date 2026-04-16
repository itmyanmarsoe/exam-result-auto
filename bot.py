import requests
import json
import os

# GitHub Secrets မှ အချက်အလက်များကို ယူခြင်း
BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_process():
    try:
        # ၁။ PDF Raw Link
        raw_pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"

        # ၂။ JSON Data ပုံစံ
        result_data = {
            "years": [
                {
                    "name": "၂၀၂၆ အောင်စာရင်း (Bot စမ်းသပ်မှု)",
                    "href": raw_pdf_url
                }
            ]
        }
        json_content = json.dumps(result_data, ensure_ascii=False)

        # ၃။ Blogger API v3 လိပ်စာအပြည့်အစုံ (လူကြီးမင်း၏ Blog ID ကို အထဲမှာ တစ်ခါတည်း ထည့်ပေးထားပါသည်)
        # စာသားများကို အရှေ့အနောက် ညီအောင် ပြန်ညှိပေးထားပါသည်
        post_url = "https://www.googleapis.com/blogger/v3/blogs/" + "4703947063207207857" + "/posts/"
        
        # Post တင်မည့် အချက်အလက်များ
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": "<pre>" + json_content + "</pre>"
        }
        
        # API Key ဖြင့် Blogger သို့ ပို့လွှတ်ခြင်း
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
