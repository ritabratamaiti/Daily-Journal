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

title = "A Mixed Day: Reflecting on Distractions and Moving Forward with My Goals"
textHTML = """<p>Today was a bit of a challenge as I wasn't able to work on my projects as much as I had hoped. I ended up getting occupied with other things, which really slowed down my productivity.</p>
<p>I am determined to improve my ability to avoid distractions and stay focused on my goals. While I made some progress in this area today, I know that I have a lot of work ahead of me. It can be frustrating at times, but I am committed to improving myself and achieving my goals.</p>
<p>As for my gameplan for this week, I plan to add the articles I wrote for <a href="https://serenebase.com/">Serenebase</a> to the website and work on a marketing plan for <a href="https://viberooms.serenebase.com/">Viberooms</a>. I am also excited to continue working on my generative AI project and writing an article to gauge interest. Additionally, I will be starting two GPT-3 based apps, even though they may not be successful.</p>
<p>Overall, it was a bit of a mixed day, but I am feeling optimistic and ready to tackle my projects this week. I am confident that with hard work and determination, I can make great progress and achieve my goals.</p>"""

def remove_newlines(text):
    return text.replace("\r", "").replace("\n", "")

save_post(title, remove_newlines(textHTML))