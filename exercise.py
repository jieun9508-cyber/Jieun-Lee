# num = []
# for x in range (1,11) :
#     num.append(x)
# print(sum(num))

# text = "apple banana apple grape apple"
# print(text.count("apple"))
# print(text.split())
# print(text.split().count("apple"))

# a = text.split()
# count = 0

# for x in a :
#     if x == "apple" :
#         count += 1
# print(count)

# nums = []
# def square_nums(n) : 
#     for x in range(1,n+1) :
#         nums.append(x**2)
#     return sum(nums)
# print(square_nums(10))

# def square_nums(n) :
#     return sum(n**2 for n in range(1,n+1))
# print(square_nums(10))

# def result(n) :
#     if n>= 60 :
#         print("Pass")
#     else :
#         print("Fail")
# result(90)


# "정수 n을 입력받아 1부터 n까지의 짝수 합 프로그램 출력하기"

# 1. 지역 변수 사용
# def even(n) :
#     num = []
#     for x in range(1,n+1) :
#         if x%2 == 0:
#             num.append(x)
#     return num
# print(sum(even(10)))

# 2. range 사용
# def even(n) :
#     return sum(range(2,n+1,2))
# print(even(10))

# 3. 리스트 컴프리헨션
# def even(n) :
#     return sum([x for x in range(1,n+1) if x%2 == 0])
# print(even(10))

# 구구단
# n = int(input())
# for i in range(1,10) :
#      print(f"{n}*{i} = {n*i}")


# a = "Python"
# print(a[::-1])

# (a,b) = (5,3)
# print(a*b -(a+b))

# s = "Hello"
# n = 5
# print(s*n)


# n = 90
# if n >= 60 :
#     print("Pass")
# else :
#     print("Fail")

# even = []
# for n in range(1,11) :
#     if n%2 == 0 :
#         even.append(n)
# print(sum(even))

# 구구단
# n = 3
# for i in range(1,10) :
#         print(f"{n}*{i} = {n*i}")
# print()

# text = ["apple", "banana", "apple", "grape", "apple"]
# word = "apple"
# same = []
# for i in text :
#     if i == word :
#         same.append(i)
# print(len(same))

# text = ("apple", "banana", "apple", "grape", "apple")
# word = "apple"
# same = []
# for i in text :
#     if i == word :
#         same.append(i)
# print(len(same))

# print(max(10 , 20 ,35 , 40 , 5 ))

# result = []
# def plus_return(n) :
#     for i in range(1,n+1) :
#       result.append(i**2)
#     return result
# print(sum(plus_return(5)))


# def square_sum(n) :
#     return sum(i**2 for i in range(1,n+1))
# n = int(input())
# print(square_sum())

# map_lambda_filter 활용 vs 리스트 컴프리헨션 활용

# result = map(lambda x: x**2,filter(lambda x: x%2 == 1, range(1,11)))
# print(list(result))

# print(list(x**2 for x in range(1,11) if not x%2 == 0))

# words = ["apple", "banana", "kiwi"]
# result = map(len,words)
# print(list(result))

# words = ["apple", "banana", "kiwi"]
# result = map(str.upper, words)
# print(list(result))

# numbers = [1,2,3,4,5]
# result = map(lambda x : x**2+1, numbers)
# print(list(result))

# nums = ["10", "20", "30"]
# result = map(int, nums)
# print(list(result))

# 평균 (소수 첫째 자리)
# n = int(input())
# nums = list(map(int, input().split()))
# avg = sum(nums) / n
# print(f"{avg:.1f}")

# 리스트 필터링
# n = int(input())
# nums = list(map(int, input().split()))
# k = int(input())

# filtered = [x for x in nums if x >= k]
# filtered.sort()     --- 오름차순
# filtered.sort(reverse=True)  --- 내림차순

# if filtered:
#     print(" ".join(map(str, filtered)))
# else:
#     print("None")

# n = int(input())
# nums = list(map(int, input().split()))
# filtered = [x for x in nums if x%2 == 1]
# filtered.sort(reverse=True)
# if filtered :
#     print(" ".join(map(str,filtered)))
# else :
#     print("None")