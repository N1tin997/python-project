try:

    f = open('workfromhome.txt','r')
    f.write("This is test for exception!!")

except:
    print("Error Made by Nitin and it is wrong")

# else:
#     print('Success!')
#     f.close()
finally:
    print("Finally done")
print("Done")