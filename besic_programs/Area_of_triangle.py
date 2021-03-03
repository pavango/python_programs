firtst_side = float(input('Enter first side: '))
second_side = float(input('Enter second side: '))
third_side = float(input('Enter third side: '))

semi_perimeter = (a + b + c) / 2

area = (semi_perimeter*(semi_perimeter-firtst_side )*(semi_perimeter-second_side)*(semi_perimeter-third_side)) ** 0.5

print('The area of the triangle is {0}'.format(area))
