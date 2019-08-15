# import all the dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from youtube_data import youtube_search
import numpy as np


# enter name of youtube channel
test = youtube_search("Last moment tuitions")
test.keys()
comments=test['commentCount']
# print(comments)
df = pd.DataFrame(data=test)
# print(displayforgodssake)
df1 = df[['title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']]
df1.columns = ['Title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']
df1.head()
# displayforgodssake=df1.head()

numeric_dtype = ['viewCount','commentCount','likeCount','dislikeCount','favoriteCount']
for i in numeric_dtype:
    df1[i] = df[i].astype(int)

lmt = df1[df1['channelTitle']=='Last moment tuitions']
lmt.head()
# print(lmt_display)

lmt = lmt.sort_values(ascending=True,by='viewCount')
plt.bar(range(lmt.shape[0]),lmt['viewCount'])
plt.xticks(range(lmt.shape[0]),lmt['Title'],rotation=90)
plt.ylabel('View Count')

plt.show()














