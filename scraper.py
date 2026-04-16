import requests
import json

# Myo ရဲ့ အချက်အလက်များ (ဘေးက space တွေကို strip() နဲ့ ဖြုတ်ပေးထားပါတယ်)
API_KEY = "AIzaSyCm3yKZ0IHCaL-DxDA0hQsArcBFiBPHNU8".strip()
BLOG_ID = "4703947063207207857".strip()

def post_to_blogger(content_json):
    # လိပ်စာကို အသေချာဆုံးပုံစံ ပြောင်းလဲထားပါသည်
    url = "https://googleapis.com" + BLOG_ID + "/posts"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    post_data = {
        "kind": "blogger#post",
        "title": "2026",
        "content": json.dumps(content_json, ensure_ascii=False)
    }
    
    # API Key ကို parameter အနေနဲ့ သီးသန့်ပို့ခြင်း
    params = {"key": API_KEY}
    
    try:
        response = requests.post(url, params=params, json=post_data, headers=headers)
        if response.status_code == 200:
            print("အောင်မြင်စွာ Post တင်ပြီးပါပြီရှင်!")
        else:
            print("Error Code:", response.status_code)
            print("Error Detail:", response.text)
    except Exception as e:
        print("ချိတ်ဆက်မှု Error တက်နေပါသည်:", str(e))

# စမ်းသပ်ရန် Data
sample_data = {
    "year": 2026,
    "years": [
        {
            "no": "၁။",
            "name": "စမ်းသပ်ချက် (ရန်ကုန်)",
            "cities": [{"no": "က", "name": "နမူနာမြို့နယ်", "href": "https://google.com"}]
        }
    ]
}

if __name__ == "__main__":
    post_to_blogger(sample_data)
