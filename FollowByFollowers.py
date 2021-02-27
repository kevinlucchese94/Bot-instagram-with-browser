from instapy import InstaPy
from instapy import smart_run
from credenziali import *

# login credentials
insta_username = username
insta_password = password

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # Follows the followers of each given user
    # The usernames can be either a list or a string
    # The amount is for each account, in this case 30 users will be followed
    # If randomize is false it will pick in a top-down fashion

    session.follow_user_following(['user1', 'user2', 'user3', 'user4', 'user5'], amount=5, randomize=False)
    session.close()
