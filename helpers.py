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

title = "📝 A Productive Day (or at least I tried) 😊"
textHTML = """<p>Today, I am happy to say that I finished coding and deploying my daily journal! It's been a long time coming, but I am finally able to keep track of my daily activities and thoughts in one central location.</p>
<p>Next on my to-do list is adding the articles I have written to the <b>Serenebase Blog</b>. I am excited to share my thoughts and insights with a wider audience, and I hope that my content will be well-received.</p>
<p>Looking ahead to the following week, I will be thinking of a strategy to market <i>Viberooms</i>. I have a few ideas in mind, but I want to make sure I have a solid plan before moving forward.</p>
<p>In addition to working on Viberooms, I will also be simultaneously working on a creative tools project that uses <u>generative AI</u>. This is an idea I have been developing for a while now, and I am eager to see it come to fruition.</p>
<p>Overall, today was not as productive as I would have liked. I found myself getting distracted and losing focus at times, so I am planning on working on that in the coming days.</p>
<p>I am determined to make the most out of each day and achieve my goals, no matter how small they may seem. I know that with hard work and determination, anything is possible.</p>
"""

def remove_newlines(text):
    return text.replace("\r", "").replace("\n", "")

save_post(title, remove_newlines(textHTML))