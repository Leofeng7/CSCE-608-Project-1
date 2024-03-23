import random
import string
from gen_helper import*

import pandas as pd

users = pd.read_csv('../data/users_data.csv')

posts = pd.read_csv('../data/post_data.csv')

comments = pd.read_csv('../data/comments_data.csv')

like_ids = []
user_ids = []
post_ids = []
comment_ids = []
dates = []

for i in range(0, 10000):
    like_ids.append(generate_random_word(15))
    random_user = users.sample(n=1)
    user_ids.append(random_user['user_id'].iloc[0])
    entity_type = generate_entity_type()
    if (entity_type == 'Post'):
        random_post = posts.sample(n=1)
        post_ids.append(random_post['post_id'].iloc[0])
        comment_ids.append('null')
    else:
        random_comment = comments.sample(n=1)
        comment_ids.append(random_comment['comment_id'].iloc[0])
        post_ids.append('null')

    dates.append(generate_random_date())

df = pd.DataFrame(list(zip(like_ids, user_ids, comment_ids, post_ids, dates)),
                  columns=['like_id', 'user_id', 'comment_id', 'post_id', 'date'])

df.to_csv(r'../data/likes_data.csv', index=False)