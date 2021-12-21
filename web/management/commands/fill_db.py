from django.core.management.base import BaseCommand
from factory.django import DjangoModelFactory
from factory import Faker
from djangogramm.web.models import User, Post, Comment, Message
#from web.models import User, Post, Comment, Message
import random


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('word')
    full_name = Faker('name')
    bio = Faker('text')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    text = Faker('paragraph')


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    text = Faker('sentence')


class MessageFactory(DjangoModelFactory):
    class Meta:
        model = Message

    text = Faker('sentence')


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    USER_COUNT = 20

    POST_MIN_COUNT = 5
    POST_MAX_COUNT = 10

    MIN_LIKES_PER_POST = 5
    MAX_LIKES_PER_POST = 15

    MIX_COMMENTS_PER_POST = 5
    MAX_COMMENTS_PER_POST = 15

    MIN_LIKES_PER_COMMENTS = 0
    MAX_LIKES_PER_COMMENTS = 7

    MIN_FOLLOWERS_COUNTS = 2
    MAX_FOLLOWERS_COUNTS = 7

    models = (User, Post, Comment, Message)

    def clear_models(self):
        for model in self.models:
            model.objects.all().delete()

    def generate_user(self):
        return [UserFactory() for _ in range(self.USER_COUNT)]

    def generate_post_and_likes(self, users):
        posts = []
        for user in users:
            for _ in range(random.randint(self.POST_MIN_COUNT, self.POST_MAX_COUNT)):
                post = PostFactory(user=user)
                post.likes.set(random.sample(users, random.randint(self.MIN_LIKES_PER_POST, self.MAX_LIKES_PER_POST)))
                posts.append(post)
        return posts

    def generate_comments_and_likes(self, posts, users):
        for post in posts:
            for _ in range(random.randint(self.MIX_COMMENTS_PER_POST, self.MAX_COMMENTS_PER_POST)):
                comment = CommentFactory(post=post, user=random.choice(users))
                comment.likes.set(
                    random.sample(users, random.randint(self.MIN_LIKES_PER_POST, self.MAX_LIKES_PER_POST)))

    def generate_followers_and_follows(self, users):
        for user in users:
            followers = {follower
                         for follower in
                         random.sample(users, random.randint(self.MIN_FOLLOWERS_COUNTS, self.MAX_FOLLOWERS_COUNTS))
                         if follower != user}
            follows = {follows
                       for follows in
                       random.sample(users, random.randint(self.MIN_FOLLOWERS_COUNTS, self.MAX_FOLLOWERS_COUNTS))
                       if follows != user}
            user.followers.set(followers)
            user.follows.set(follows)

    def handle(self, *args, **options):
        self.clear_models()

        users = self.generate_user()
        self.generate_followers_and_follows(users)
        posts = self.generate_post_and_likes(users)
        self.generate_comments_and_likes(posts, users)

        print('Data created...')

# 1h^00m
