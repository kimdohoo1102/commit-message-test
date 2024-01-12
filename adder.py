def add(x,y) -> str:

    return int(x)+int(y)

if __name__ == "__main__":
    
    x = input('first num : ')
    y = input('second num: ')

    sum = add(x,y)

    print(sum)
