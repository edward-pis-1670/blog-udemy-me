from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.title

#sau khi create 1 bản post mới thì sẽ phải get_absolute_url để lấy đường dẫn mới đến đâu.
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('blogme.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()






