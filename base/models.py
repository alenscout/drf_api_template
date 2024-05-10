from django.db import models

class ModelOneForTest(models.Model):
    title = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title

class ModelTwoForTest(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    two_to_one = models.ForeignKey(ModelOneForTest, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title