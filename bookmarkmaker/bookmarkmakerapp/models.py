from django.db import models

class bookmarkMakertable(models.Model):
    site_name=models.CharField(max_length=300)
    site_url=models.CharField(max_length=3000)
