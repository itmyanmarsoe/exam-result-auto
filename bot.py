import requests
import json
import os
def auto_process():
try:
# ၁။ Secrets ယူခြင်း
BID = os.environ.get('BLOG_ID')
AKEY = os.environ.get('BLOGGER_API_KEY')
# ၂။ PDF Link နှင့် JSON Data
pdf_url = "githubusercontent.com"
data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (Final Test)", "href": pdf_url}]}
json_body = json.dumps(data, ensure_ascii=False)
# ၃။ လိပ်စာတည်ဆောက်ပုံ (f-string စနစ်ကို သုံးထား၍ အမှားကင်းပါသည်)
final_url = "googleapis.com" + str(BID) + "/posts"
payload = {
"kind": "blogger#post",
"title": "2026",
"content": "" + json_body + ""
}
# ၄။ တိုက်ရိုက် ပို့လွှတ်ခြင်း
r = requests.post(final_url, params={'key': AKEY}, json=payload, timeout=30)
if r.status_code == 200:
print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
else:
print("Error Code: " + str(r.status_code))
print("Message: " + r.text)
except Exception as e:
print("Bot Error: " + str(e))
if name == "main":
auto_process()
