from django.db import models

# Create your models here.


class TodoModel(models.Model):
    todo_desc=models.CharField(max_length=100,verbose_name="Enter First_name")
    todo_date=models.DateField(auto_now_add=True)
  

    class Meta:
        db_table="Todomodel"