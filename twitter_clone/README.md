- Kullanıcılar
- Twitler
- Reply
- Likes
- Retweet
-







- MYSQL
- Bootstrap
- Jquery
- Ajax
- MacOS = mamp    Windows = Wamp,Xamp,ampps
- Phpmyadmin,navicat
- http://docs.peewee-orm.com/en/latest/
- https://pythonhosted.org/Flask-Babel/
- https://flask-wtf.readthedocs.io/en/stable/
- https://wtforms.readthedocs.io/en/2.3.x/validators/#wtforms.validators.Email





users
- user_id(int,autoincrement,primarykey)
- username(str)
- email(str)
- password(str)
- first_name(str)
- surname(str)
- about(str)
- phone_number(str)
- website (str)
- create_date (datetime)
- is_verified (0,1)
- following_count
- follower_count


follows
- user_id
- following_id


likes
- user_id
- tweet_id


tweets
- tweet_id (int,autoincrement,primarykey)
- tweet_content (str)
- user_id
- tweet_date (datetime)
- like_count
- retweet_count
- reply_count
- parent_tweet_id(int)
- retweet_id

























