import requests, json
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:java&sort=stars"

res = requests.get(url)

dicts = res.json()

names, stars = [], []
for dict in dicts["items"][:30]:
    stars.append(int(dict["stargazers_count"]))
    names.append(f"<a href='{dict['html_url']}'>{dict['name']}</a>")
    
data = [{
    "type": "bar",
    "x": names,
    "y": stars,
    "hoverlabel": {
        "bgcolor": "black"
    }
}]

chart_layout = {
    "title": "popular projects in java",
    "xaxis": {"title": "repos name"},
    "yaxis": {"title": "stars"},
}

fig = {"data": data, "layout":chart_layout}
offline.plot(fig, filename="java_repos.html")

