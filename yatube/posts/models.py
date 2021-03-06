from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(default="")

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
        )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, related_name="posts",
        blank=True, null=True, verbose_name='Группа'
        )
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment"
        )
    img = models.ImageField(upload_to='comments/', blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment'
        )
    text = models.TextField(
        max_length=100, help_text="Текст комменатрия", blank=True, null=True
        )
    created = models.DateTimeField('created', auto_now_add=True)

    class Meta:
        ordering = ['-id']


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
        )
