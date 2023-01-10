from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField
from .validators import textfield_not_empty

STATUS = ((0, "Content Not Checked"), (1, "Content Checked for Publishing"))

"""Model for Care Article"""
class Carearticle(models.Model):
    article_title = models.CharField(max_length=170, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True) 
    article_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="care_posts")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    article_image = CloudinaryField('image', default='placeholder')
    article_excerpt = models.TextField(blank=True)
    articel_content = models.TextField(validators=[textfield_not_empty])
    approved_status = models.IntegerField(choices=STATUS, default=0)
    bookmarks = models.ManyToManyField(User, related_name='bookmark', default=None, blank=True)
    helpful_ticks = models.ManyToManyField(User, related_name='carearticle_tick', blank=True)

    """Orders the Articles by date created on, in descending order"""
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_ticks(self):
        return self.helpful_ticks.count()


"""Model for Comments"""
class Article_comments(models.Model):
    article_comment = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=90)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    """Orders the comment by date created on ascending order"""
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"