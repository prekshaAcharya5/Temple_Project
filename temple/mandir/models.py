from django.db import models

# Create your models here.
from django.db import models


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     role = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


class Committee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CommitteeMember(models.Model):
    m_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    post = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='committee_members/')
    c_id = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContentImage(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    img_path = models.ImageField(upload_to='content_images/')

    def __str__(self):
        return f"Image for Content ID: {self.content_id.id}"


class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_date = models.DateField()

    def __str__(self):
        return self.name


class DonorImage(models.Model):
    id = models.AutoField(primary_key=True)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='donor_images/')

    def __str__(self):
        return f"Image for Donor ID: {self.donor_id.id}"


class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

