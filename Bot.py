__author__ = 'Sid'
from scrape import parser
import praw
import re
import time
username = "" #username here
passw = ""
r = praw.Reddit('Goodreads bot for /r/india by u/TheMereReflection v 1.0.')
r.login(username,passw) #we can make password a variable
subreddit = r.get_subreddit('test')
exp='https*://www.goodreads.com/book/show/[0-9]*\.\w*|www.goodreads.com/book/show/[0-9]*\.\w*'
p=re.compile(exp)
while True:
    subreddit_comments = subreddit.get_comments()
    for comment in subreddit_comments:
        flag=0

        for replies in r.get_submission(comment.permalink).comments[0].replies:
            print replies
            if replies.author.name==username:
                flag=1

                break
        if flag==0 and p.search(comment.body)!=None:
            url = p.search(comment.body)

            dic=parser(url.group())

            reply="ID: " + dic["id"] + " " + "ISBN: "+dic["isbn"] + " " + "Author: " + dic["author"] + " " + "Title: " + dic["title"]
            comment.reply(reply)



