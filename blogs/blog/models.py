from django.db import models

class Category(models.Model):
    # unique=True 중복 불허
    name = models.CharField(max_length=50, unique=True)
    # url 주소 - 문자, allow_unicode - 한글 허용
    slug = models.SlugField(max_length=200, unique=True,
                            allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        ordering = ['name']  # 이름순 정렬
        verbose_name = 'categorys'
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/', null=True, blank=True) # null허용, 파일 첨부하지 않을 때도 OK
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)    # category가 삭제되도 Post field는 삭제되지 않도록

    def __str__(self):
        return self.title