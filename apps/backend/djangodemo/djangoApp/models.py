from django.db import models

class NumberModel(models.Model):
    name = models.CharField(max_length=20)
    num_orders = models.PositiveSmallIntegerField(default=0)
    num_stocs = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
    

class MyModel(models.Model):
    name = models.CharField(max_length=20)
    
    COUNTRY_CHOICES = [
    ('Europe', (
            ('FR', 'France'),
            ('ES', 'Spain'),
            ('TR', 'Turkey'),
        )
    ),
    ('Africa', (
            ('MA', 'Morocco'),
            ('DZ', 'Algeria'),
            ('NG', 'Nigeria'),
        )
    ),
    ('Asia', (
            ('CN', 'China'),
            ('MH', 'Malaysia'),
            ('RU', 'Russia'),
        )
    ),
    ]
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, default='Turkey')

    productID = models.DecimalField(max_digits=8, decimal_places=0, default=11111)

    YEAR_CHOICES = (
        ('2000', '2000'),
        ('2005', '2005'),
        ('2010', '2010'),
        ('2015', '2015'),
        ('2020', '2020'),
    )
    
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, default='2020')
    
    def __str__(self):
        return self.name

    