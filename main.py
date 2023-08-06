def triangle(n):
    arr = [1 for i in range(n)]

    if n > 2:
        prevArr = triangle(n - 1)

    for i in range(n - 2):
        arr[i + 1] = prevArr[i] + prevArr[i + 1]
    
    return arr
    
def startTriangle(n):
    for i in range(1, n + 1):
        print(triangle(i))

startTriangle(20)