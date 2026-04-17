import requests
import json
import os

# GitHub Secrets မှ အချက်အလက်များကို ယူခြင်း
BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_process():
    try:
        # ၁။ PDF Raw Link အပြည့်အစုံ
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

        # ၃။ Blogger API v3 URL (လိပ်စာကို ပုံသေစာသားအဖြစ် ပြင်ဆင်ပေးထားပါသည်)
        # ဤနေရာတွင် www. ပါဝင်အောင်နှင့် လိပ်စာ အဆုံးသတ် မှန်ကန်အောင် ပြင်ထားပါသည်
    #    post_url = "https://googleapis.com" + str(BLOG_ID) + "/posts"
    post_url  = "https://www.googleapis.com/blogger/v3/blogs/" +"4703947063207207857" + "/posts"
        # Post တင်မည့် အချက်အလက်များ
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": "<pre>" + json_content + "</pre>"
        }
        
        # API Key ဖြင့် Blogger သို့ ပို့လွှတ်ခြင်း
        # params ထဲတွင် API_KEY ကို လုံလုံခြုံခြုံ ထည့်သွင်းထားပါသည်
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
