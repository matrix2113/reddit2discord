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

for submission in reddit.subreddit(os.environ["SUBREDDIT"]).stream.submissions():
  print(submission.title)
  utc_time = datetime.utcfromtimestamp(float(submission.created_utc))
  embd = discord.Embed(color=0xE02424)
  embd.set_author(name=submission.author, icon_url=submission.author.icon_img, url=f"https://reddit.com/user/{submission.author}")
  embd.title= submission.title
  embd.url = submission.url
  embd.description = submission.selftext
  embd.set_footer(text=f"ID: {submission.id} | {utc_time.strftime('%m-%d-%Y %H:%M:%S (UTC)')}")
  try:
    webhook.send(embed=embd)
    time.sleep(15)
  except Exception as e:
    return
