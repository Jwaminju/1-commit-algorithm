N, d, k, c = input().split()
N, d, k, c = int(N), int(d), int(k), int(c)

sushi = []
for i in range(N):
    sushi.append(int(input()))

def solution():
    left, right = 0, k  # len(sushi)-1
    max_plate = 0

    while True:              # O(n)
        count = 0
        plate = []  # sushi[left:right]
        for i in range(left, left+k):
            plate.append(sushi[i%N])

        # print(plate)
        plate = list(set(plate))   # 시간복잡도 O(k)
        count = len(plate)  # 가짓수 세기

        if plate.count(c) == 0:  # 쿠폰 적용
            count += 1
        if max_plate < count:
            max_plate = count

        left += 1
        if left == N:
            break


    return max_plate


num = solution()
print(num)
# for i in range(k):        # O(k)
#     if plate.count(i) > 1:    # O(n)  --> O(nk)
#
#         pass
