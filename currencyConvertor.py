import praw
#import pbd
import re
import os

reddit = praw.Reddit('bot1')

'''
subreddit = reddit.default()

print(reddit)

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
'''
f2 = open("replies.txt", "r")
repliedPosts = []


repliedPosts = f2.read()
repliedPosts = repliedPosts.split("\n")    
repliedPosts = list(filter(None, repliedPosts))

#print(repliedPosts)



f= open("replies.txt", "a")

for s in reddit.front.hot():
    #print(s)
    sub = reddit.submission(s)
    #print(sub.shortlink)
    #f.write(str(s))
    #f.write("\n")        
    #print("Title: ", sub.title)
    #print("Text: ", sub.selftext)
    #print("Score: ", sub.score)
    sub.comments.replace_more(limit=0)
    for c in sub.comments.list():
        print(c.body)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") 
    break



    
