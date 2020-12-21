def lesser_of_two_evens(a,b):

    if (a%2==0 and b%2==0):

        if a > b:
            return b
        else:
            return a

    elif (a%2!=0 or b%2!=0):

        if a > b:

            return a
        else:
            return b

print(lesser_of_two_evens(2,5))

