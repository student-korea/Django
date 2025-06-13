from django.db import models

# Create your models here.
class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id= models.CharField(max_length=100)
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField()
    #답글달기
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    #------
    bhit = models.IntegerField(default=0)
    bfile = models.ImageField(null=True,blank=True,upload_to='board') # FileField
    ntcnk = models.IntegerField(default=0)
    bdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.bno},{self.btitle},{self.bgroup}'