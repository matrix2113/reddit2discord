import dhooks
import discord
import praw
import os 

reddit = praw.Reddit(client_id=os.environ["CLIENT_ID"],
                     client_secret=os.environ["CLIENT_SECRET"],
                     user_agent="python",
                     username=os.environ["USERNAME"],
                     password=os.environ["PASSWORD"])

webhook = dhooks.Webhook(f"https://discord.com/api/webhooks/{os.environ['WEBHOOK_ID']}/{os.environ['WEBHOOK_TOKEN']}")

for submission in reddit.subreddit(os.environ["SUBREDDIT"]).stream.submissions():
        print(submission.title)
        return
        embd = discord.Embed()
        embd.description = submission.title
        embd.title= submission.url
        webhook.send(embed=embd)
