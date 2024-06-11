from django.db import models

class Account(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Prompt(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return self.title

class MyFavo(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.prompt_id)