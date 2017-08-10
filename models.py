from django.db import models

class Posts(models.Model):
	title = models.CharField(max_length=60)
	post_content = models.TextField()
	published_date = models.DateTimeField(auto_now=True)
	# add in author and categories at a later stage
