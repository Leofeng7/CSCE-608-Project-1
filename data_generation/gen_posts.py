import random
import string
from gen_helper import*

import pandas as pd

users = pd.read_csv('../data/users_data.csv')

post_ids = []
user_ids = []
contents = []
dates = []

for i in range(0, 5000):
    post_ids.append(generate_random_word(15))
    random_user = users.sample(n=1)
    user_ids.append(random_user['user_id'].iloc[0])
    contents.append(generate_random_word(random.randint(1, 280)))
    dates.append(generate_random_date())


df = pd.DataFrame(list(zip(post_ids, user_ids, contents, dates)),
                  columns=['post_id', 'user_id', 'content', 'date'])

df.to_csv(r'../data/post_data.csv', index=False)