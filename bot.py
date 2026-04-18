import requests
import json
import os

def auto_process():
    try:
        # ၁။ Secrets ယူခြင်း
        BID = os.environ.get('BLOG_ID')
        AKEY = os.environ.get('BLOGGER_API_KEY')

        # ၂။ PDF Link နှင့် JSON Data
        pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"
        data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (Bot Test)", "href": pdf_url}]}
        json_body = json.dumps(data, ensure_ascii=False)

        # ၃။ Blogger API URL (စာကြောင်းတစ်ခုတည်း အပြည့်အစုံ ရေးထားပါသည်)
        # ဤနေရာတွင် *** တွေ ကပ်မပါအောင် String formatting သေချာလုပ်ထားပါသည်
        final_url = "https://googleapis.com" % BID
        
        payload = {
            "kind": "blogger#post",
            "title": "2026",
            "content": f"<pre>{json_body}</pre>"
        }
        
        # ၄။ တိုက်ရိုက် ပို့လွှတ်ခြင်း
        r = requests.post(final_url, params={'key': AKEY}, json=payload, timeout=30)
        
        if r.status_code == 200:
            print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
        else:
            print(f"Error Code: {r.status_code}")
            print(f"Message: {r.text}")

    except Exception as e:
        print(f"Bot Error: {str(e)}")

if __name__ == "__main__":
    auto_process()
