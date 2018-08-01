A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
A_P = 380
B_P = 1200
C_P = 180
if A in range(11, 21):
    A_P = A_P * 0.9
elif A in range(21, 31):
    A_P = A_P * 0.85
elif A > 31:
    A_P = A_P * 0.8

if B in range(11, 21):
    B_P = B_P * 0.95
elif B in range(21, 31):
    B_P = B_P * 0.85
elif B > 31:
    B_P = B_P * 0.8

if C in range(11, 21):
    C_P = C_P * 0.85
elif C in range(21, 31):
    C_P = C_P * 0.8
elif C > 31:
    C_P = C_P * 0.7
print(A_P*A + B_P*B + C_P*C)
