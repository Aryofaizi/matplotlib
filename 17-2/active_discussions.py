import requests
from operator import itemgetter
from plotly import offline

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

res = requests.get(url)
print(res.status_code)

# process information about each submission.
submission_ids = res.json()
submission_dicts = []
comments , labels = [], []
for submission_id in submission_ids[:10]:
    try:
        # make a separate api call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        response = requests.get(url)
        print(f"{submission_id}, status:{response.status_code}")
        data = response.json()
        
        submission_dict = {
        'title': data['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': data['descendants'],
    }
        submission_dicts.append(submission_dict)
    except:
        print("request failed")
        
        
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# generate list for plotting 
for item in submission_dicts:
    comments.append(item["comments"])
    labels.append(f"<a href='{item['hn_link']}'>{item['title']}</a>",)

# make bar 

data = [{
    "type" : "bar",
    "x": labels,
    "y":  comments,
}]

layout = {
    "title": "active discussions",
    "xaxis": {"title": "author"},
    "yaxis": {"title": "stars"},
}

fig = {"data":data, "layout":layout}
offline.plot(fig, filename="discussions.html")