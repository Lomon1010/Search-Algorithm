import time
import random

a = [] # 빈 리스트 생성

q = int(input("데이터를 최대 몇까지 만들까요? : "))

for i in range(q): # 리스트에 1부터 유저입력까지 받음
    a.append(i+1)

q1 = int(input("데이터는 [1, 2, 3, 4, 5, ... ,"+str(q)+"]입니다.\n어떤 데이터를 찾을까요? : ")) # 찾을 값
q2 = int(input("해시 함수는 Value를 key로 나눈 나머지입니다. key를 몇으로 설정할까요? : ")) # 해시 키
q3 = int(input("해시 함수의 경우 사실감을 위해 자료를 섞을까요?\n1. Yes\n2. No\n: ")) 
# 선형 탐색
print('\n<선형 탐색>\n')
times = 0 # 걸린 횟수 변수

start1 = time.time() # 시간 재기 시작
i = 1

while i != q1: # 반복
    print(i, "아니군요.")
    times += 1
    i += 1
    
times += 1 # 마지막에 값 맞는지 확인하는 과정도 걸린 횟수에 추가
end1 = time.time() # 시간 끝
print("\n<선형 탐색>\n", q1, "찾았습니다. {}회 걸림\n {}초 걸렸습니다.\n".format(times, end1-start1)+'-'*50)

# 이진 탐색
print('\n<이진 탐색>\n')
times = 0 # 걸린 횟수 변수

start2 = time.time() # 시간 재기 시작
        
first = 0
last = len(a) - 1

while last >= first: # 반복
    middle = (first + last) // 2 # 중앙값 찾기
            
    if a[middle] == q1:
        times += 1 # 마지막에 값 맞는지 확인하는 과정도 걸린 횟수에 추가
        end2 = time.time() # 시간 끝
        print("\n<이진 탐색>\n", q1, "찾았습니다. {}회 걸림\n {}초 걸렸습니다.\n".format(times, end2-start2)+'-'*50)
        break
    else:
        print(a[middle], "아니군요.")
        times += 1
        if q1 < a[middle]:
            last = middle - 1
        else:
            first = middle + 1

# 해시 탐색
print('\n<해시 탐색>\n')
times = 0 # 걸린 횟수 변수

start3 = time.time() # 시간 재기 시작

key = q2

if q3 == 1:
    random.shuffle(a) # 자료가 랜덤으로 주어진 경우여야 좀 더 결과가 예쁠 듯하다.

def hash_func(p, key): # 해시함수 (key로 나눈 나머지)
    return p % key

def hash_table(arr): # 배열
    global key
    hash_len = round(len(arr) * 1.5 + 0.5)
    hash_arr = [0 for i in range(hash_len)]
    i = 0
    while i < len(arr):
        k = arr[i] % key
        if hash_arr[k] != 0:
            while hash_arr[k] != 0:
                k += 1
            hash_arr[k] = arr[i]
        else:
            hash_arr[k] = arr[i]
        i += 1

    return hash_arr

b = hash_table(a) # b = 배열

hf = hash_func(q1, key) # 찾고자하는 값을 해시함수에 넣음

while b[hf-1] != q1: # 찾기
    times += 1
    if b[hf] == q1:
        end3 = time.time()
        print("\n", q1, "찾았습니다. {}회 걸림\n {}초 걸렸습니다.\n".format(times, end3-start3)+'-'*50)
        break
    else:
        print(b[hf], "아니군요.")
        hf += 1

print('##### 참고 #####\n자료: '+str(a)+'\n\n'+'해싱: '+str(b)+'\n') # 자료값과 해싱한 배열        
