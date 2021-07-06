def search(homes, distance):
    homes.sort()
    left, right = 1, homes[-1]-homes[0]
    result = 0

    while left <= right:
        mid = (left + right)//2
        first = homes[0]
        count = 1

        for i in range(1, len(homes)):
            if homes[i] >= first+mid:
                count += 1
                first = homes[i]
        if count >= distance:
            left = mid + 1
            result = mid
        else:
            right = mid-1
    return result


if __name__ == '__main__':
    house, wifi = map(int, input().split())
    coord = []
    for i in range(house):
        coord.append(int(input()))
    a = search(coord, wifi)
    print(a)
