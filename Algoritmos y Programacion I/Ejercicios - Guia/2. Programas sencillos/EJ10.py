def domino(n):
    for i in range(0, n+1):
        for j in range(i, n+1):
            print(f'{i}:{j}')


def main():
    domino(3)


main()