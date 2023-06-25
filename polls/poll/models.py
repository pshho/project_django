from django.db import models

# 질문 테이블 모델
class Question(models.Model): # 상속 관계
    # 필드
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):  # 객체 정보를 문자열로 반환
        return self.question_text

# 항목 테이블(엔티티)
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

# 서울시부동산실거래가정보
class SeoulEstateReal(models.Model):
    접수연도 = models.IntegerField(null=True, blank=True)
    자치구코드 = models.IntegerField(null=True, blank=True)
    자치구명 = models.CharField(max_length=30)
    법정동코드 = models.IntegerField(null=True, blank=True)
    법정동명 = models.CharField(max_length=40)
    본번 = models.IntegerField(null=True, blank=True)
    부번 = models.IntegerField(null=True, blank=True)
    건물명 = models.CharField(max_length=200)
    계약일 = models.CharField(max_length=20, null=True, blank=True)
    물건금액_만원 = models.IntegerField(null=True, blank=True)
    건물면적 = models.CharField(max_length=30)
    토지면적 = models.CharField(max_length=30)
    층 = models.CharField(max_length=10)
    권리구분 = models.CharField(max_length=25, null=True, blank=True)
    취소일 = models.CharField(max_length=20, null=True, blank=True)
    건축년도 = models.CharField(max_length=20)
    건물용도 = models.CharField(max_length=50)
    신고구분 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.건물명

# 서울시부동산실거래가(위도,경도)
class SeoulEstateRentLonLat(models.Model):
    주소 = models.CharField(max_length=400)
    위도 = models.CharField(max_length=300)
    경도 = models.CharField(max_length=300)

    def __str__(self):
        return self.주소

# 서울시부동산전월세가정보
class SeoulEstateRent(models.Model):
    접수연도 = models.IntegerField(null=True, blank=True)
    자치구코드 = models.IntegerField(null=True, blank=True)
    자치구명 = models.CharField(max_length=30)
    법정동코드 = models.IntegerField(null=True, blank=True)
    법정동명 = models.CharField(max_length=40)
    본번 = models.IntegerField(null=True, blank=True)
    부번 = models.IntegerField(null=True, blank=True)
    층 = models.CharField(max_length=10)
    계약일 = models.CharField(max_length=20, null=True, blank=True)
    전월세구분 = models.CharField(max_length=30, null=True, blank=True)
    임대면적 = models.CharField(max_length=30)
    보증금_만원 = models.IntegerField(null=True, blank=True)
    임대료_만원 = models.IntegerField(null=True, blank=True)
    건물명 = models.CharField(max_length=200)
    건축년도 = models.CharField(max_length=20)
    건물용도 = models.CharField(max_length=50)
    계약기간 = models.CharField(max_length=100, null=True, blank=True)
    신규갱신여부 = models.CharField(max_length=20, null=True, blank=True)
    종전보증금_만원 = models.IntegerField(null=True, blank=True)
    종전임대료_만원 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.건물명

# 서울시부동산전월세가(위도,경도)
class SeoulEstateRealLonLat(models.Model):
    주소 = models.CharField(max_length=400)
    위도 = models.CharField(max_length=300)
    경도 = models.CharField(max_length=300)

    def __str__(self):
        return self.주소