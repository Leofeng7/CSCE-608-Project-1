import random
import string
from gen_helper import*

import pandas as pd

users = pd.read_csv('../data/users_data.csv')
posts = pd.read_csv('../data/post_data.csv')

comment_ids = []
user_ids = []
post_ids = []
contents = []
dates = []

for i in range(0, 10000):
    comment_ids.append(generate_random_word(15))
    random_user = users.sample(n=1)
    random_post = posts.sample(n=1)
    user_ids.append(random_user['user_id'].iloc[0])
    post_ids.append(random_post['post_id'].iloc[0])
    contents.append(generate_random_word(random.randint(15, 240)))
    dates.append(generate_random_date())

df = pd.DataFrame(list(zip(comment_ids, user_ids, post_ids, contents, dates)),
                  columns=['comment_id', 'user_id', 'post_id', 'content', 'date'])

df.to_csv(r'../data/comments_data.csv', index=False)