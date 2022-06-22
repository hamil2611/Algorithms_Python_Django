def nhan_matran_33_31(m1, m2):
    return (
        m1[0][0] * m2[0] + m1[0][1] * m2[1] + m1[0][2] * m2[2],
        m1[1][0] * m2[0] + m1[1][1] * m2[1] + m1[1][2] * m2[2],
        m1[2][0] * m2[0] + m1[2][1] * m2[1] + m1[2][2] * m2[2]
    )
 
def nhan_matran_33_33(m1, m2):
    return (
        (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0] + m1[0][2] * m2[2][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]+m1[0][2] * m2[2][1],m1[0][0] * m2[0][2] + m1[0][1] * m2[1][2]+m1[0][2] * m2[2][2]),
        (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]+ m1[1][2] * m2[2][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]+ m1[1][2] * m2[2][1],m1[1][0] * m2[0][2] + m1[1][1] * m2[1][2]+ m1[1][2] * m2[2][2]),
        (m1[2][0] * m2[0][0] + m1[2][1] * m2[1][0]+ m1[2][2] * m2[2][0], m1[2][0] * m2[1][0] + m1[2][1] * m2[1][1]+ m1[2][2] * m2[2][1],m1[2][0] * m2[0][2] + m1[2][1] * m2[1][2]+ m1[2][2] * m2[2][2])
    )
 
def pow_matrix(m, n):
    if n == 1:
        return m
    elif n % 2 == 0:
        a = pow_matrix(m, n / 2)
        return nhan_matran_33_33(a, a)
    else:
        return nhan_matran_33_33(pow_matrix(m, n - 1), m)
 
def dayso(n):
    if n == 0:
        return 4
    if n == 1:
        return 7
    if n == 2:
        return 5
    a = ((1,1,1),(1, 0,0),(0,1,0))
    an = pow_matrix(a, n-2)
    phantu_dauvao = (5,7,4)
    phantu_n = nhan_matran_33_31(an, phantu_dauvao)
    return phantu_n[0]
    
n = input("Nhap n:")
print(dayso(int(n)))