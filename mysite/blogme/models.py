from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True,default=timezone.now())

    def __str__(self):
        return self.title

#sau khi create 1 bản post mới thì sẽ phải get_absolute_url để lấy đường dẫn mới đến đâu.
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


