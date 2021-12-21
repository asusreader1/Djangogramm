from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    bio = models.TextField()

    follows = models.ManyToManyField('self', db_table='web_follows', related_name='followed_by', symmetrical=False)
    followers = models.ManyToManyField('self', db_table='web_followers', related_name='follow_to', symmetrical=False)


class Post(models.Model):
    text = models.TextField()
    media = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    likes = models.ManyToManyField(User, db_table='web_post_like_user', related_name='posts_likes')


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    likes = models.ManyToManyField(User, db_table='web_comment_like_user', related_name='comments_likes')


class Dialog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(User, related_name='input_messages', on_delete=models.SET_NULL, null=True)
    dialog = models.ForeignKey(Dialog, on_delete=models.SET_NULL, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

