from django.db import models
from member.models import Member

# Create your models here.
class Customer(models.Model):
    bno = models.AutoField(primary_key=True)
    # id= models.CharField(max_length=100)
    member = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True)
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField()
    #답글달기
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    #------
    bhit = models.IntegerField(default=0)
    bfile = models.ImageField(null=True,blank=True,upload_to='customer') # FileField
    bfile2 = models.ImageField(null=True,blank=True,upload_to='customer') # FileField
    ntchk = models.IntegerField(default=0)
    bdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.bno},{self.btitle},{self.bgroup}'
    
# class customerFile(models.Model):
#     fno = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
#     ffile = models.ImageField(null=True,blank=True,upload_to='board') # FileField
#     fdate = models.DateTimeField(auto_now=True)