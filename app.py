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

for submission in reddit.subreddit(SUBREDDIT).stream.submissions():
        print(submission.title)
        if submission is None:
                continue
        if("USA" in submission.title):
            embd = discord.Embed()
            embd.description = submission.title
            embd.title= submission.url
            webhook.send(embed=embd)
