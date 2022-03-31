from django.db import models

# Create your models here.
class Stocks(models.Model):
    Stock_id=models.AutoField
    Stock_sym=models.CharField(max_length=50)
    Stock_name=models.TextField(max_length=500)
    #Date_l= models.DateField()
    Paid_u=models.IntegerField()
    Isin_n=models.CharField(max_length=500)
    Face_v=models.IntegerField()
    Open_v=models.FloatField()
    Close_v=models.FloatField()
    High_v=models.FloatField()
    Last_v=models.FloatField()
    Low_v=models.FloatField()
    Prev_v=models.FloatField()
    Total_w=models.FloatField()
    #Time_s=models.DateField()
    Total_rd=models.FloatField()
    Total_t=models.IntegerField()
    DELIV_QTY=models.IntegerField()
    DELIV_PER=models.FloatField()
    AVG_PRICE=models.FloatField()



