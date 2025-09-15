# 딕셔너리 생성
# 딕셔너리에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제
# 딕셔너리 특정 key의 데이터를 수정

# enumerate, zip(), .items()  .keys  .values
# map(), 함수의 파라미터 - 키워드 파라미더, 가변 키워드 파라미터


cat = {
    "name" : "까미",
    "age" : 3,
    "color" : "black"
}
# 출력
print(f"cat['name'] = {cat['name']}")
# 값 추가
cat["type"] = "K.shorthair"
print(f'cat = {cat}')


cat = {}
names = ['까미', '올리', '생강']
ages = ['3', '5', '1']
