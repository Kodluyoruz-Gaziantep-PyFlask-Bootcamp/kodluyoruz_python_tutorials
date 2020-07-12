from peewee import *

database = MySQLDatabase('kz_twitter_clone', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Users(BaseModel):
    about = CharField(null=True)
    create_date = DateTimeField()
    email = CharField()
    first_name = CharField()
    follower_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    following_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_verified = IntegerField(constraints=[SQL("DEFAULT 0")])
    password = CharField()
    phone_number = CharField(null=True)
    surname = CharField()
    user_id = AutoField()
    username = CharField()
    website = CharField(null=True)

    class Meta:
        table_name = 'users'

    @property
    def full_name(self):
        return str(self.first_name) + " " + str(self.surname)

class Follows(BaseModel):
    following = ForeignKeyField(column_name='following_id', field='user_id', model=Users, null=True)
    user = ForeignKeyField(backref='users_user_set', column_name='user_id', field='user_id', model=Users, primary_key=True)

    class Meta:
        table_name = 'follows'

class Tweets(BaseModel):
    like_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    parent_tweet = ForeignKeyField(column_name='parent_tweet_id', field='tweet_id', model='self', null=True)
    reply_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    retweet_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    retweet_id = IntegerField(null=True)
    tweet_content = TextField()
    tweet_date = DateTimeField()
    tweet_id = AutoField()
    user = ForeignKeyField(column_name='user_id', field='user_id', model=Users, null=True)

    class Meta:
        table_name = 'tweets'

class Likes(BaseModel):
    tweet = ForeignKeyField(column_name='tweet_id', field='tweet_id', model=Tweets, null=True)
    user = ForeignKeyField(column_name='user_id', field='user_id', model=Users, null=True)

    class Meta:
        table_name = 'likes'
        primary_key = False

