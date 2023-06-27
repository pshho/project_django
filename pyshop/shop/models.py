from django.db import models
from django.urls import reverse

class Category(models.Model):
    # unique=True 중복 불허
    name = models.CharField(max_length=50, db_index=True)
    meta_description = models.TextField(blank=True)
    # url 주소 - 문자, allow_unicode - 한글 허용
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])

    class Meta:
        ordering = ['name']  # 이름순 정렬
        verbose_name = 'categorys'
        verbose_name_plural = 'categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=105, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)    # 소수 2째 자리까지
    stock = models.PositiveIntegerField()   # 재고 수량
    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)
    created = models.DateTimeField(auto_now_add=True)   # 상품 등록일(반드시 작성일 추가)
    updated = models.DateTimeField(auto_now=True)   # 필요할 때 수정일 추가

    class Meta:
        ordering = ['-created', '-updated']
        index_together = [['id', 'slug']]   # 인덱스 기능 id와 slug 혼합

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
