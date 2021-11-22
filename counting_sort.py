def counting_sort(data:list):
    max_num = int(input())
    cnt = [0 for i in range(max_num)]
    sorted_data = []
    for i in data:
        cnt[i] += 1
    for i in range(len(cnt)-1):
        cnt[i+1] += cnt[i]
    for i in range(len(cnt)):
        for j in cnt[i]:
            sorted_data.append(i)
    return sorted_data

if __name__ == '__main__':
    data = list(map(int, input().split()))
    counting_sort(data)