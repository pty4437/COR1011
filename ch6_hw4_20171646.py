import math

a,b,c = input("Enter a, b, c : ").split()
a = float(a)
b = float(b)
c = float(c)

D = math.pow(b,2) - 4*a*c

D = math.sqrt(D)

root1 = ((-1)*b + D) / (2 * a)
root2 = ((-1)*b - D) / (2 * a)

print("root1 = {:.4f} and root2 = {:.4f}.".format(root1, root2))

