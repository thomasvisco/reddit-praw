
import praw
import pandas as pd

r = praw.Reddit(client_id='j2rOXc83Q1ojcQ',
                client_secret='IDR1o4sqwgMxlsDpoVB6vx9WvCU',
                password='thisismyPassword',
                user_agent='script by /u/tav1991',
                username='tav1991')

subreddit = r.subreddit('combatfootage')

keyword = 'ATGM'

header_list = ['title', 'id', 'url']

titles = []
ids = []
urls = []

for submission in subreddit.hot(limit=1000):
    if keyword in submission.title:
        titles.append(submission.title)

for submission in subreddit.hot(limit=1000):
    if keyword in submission.title:
        ids.append(submission.id)

for submission in subreddit.hot(limit=1000):
    if keyword in submission.title:
        urls.append(submission.url)

df = pd.DataFrame({'Titles': titles, 'Ids': ids, 'URLs': urls})

del titles, ids, urls

pd.to_csv('results.csv')