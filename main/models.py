from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='project_service')

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileFieldgit (upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class GetInTouch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OurStory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
