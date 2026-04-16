import requests
import json
import os

# GitHub Secrets ကနေ Key တွေကို ယူခြင်း
BLOG_ID = os.environ.get('BLOG_ID')
API_KEY = os.environ.get('BLOGGER_API_KEY')

def auto_post():
    print("Automation စတင်နေပါပြီ...")
    
    # ၁။ Website ကနေ Data ယူသည့်နေရာ (အခုလောလောဆယ် စမ်းသပ်ရန် Data ထည့်ထားပါသည်)
    # ၂၀၂၆ ဇွန်လတွင် ဤနေရာ၌ myanmarexam.org မှ scraping logic ထည့်ပါမည်
    new_exam_data = {
        "years": [
            {
                "name": "စမ်းသပ်အောင်စာရင်း (Grade 12) - ၂၀၂၆",
                "href": "https://githubusercontent.com"
            }
        ]
    }
    
    json_content = json.dumps(new_exam_data, ensure_ascii=False)

    # ၂။ Blogger API သို့ Post တင်ရန် ပြင်ဆင်ခြင်း
    post_url = f"https://googleapis.com{BLOG_ID}/posts/"
    
    post_body = {
        "kind": "blogger#post",
        "title": "2026", # App က ရှာမည့် ခေါင်းစဉ်
        "content": json_content
    }

    params = {'key': API_KEY}
    
    try:
        # API သို့ Post တင်ခြင်း
        r = requests.post(post_url, params=params, json=post_body)
        if r.status_code == 200:
            print("အောင်မြင်စွာ Post တင်ပြီးပါပြီ။ Blogger တွင် စစ်ကြည့်နိုင်ပါပြီ။")
        else:
            print(f"အမှားဖြစ်သွားပါသည်: {r.status_code}")
            print(r.text)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    auto_post()
