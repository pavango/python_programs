# Solve the quadratic equation ax**2 + bx + c = 0

import cmath

a_value = 1
b_value = 5
c_value = 6

# calculate the discriminant
discriminant_value = (b_value**2) - (4*a_value*c_value)

# finding two solutions
solution1 = (-b_value-cmath.sqrt(discriminant_value))/(2*a_value)
solution2 = (-b_value+cmath.sqrt(discriminant_value))/(2*a_value)

print('The solution are {0} and {1}'.format(solution1,solution2))
