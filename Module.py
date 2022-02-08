
# 모듈 사용 방법

import theater_module
theater_module.price(3) # 3명이서 영화를 보고 갔을 때.
theater_module.price_morning(3) # 3명이서 조조 영화를 보고 갔을 때.
theater_module.price_Army(3) # 3명의 군인들이 영화를 보고 갔을 때.

# 모듈 as를 사용해 이름 줄이기

import theater_module as mv
mv.price(2)
mv.price_morning(2)
mv.price_Army(2)

# form으로 사용한 모듈 사용법
# 모든 함수를 사용할 때 ==> import옆에 * 사용
from theater_module import*
price(2)
price_morning(4)
price_Army(5)

# 필요한 변수만 사용할 떼 == > import 옆에 사용하고 싶은 변수만 작성
from theater_module import price, price_morning
price(2)
price_morning(4)