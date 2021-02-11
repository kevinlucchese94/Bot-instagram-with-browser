# BotInstagram
versione 2.0

nel crontab deve essere


<code>
  0 8,16 * * 1,3,5 python3 FollowByFollower.py
</code>

<code>
  0 8,16 * * 2,4,6 python3 FollowByLocation.py
</code>

<code>
  0 10,14,18,22 * * 1,3,5 python3 LikeByHashtag.py
    </code>

<code>
  0 10,14,18,22 * * 2,4,6 python3 LikeByLocation.py
 
   </code>

<code>
  0 8,18 * * * python3 Unfollow.py
  </code>
