def solution(begin, target, words):
    def DFS(begin , target , words, count, result_array):
        if not(target in words):
            return [0]
        if begin == target:
            return [count]
        check = False
        for i in range(len(words)):
            diff_cnt = 0
            for j in range(len(words[0])):
                if words[i][j] != begin[j]:
                    diff_cnt += 1
            if diff_cnt == 1:
                check = True
                print(words[i:] + words[:i])
                result_array += DFS(words[i], target, words[i:], count+1, result_array)
        if not check:
            return result_array + [-1]
        return result_array
    result = DFS(begin, target, words, 0 , [])
    result.sort()
    for i in range(len(result)):
        if result[i] >= 0:
            return result[i]
    return 0
