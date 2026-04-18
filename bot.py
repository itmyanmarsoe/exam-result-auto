import requests
import json
import os
BID = os.environ.get('BLOG_ID')
AKEY = os.environ.get('BLOGGER_API_KEY')
pdf_url = "https://raw.githubusercontent.com/itmyanmarsoe/exam-result-auto/main/result.pdf"
data = {"years": [{"name": "၂၀၂၆ အောင်စာရင်း (စမ်းသပ်ချက်)", "href": pdf_url}]}
json_body = json.dumps(data, ensure_ascii=False)
final_url = "googleapis.com" + str(BID) + "/posts"
payload = {
"kind": "blogger#post",
"title": "2026",
"content": "" + json_body + ""
}
print("Blogger ဆီသို့ ပို့နေပါပြီ...")
r = requests.post(final_url, params={'key': AKEY}, json=payload, timeout=30)
if r.status_code == 200:
print("အောင်မြင်စွာ တင်ပြီးပါပြီ။ Blog ကို စစ်ကြည့်ပါရှင်။")
else:
print("Error Code: " + str(r.status_code))
print("Message: " + r.text)
