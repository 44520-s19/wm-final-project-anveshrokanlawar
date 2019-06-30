# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:39:16 2019

@author: Anvesh Rokanlawar
"""

import requests
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt



def get_sentiments(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)



youtube_api = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&"
youtube_api_likes_comments='https://www.googleapis.com/youtube/v3/videos?'

youtube_api_key = "AIzaSyDjP-GSTWjqyZAJsYnnZ7FE905oCHgTaeE"

video_ids=['kJQP7kiw5Fk','JGwWNGJdvx8','RgKAFK5djSk','9bZkp7q19f0'
           ,'fRh_vgS2dFE','nfWlot6h_JM','CevxZvSJLk8']
video_id1 = video_ids[0]
video_id2 = video_ids[1]
video_id3 = video_ids[2]
video_id4 = video_ids[3]
video_id5 = video_ids[4]
#video_id6 = video_ids[5]
#video_id7 = video_ids[6]
#video_id4 = input('enter video id : ')
def data_request(videosid):
    data=requests.get(youtube_api + "videoId="+videosid+ "&key=" + youtube_api_key + "&maxResults=100"  )
    return data

def likesdata_request(videosid):
    likes=requests.get(youtube_api_likes_comments + 'id='+videosid+'&part=statistics'+"&key=" + youtube_api_key  )
    return likes
    
data1 = data_request(video_id1)
data2 = data_request(video_id2)
data3 = data_request(video_id3)
data4 = data_request(video_id4)
data5 = data_request(video_id5)

likes1=likesdata_request(video_id1)
likes2=likesdata_request(video_id2)
likes3=likesdata_request(video_id3)
likes4=likesdata_request(video_id4)
likes5=likesdata_request(video_id5)

comments_data1 = json.loads(data1.text)
comments_data2 = json.loads(data2.text)
comments_data3 = json.loads(data3.text)
comments_data4 = json.loads(data4.text)
comments_data5 = json.loads(data5.text)

likes_data1 = json.loads(likes1.text)
likes_data2 = json.loads(likes2.text)
likes_data3 = json.loads(likes3.text)
likes_data4 = json.loads(likes4.text)
likes_data5 = json.loads(likes5.text)

actual_comments1 = []
actual_comments2 = []
actual_comments3 = []
actual_comments4 = []
actual_comments5 = []

likes_views1 = []
likes_views2 = []
likes_views3 = []
likes_views4 = []
likes_views5 = []


for comment in comments_data1.get('items'):
     actual_comments1.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])
     
for comment in comments_data2.get('items'):
     actual_comments2.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])

for comment in comments_data3.get('items'):
     actual_comments3.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])

for comment in comments_data4.get('items'):
    actual_comments4.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])

for comment in comments_data5.get('items'):
     actual_comments5.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])

for like in likes_data1.get('items'):
    likes_views1.append(like['statistics']['viewCount'])
    likes_views1.append(like['statistics']['likeCount'])

for like in likes_data2.get('items'):
    likes_views2.append(like['statistics']['viewCount'])
    likes_views2.append(like['statistics']['likeCount'])
    
for like in likes_data3.get('items'):
    likes_views3.append(like['statistics']['viewCount'])
    likes_views3.append(like['statistics']['likeCount'])
    
for like in likes_data4.get('items'):
    likes_views4.append(like['statistics']['viewCount'])
    likes_views4.append(like['statistics']['likeCount'])
    
for like in likes_data5.get('items'):
    likes_views5.append(like['statistics']['viewCount'])
    likes_views5.append(like['statistics']['likeCount'])
    
#build yor figure
fig = plt.figure()
ax = fig.add_subplot(111)
sentiments1 = [get_sentiments(comment) for comment in actual_comments1]
sentiments2 = [get_sentiments(comment) for comment in actual_comments2]
sentiments3 = [get_sentiments(comment) for comment in actual_comments3]
sentiments4 = [get_sentiments(comment) for comment in actual_comments4]
sentiments5 = [get_sentiments(comment) for comment in actual_comments5]
#sentiments6 = [get_sentiments(comment) for comment in actual_comments6]
#sentiments7 = [get_sentiments(comment) for comment in actual_comments7]
#sentiments8 = [get_sentiments(comment) for comment in actual_comments8]

Video1pos = [sent['pos'] for sent in sentiments1]
Video2pos = [sent['pos'] for sent in sentiments2]
Video3pos = [sent['pos'] for sent in sentiments3]
Video4pos = [sent['pos'] for sent in sentiments4]
Video5pos = [sent['pos'] for sent in sentiments5]
#Video6pos = [sent['pos'] for sent in sentiments6]
#Video7pos = [sent['pos'] for sent in sentiments7]
#Video8pos = [sent['pos'] for sent in sentiments4]

Video1neg = [sent['neg'] for sent in sentiments1]
Video2neg = [sent['neg'] for sent in sentiments2]
Video3neg = [sent['neg'] for sent in sentiments3]
Video4neg = [sent['neg'] for sent in sentiments4]
Video5neg = [sent['neg'] for sent in sentiments5]
'''
Video1neu = [sent['neu'] for sent in sentiments1]
Video2neu = [sent['neu'] for sent in sentiments2]
Video3neu = [sent['neu'] for sent in sentiments3]
Video4neu = [sent['neu'] for sent in sentiments4]
Video5neu = [sent['neu'] for sent in sentiments5]
'''
mean_of_postives1=sum(Video1pos)/len(Video1pos)
mean_of_postives2=sum(Video2pos)/len(Video2pos)
mean_of_postives3=sum(Video3pos)/len(Video3pos)
mean_of_postives4=sum(Video4pos)/len(Video4pos)
mean_of_postives5=sum(Video5pos)/len(Video5pos)

mean_of_negatives1=sum(Video1neg)/len(Video1neg)
mean_of_negatives2=sum(Video2neg)/len(Video2neg)
mean_of_negatives3=sum(Video3neg)/len(Video3neg)
mean_of_negatives4=sum(Video4neg)/len(Video4neg)
mean_of_negatives5=sum(Video5neg)/len(Video5neg)
'''
mean_of_neturals1=sum(Video1neu)/len(Video1neu)
mean_of_neturals2=sum(Video2neu)/len(Video2neu)
mean_of_neturals3=sum(Video3neu)/len(Video3neu)
mean_of_neturals4=sum(Video4neu)/len(Video4neu)
mean_of_neturals5=sum(Video5neu)/len(Video5neu)
'''

n=5
index=np.arange(n)
barwidth=0.45
opacity=0.8

Positive=[mean_of_postives1,mean_of_postives2,mean_of_postives3,mean_of_postives4,mean_of_postives5]
Negative=[mean_of_negatives1,mean_of_negatives2,mean_of_negatives3,mean_of_negatives4,mean_of_negatives5]
#Neutral=[mean_of_neturals1,mean_of_neturals2,mean_of_neturals3,mean_of_neturals4,mean_of_neturals5]

views=[int(likes_views1[0]),int(likes_views2[0]),int(likes_views3[0]),int(likes_views4[0]),int(likes_views5[0])]
likes=[int(likes_views1[1]),int(likes_views2[1]),int(likes_views3[1]),int(likes_views4[1]),int(likes_views5[1])]
objects=('DESPACITO','SHAPE OF YOU','SEE YOU AGAIN','GANGNAM STYLE','JB-SORRY')
print(views)
'''
rects1 = plt.bar(index, Positive, barwidth,
alpha=opacity,
color='g',
label='Positive')

rects2 = plt.bar(index + barwidth, Negative, barwidth,
alpha=opacity,
color='r',
label='Negative')
'''

rects3 = plt.bar(index, likes, barwidth,
alpha=opacity,
color='b',
label='likes')

'''
rects4 = plt.bar(index + barwidth, views, barwidth,
alpha=opacity,
color='g',
label='views')
'''
'''
plt.xticks(index, objects)
plt.ylabel('Mean of Sentiments')
plt.title('Sentiment analysis of popular videos on YouTube')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
'''

plt.xticks(index, objects)
plt.ylabel('Count')
plt.title('likes of the popular videos')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
