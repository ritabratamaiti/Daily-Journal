# import datetime
from datetime import datetime
import json

# temp = {
#     "latest": 1,
#     "posts": [
#         {"1": {
#             "title": "Coded my personal daily journal",
#             # todays date
#             "date": datetime.now().strftime("%d/%m/%Y"),
#             "display_date": datetime.now().strftime("%b %d, %Y"),
#         }}
#     ]
# }

# {
#     "title" : "Coded my personal daily journal",
#     "display_date": "Dec 03, 2022",
#     "textHTML": "<p>Hey there! Today I started my personal journal to help me stay on track and hold myself accountable. I'm excited to document my progress and reflect on my goals. This is the start of a new journey for me, and I'm determined to make it a successful one.I'll be sharing my thoughts, experiences, and challenges along the way.</p><p>In today's entry, I want to reflect on my goals and what I'm working towards. Recently been focusing on developing productivity and creative applications that leverage the latest advances in large language models, as I feel that this specific niche has quite a lot of potential.</p><p>In addition to my coding goals, I'm also working on becoming more disciplined and organized in my daily life. I want to make sure that I'm using my time effectively and staying on top of my tasks. I've been trying to establish a daily routine and stick to it, and so far it's been going well.</p><p>Overall, I'm feeling motivated and excited about the future. I'm looking forward to continuing to work towards my goals and seeing what I can accomplish. Here's to a productive and fulfilling journey ahead!</p>"
# }

# # save the data to a json file
# with open("index.json", "w") as f:
#     json.dump(temp, f, indent=4)


# new_post = {
#     "title" : "title..",
#     "textHTML": "HTML Text..",
# }


def save_post(title, textHTML):
    # load the json file
    with open("index.json", "r") as f:
        data = json.load(f)

    # get the latest post number
    latest = data["latest"]
    # increment by 1
    latest += 1
    data["latest"] = latest
    # add a new entry to the posts list; with the latest post number as the key
    new_post = {
        "title": title,
        "date": datetime.now().strftime("%d/%m/%Y"),
        "display_date": datetime.now().strftime("%b %d, %Y"),
    }

    data["posts"].append({latest: new_post})

    post_data = {
        "title": title,
        "textHTML": textHTML,
        "display_date": datetime.now().strftime("%a, %b %d, %Y"),
    }

    # save data to the index.json file
    with open("index.json", "w") as f:
        json.dump(data, f, indent=4)

    # save the post data to a json file as "latest.json"
    with open(f"{latest}.json", "w") as f:
        json.dump(post_data, f, indent=4)

title = "Some updates on Serenebase and my generative art project"
textHTML = """<p>Today, I spent the day focused on further developing <a href="https://www.serenebase.com/">Serenebase</a>, my online platform for mental health resources. I added several new blogs to the site, providing even more information and support for those looking to improve their mental health.</p>
<p>In addition, I came up with a comprehensive content marketing plan for <a href="https://viberooms.serenebase.com/">viberooms</a>, a new feature on Serenebase that allows users to connect with others in a virtual support group. I am excited to start implementing this plan and helping even more individuals find the support they need.</p>
<p>I also made the decision to reach out to mental health startup founders this week to add their resources to the directory on Serenebase. I believe that by providing a wide range of options, we can help even more people find the support and tools they need to improve their mental health.</p>
<p>Lastly, after a brief hiatus, I am excited to return to my generative art project. I am determined to continue working on this project and improving my overall productivity in order to make a positive impact on the mental health community.</p>
<p>Overall, it was a productive and fulfilling day, and I am looking forward to continuing to grow and improve Serenebase in the coming days and weeks.</p>"""

def remove_newlines(text):
    return text.replace("\r", "").replace("\n", "")

save_post(title, remove_newlines(textHTML))