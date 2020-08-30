from django.db import models

# Create your models here.
class Data(models.Model):
    year = models.CharField(max_length = 25,null=False)
    petroleum_product = models.CharField(max_length = 25,null=False)
    sale = models.FloatField(blank=False)

    def __str__(self):
        return self.petroleum_product
