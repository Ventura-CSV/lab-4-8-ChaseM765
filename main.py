def main():
    plist = []
    begin = int(input('Enter value greater than 1: '))
    end = int(input('Enter value greater than previous: '))
    while (begin < 1 or begin > end):
        begin = int(input('The number must be more than 1 and less than other entry: '))
        print ('Other entry:', end)

    for num in range(begin , end):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                plist.append(num)
    print(*plist)

    return plist


if __name__ == '__main__':
    main()
