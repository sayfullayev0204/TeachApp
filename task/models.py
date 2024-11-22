# from django.db import models
# from django.contrib.auth.models import User

# class Country(models.Model):
#     name = models.CharField(max_length=255)

# class School(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     admin = models.ForeignKey(User, on_delete=models.CASCADE)


# # 1-sinfdan 4-sinfgacha bo'lgan sinf tanlovlari
# CLASS_CHOICES = [
#     (1, '1-sinf'),
#     (2, '2-sinf'),
#     (3, '3-sinf'),
#     (4, '4-sinf'),
# ]

# # Uy Vazifasi modeli
# class Homework(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='images/')
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     grade = models.IntegerField(choices=CLASS_CHOICES)

#     def __str__(self):
#         return self.title

# # To'g'ri Yechimlar modeli
# class Solution(models.Model):
#     homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='solutions')
#     teacher = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField(blank=True)
#     image = models.ImageField(upload_to='solutions/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Solution for {self.homework.title}"

# # Izohlar modeli
# class Comment(models.Model):
#     homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
#     text = models.TextField()
#     image = models.ImageField(upload_to='comments/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.user.username}"


from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    category_choices = (
        ('1-sinf', '1-sinf'),
        ('2-sinf', '2-sinf'),
        ('3-sinf', '3-sinf'),
        ('4-sinf', '4-sinf')
    )
    category = models.CharField(max_length=20, choices=category_choices)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tasks/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return self.title
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='answer/')
    created_at = models.DateTimeField(auto_now=True)
    image_url = models.TextField(blank=True)
    def __str__(self):
        return self.title
