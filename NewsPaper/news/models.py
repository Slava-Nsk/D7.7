from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum
from django.urls import reverse



# Create your models here.
class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comment_rating = Comment.objects.filter(user=self.author_user).aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        post_comment_rating = Comment.objects.filter(post__author=self).aggregate(pcr=Coalesce(Sum('rating'), 0))['pcr']

        self.author_rating = post_rating * 3 + comment_rating + post_comment_rating
        self.save()

    def __str__(self):
        return self.author_user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    news = 'N'
    article = 'A'
    type_choices = [(news, 'Новость'), (article, 'Статья')]
    type = models.CharField(max_length=1, choices=type_choices, default='A')  #
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  #
    in_time = models.DateTimeField(auto_now_add=True)  #
    category = models.ManyToManyField(Category, through='PostCategory')  #
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2000)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...' if len(self.text) > 124 else self.text

    def __str__(self):
        return self.preview()

    def get_absolute_url(self):
        return reverse('post_detail_name', args=[str(self.id)])




class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0.0)

    def __str__(self):
        return f'"{self.text}" автора {self.user} к записи "{self.post.title}". Рейтинг {self.rating}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
