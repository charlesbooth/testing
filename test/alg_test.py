from bisect import bisect_left


def main():
    fin = open('words.txt')
    form = [word.rstrip().lower()
            for word in fin]
    while True:
        i = bisect_left(form, 'a', key=lambda x: x[0])
        print(i, form[i])


if __name__ == "__main__":
    main()
