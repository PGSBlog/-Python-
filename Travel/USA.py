class USAPackage:
    def detail(self):
        print("[미국 패키지] 뉴욕 여행 150만원")

if __name__ == "__main__" : 
    print("USA 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to = USAPackage()
    trip_to.detail()
else:
    print("USA 외부에서 모듈 호출")