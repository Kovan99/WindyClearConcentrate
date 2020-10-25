from cs50 import get_int


def main():

    checksum = int(0)
    
    cc = str(get_int("Number: "))
    
    
    for i in range(0, len(cc), 1):
        index = len(cc) - 1 - i
        if i % 2 != 0:
            checksum += sum(int(digit) for digit in str((int(cc[index]) * 2)))
        if i % 2 == 0:
            checksum += int(cc[index])
    
    # This variable stores the first two digits of the card number
    first2digits = int(cc[0] + cc[1])
    # print(first2digits)

    if checksum % 10 == 0:
        if len(cc) == 16:
            if first2digits in [51, 52, 53, 54, 55]:
                print("MASTERCARD")
        if len(cc) == 15:
            if first2digits in [34, 37]:
                print("AMEX")
        if (len(cc) == 16) or (len(cc) == 13):
            if int(cc[0]) == 4:
                print("VISA")
    else:
        print("INVALID")


main()