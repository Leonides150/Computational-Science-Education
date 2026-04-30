# Python args
# The function shows the usage of *args in python by which you can pass any number of arguments to a function
def sum_nums(*args):
    sum=0
    for i in args:
        sum += i
    return sum

print(sum_nums(4, 5, 6, 7, 921, 45))

#Python kwargs
# 
def sum_nums(**kwargs):
    sum=0
    for i, v in kwargs.items():
        sum += v
    return sum

print(sum_nums(flight=400, rentalcar=5, accomodation=600, sightseeing=700, purchases=921, tips=45))