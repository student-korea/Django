from django.db import models

# Create your models here.
# class Product(models.Model):
#     pro_code = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=1000)
#     main_cate = models.CharField(max_length=100)
#     sub_cate = models.CharField(max_length=100)
#     origin = models.CharField(max_length=100)
#     weight = models.DecimalField(max_digits=10, decimal_places=2)
#     con_price = models.IntegerField(default=0)
#     dis_price = models.IntegerField(default=0)  
#     stock = models.IntegerField(default=0)
#     main_img = models.ImageField(upload_to='product/')
#     sub_img = models.ImageField(upload_to='product/', null=True, blank=True)
#     sub_img2 = models.ImageField(upload_to='product/', null=True, blank=True)
#     reg_date = models.DateTimeField(auto_now_add=True)
#     mod_date = models.DateTimeField(auto_now=True)
#     is_act = models.IntegerField(default=0)
#     ex_level = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name