from django.db import models

class CryptoCoin(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price_change = models.CharField(max_length=100)
    # market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    # market_cap_rank = models.CharField(max_length=10, null=True, blank=True)  # Allow null values
    # volume = models.DecimalField(max_digits=20, decimal_places=2)
    # volume_rank = models.CharField(max_length=10, null=True, blank=True)  # Allow null values
    # volume_change = models.DecimalField(max_digits=5, decimal_places=2)
    # circulating_supply = models.DecimalField(max_digits=20, decimal_places=2)
    # total_supply = models.DecimalField(max_digits=20, decimal_places=2)
    # diluted_market_cap = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    crypto_coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OfficialLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    crypto_coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    crypto_coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
