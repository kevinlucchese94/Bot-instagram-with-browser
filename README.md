# BotInstagram
versione 2.0

nel crontab deve essere


  <code>0 10,16,22 * * 1,3,5 python3 /BotInstagram/FollowByHashtag.py</code>

  <code>0 10,16,22 * * 2,4,6 python3 /BotInstagram/FollowByLocation.py</code>

  <code>0 9,13,17,21 * * 1,3,5 python3 /BotInstagram/LikeByHashtag.py</code>

  <code>0 9,13,17,21 * * 2,4,6 python3 /BotInstagram/LikeByLocation.py</code>
 
  <code>0 8,14,20 * * * python3 /BotInstagram/Unfollow.py</code>
