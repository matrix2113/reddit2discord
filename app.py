import dhooks
import discord
import praw

import time
import os 

from datetime import datetime

reddit = praw.Reddit(client_id=os.environ["CLIENT_ID"],
                     client_secret=os.environ["CLIENT_SECRET"],
                     user_agent="python",
                     username=os.environ["USERNAME"],
                     password=os.environ["PASSWORD"])

webhook = dhooks.Webhook(f"https://discord.com/api/webhooks/{os.environ['WEBHOOK_ID']}/{os.environ['WEBHOOK_TOKEN']}")

# for submission in reddit.subreddit(os.environ["SUBREDDIT"]).stream.submissions():
submission = reddit.submission("ohl82i")
print(submission)

utc_time = datetime.utcfromtimestamp(float(submission.created_utc))

embd = discord.Embed()
embd.set_author(name=submission.author, icon_url=submission.author.icon_img, url=f"https://reddit.com/user/{submission.author}")
embd.description = submission.title
embd.title= submission.url
embd.set_footer(text=f"ID: {submission.id} | {utc_time.strftime('%m-%d-%Y %H:%M:%S (UTC)')}")
webhook.send(embed=embd)
