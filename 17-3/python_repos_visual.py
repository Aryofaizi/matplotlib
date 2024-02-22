import requests
from plotly.graph_objs import Bar
from plotly import offline

def api_call():
    """A method to make a call to the specified api and
    returns the response as a dict"""
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}

    response = requests.get(url, headers=headers)
    return response

def extract_info(res):
    dicts = res.json()
    """Extracts the information from the response dict."""
    stars, names, labels = [], [], []
    for dict in dicts["items"]:
        stars.append(dict["stargazers_count"])
        name = f"<a href='{dict['html_url']}'>{dict['name']}</a>"
        names.append(name)
        owner = dict["owner"]["login"]
        labels.append(f"{owner}<br />{dict['description']}")
    return {
        "names": names,
        "stars": stars,
        "labels": labels,
        "items": dicts["items"],
        }

def set_data(info):
    """Set the data to visualize."""
    names = info["names"]
    stars = info["stars"]
    labels = info["labels"]
    
    data = [{
        "type": "bar",
        "x": names,
        "y": stars,
        "marker": {
            "color": "rgb(60, 100, 150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
        },
        "opacity": 0.6,
        "hovertext":labels,
    }]
    return data
def set_layout():
    """Define a layout for the chart."""
    chart_layout = {
        "title": "most-starred python projects on github",
        "titlefont": {"size":28},
        "xaxis": {
            "title": "repository",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
                },
        
        "yaxis": {
            "title": "stars",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
                },
    }
    return chart_layout
    
def visualize_data(data, layout):
    """Make the visualization based on the data."""
    fig = {"data": data, "layout": layout}
    offline.plot(fig, filename="repos.html")
    
    
if __name__ == "__main__":
    res = api_call()
    dicts = extract_info(res)
    data = set_data(dicts)
    layout = set_layout()
    visualize_data(data, layout)