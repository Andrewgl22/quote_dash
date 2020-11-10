from django.db import models
import re

class Manager(models.Manager):

    def validator(self,postdata):
        errors={}
        if len(postdata['first_name']) < 2:
            errors['first_name'] = "First Name must be longer than 2 characters."
        if len(postdata['last_name']) < 2:
            errors['last_name'] = "Last Name must be longer than 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid Email Address"
        if len(postdata['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        return errors

    def quote_validator(self,postdata):
        errors={}
        if len(postdata['author']) < 3:
            errors['author'] = "Author must be at least 3 characters long."
        if len(postdata['quote']) < 10: 
            errors['quote'] = "Quote must be at least 10 characters long."
        return errors

    def update_validator(self,postdata):
        errors={}
        if len(postdata['first_name']) <1:
            errors['first_name'] = "Field required"
        if len(postdata['last_name']) <1:
            errors['last_name'] = "Field required"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid Email Address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    user = models.ForeignKey(User,related_name='quotes',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

# I could not figure out whether likes need a class or what...
class Like(models.Model):
    like = models.IntegerField()
    user = models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote,related_name='likes',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
