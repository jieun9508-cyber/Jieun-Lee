# 클래스 변수 vs 인스턴스 변수 (객체별로 독립적으로 존재하는 변수)

class StudentMng :
    name = '홍길동'  # 클래스변수

s1 = StudentMng()
s2 = StudentMng()
s3 = StudentMng()

s1.name = '이순신'
print(s1.name, s2.name, s3.name)
s1.name = '강감찬'
StudentMng.name = '이순신'
print(s1.name, s2.name, s3.name)

# 클래스변수는 모든 객체가 참조하는 변수
# 그러나 객체가 변수를 재할당받으면 해당 객체는 더 이상 참조하지 X
