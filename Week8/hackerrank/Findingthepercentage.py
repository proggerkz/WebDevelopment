if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr = student_marks.get(query_name)
    sum = 0
    n = len(arr)
    for i in arr:
        sum += i
    print('{0:.2f}'.format(sum / n))