from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=100)
    date_purchased = models.DateField(auto_now_add=True)
    cost_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_image = models.FileField(upload_to="", null=True)
    sells_price = models.DecimalField(max_digits=12, decimal_places=2)
    profit_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} | ₦{self.sells_price}'