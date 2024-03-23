import random
import string
from gen_helper import*

import pandas as pd

names = pd.read_csv('names.csv')['name']

email_suffixes = [
    "@gmail.com",
    "@yahoo.com",
    "@hotmail.com",
    "@aol.com",
    "@outlook.com",
    "@live.com",
    "@icloud.com",
    "@mail.com",
    "@protonmail.com",
    "@yandex.com",
    "@zoho.com",
    "@gmx.com",
    "@fastmail.com",
    "@msn.com",
    "@inbox.com"
]

user_ids = []
usernames = []
emails = []
about = []
user_type = []
followers = []

for i in range(0, 500):
    user_ids.append(generate_random_word(15))
    usernames.append(names[random.randint(0, names.size - 1)])
    emails.append(generate_random_word(random.randint(10, 15)) + email_suffixes[random.randint(0, len(email_suffixes) - 1)])
    about.append(generate_random_word(random.randint(50, 200)))
    user_type.append(random.randint(0, 2))
    followers.append(random.randint(0, 100000000))

df = pd.DataFrame(list(zip(user_ids, usernames, emails, about, user_type, followers)),
                  columns=['user_id', 'username', 'email', 'aboutme', 'account_type', 'followers'])

df.to_csv(r'../data/users_data.csv', index=False)