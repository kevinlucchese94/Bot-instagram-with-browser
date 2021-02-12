# BotInstagram
versione 2.0

nel crontab deve essere


  <code>0 8,16 * * 1,3,5 python3 path/to/folder/FollowByHashtag.py</code>

  <code>0 8,16 * * 2,4,6 python3 path/to/folder/FollowByLocation.py</code>

  <code>0 10,14,18,22 * * 1,3,5 python3 path/to/folder/LikeByHashtag.py</code>

  <code>0 10,14,18,22 * * 2,4,6 python3 path/to/folder/LikeByLocation.py</code>
 
  <code>0 8,18 * * * python3 path/to/folder/Unfollow.py</code>
