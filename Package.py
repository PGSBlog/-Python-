# Package를 사용해 모듈 출력
# 주의할 점 : import를 쓸때는 맨뒤에 모듈, 패키지만 사용할 수 있다. // 클래스나 함수는 사용할 수 없다.
# Ex) import Travel.USA(모듈)  

from Travel import France
import Travel.USA
trip_to = Travel.USA.USAPackage()
trip_to.detail()

# from import는 사용할 수 있다.
# from 구문에선는 import를 사용할 때 클래스, 함수도 사용할 수 있다.
from Travel.USA import USAPackage
trip_to = Travel.USA.USAPackage()
trip_to.detail()

# __all__를 사용법(__init__파일도 참고하기)

from Travel import *
trip_to = France.FrancePackage()
trip_to = USA.USAPackage() # __init__에서 프랑스 정보면 공유했기에 그렇다. __init__에 미국정보를 공유하면 사용할 수 있다.
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(USA))