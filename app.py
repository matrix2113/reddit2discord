import dhooks
import discord
import praw

# ENTER YOUR WEBHOOK ID AND WEBHOOK TOKEN HERE
WEBHOOK_ID = ""
WEBHOOK_TOKEN = ""
SUBREDDIT = ""

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username="",
                     password="")

webhook = Webhook(f"https://discord.com/api/webhooks/{WEBHOOK_ID}/{WEBHOOK_TOKEN}")

for submission in reddit.subreddit(SUBREDDIT).stream.submissions():
        print(submission.title)
        if not submission:
            return
        embd = discord.Embed()
        embd.description = submission.title
        embd.title= submission.url
        webhook.send(embed=embd)
