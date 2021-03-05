import cmath

a_value = 1
b_value = 5
c_value = 6

discriminant_value = (b_value**2) - (4*a_value*c_value)

solution1 = (-b_value-cmath.sqrt(discriminant_value))/(2*a_value)
solution2 = (-b_value+cmath.sqrt(discriminant_value))/(2*a_value)

print('The solution are {0} and {1}'.format(solution1,solution2))
