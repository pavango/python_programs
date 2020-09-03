list = [1,2,3,4,5,6,7,8,9,10]
n = int(input("Enter The Table Number :"))
for i in list:
    table = n*i
    print("{0} * {1} = {2}".format(n, i, table))
