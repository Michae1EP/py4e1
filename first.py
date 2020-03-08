while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
        largest = None
        for value in num :
            if largest is None :
                largest = value
            elif value > largest :
                largest = value

        smallest = None
        for value in num :
            if smallest is None :
                smallest = value
            elif value < smallest :
                smallest = value

    except:
        print('Invalid input')

print("Minimum", smallest)
print("Maximum", largest)
