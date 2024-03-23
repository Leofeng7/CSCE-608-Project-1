import random
import string
from gen_helper import*

import pandas as pd

posts = pd.read_csv('../data/post_data.csv')

comments = pd.read_csv('../data/comments_data.csv')

hashtag_ids = []
post_ids = []
comment_ids = []
hashtag_names = []

for i in range(0, 10000):
    hashtag_ids.append(generate_random_word(15))
    entity_type = generate_entity_type()
    if (entity_type == 'Post'):
        random_post = posts.sample(n=1)
        post_ids.append(random_post['post_id'].iloc[0])
        comment_ids.append('null')
    else:
        random_comment = comments.sample(n=1)
        comment_ids.append(random_comment['comment_id'].iloc[0])
        post_ids.append('null')

    hashtag_names.append(generate_random_word(random.randint(5, 15)))

df = pd.DataFrame(list(zip(hashtag_ids, comment_ids, post_ids, hashtag_names)),
                  columns=['hashtag_id', 'comment_id', 'post_id', 'hashtag_name'])

df.to_csv(r'../data/hashtags_data.csv', index=False)