from django.conf import settings
from decimal import Decimal

from shop.models import Product

# 장바구니 - 세션(session)
class Cart:
    def __init__(self, request):
        self.session = request.session  # 세션 발급
        cart = self.session.get(settings.CART_ID)   # 장바구니 생성
        if not cart:
            cart = self.session[settings.CART_ID] = {}  # 빈 딕셔너리
        self.cart = cart

    def __len__(self):  # 수량 합계
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self): # 반복 메소드
        product_ids = self.cart.keys() # 제품 번호 리스트
        # 목록 id에서 해당 id의 모든 제품
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product    # 해당 제품 카트에 담기

        # 제품에 대한 내용 변경
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])  # 숫자형으로 변환
            # 전체 금액은 = 단위당 가격 X 수량
            item['total_price'] = item['price'] * item['quantity']
            yield item  # item을 반환

    # 장바구니에 제품 추가
    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)

        # 카트에 제품이 없는 경우
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        # 카트에 제품이 있는 경우
        # 수량 변경
        if is_update:
            self.cart[product_id]['quantity'] = quantity
        # 수량 증가
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def get_product_total(self):
        return sum(item['price'] for item in self.cart.values())

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

