from django.db import models

# Create your models here.
class Weight(models.Model):
    alert = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    bruto = models.FloatField()
    tara = models.FloatField()
    netto = models.FloatField()
    discount = models.FloatField()
    amount_weight = models.FloatField()
    price = models.FloatField()
    amount_price = models.FloatField()
    paid_off = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering =['-id']
        verbose_name = "Weight"
        verbose_name_plural = "Weights"

    def __str__(self):
        return self.name
