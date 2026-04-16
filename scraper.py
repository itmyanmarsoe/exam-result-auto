import requests
import json

# Myo ရဲ့ အချက်အလက်များ
API_KEY = "AIzaSyCm3yKZ0IHCaL-DxDA0hQsArcBFiBPHNU8"
BLOG_ID = "4703947063207207857"

def post_to_blogger(content_json):
    url = f"https://googleapis.com{BLOG_ID}/posts?key={API_KEY}"
    
    # JSON ကို စာသားအဖြစ်ပြောင်းပြီး Content ထဲထည့်ခြင်း
    post_data = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": "2026", # Myo ရဲ့ App က ဒီ Title ကို ရှာမှာပါ
        "content": json.dumps(content_json, ensure_ascii=False)
    }
    
    response = requests.post(url, json=post_data)
    if response.status_code == 200:
        print("Blogger မှာ Post တင်ခြင်း အောင်မြင်ပါသည်ရှင်!")
    else:
        print("Error တက်နေပါသည်:", response.text)

# စမ်းသပ်ရန် Data (နမူနာ)
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

# စက်ရုပ်ကို စတင်ခိုင်းစေခြင်း
post_to_blogger(sample_data)
