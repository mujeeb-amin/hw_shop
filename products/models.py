from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    # for changeing in admin panal
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class product(models.Model):
    title = models.CharField(
        max_length=120,
    )
    price = models.FloatField(default=10)
    catagory = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    type = models.CharField(
        choices=[
            ("for_kids", "For Kids"),
            ("for_men", "For Men"),
            ("for_women", "For women"),
        ],
        max_length=121,
        blank=True,
        null=True,
    )
    is_published = models.BooleanField()

    def __str__(self):
        return self.title

    # for changing in database
    class Meta:
        # abstract = True
        db_table = "products"
