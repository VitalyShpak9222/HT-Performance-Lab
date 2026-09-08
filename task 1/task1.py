import sys

def get_paths(n1, m1, n2, m2):
    path1 = []
    path2 = []

    current1 = 0
    current2 = 0

    finished1 = False
    finished2 = False

    for _ in range(max(n1, n2)):
        if not finished1:
            path1.append(current1 + 1)
            current1 = (current1 + m1 - 1) % n1

            if current1 == 0:
                finished1 = True

        if not finished2:
            path2.append(current2 + 1)
            current2 = (current2 + m2 - 1) % n2

            if current2 == 0:
                finished2 = True

        if finished1 and finished2:
            break

    return path1, path2

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])

n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

path1, path2 = get_paths(n1, m1, n2, m2)

result = ''.join(map(str, path1)) + ''.join(map(str, path2))

print(result)