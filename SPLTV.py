# Memasukkan koefisien SPLTV
x11 = float(input("Masukkan nilai x11: "))
y12 = float(input("Masukkan nilai y12: "))
z13 = float(input("Masukkan nilai z13: "))
b1 = float(input("Masukkan nilai b1: "))
x21 = float(input("Masukkan nilai x21: "))
y22 = float(input("Masukkan nilai y22: "))
z23 = float(input("Masukkan nilai z23: "))
b2 = float(input("Masukkan nilai b2: "))
x31 = float(input("Masukkan nilai x31: "))
y32 = float(input("Masukkan nilai y32: "))
z33 = float(input("Masukkan nilai z33: "))
b3 = float(input("Masukkan nilai b3: "))

# Menghitung determinan matriks koefisien
detA = x11*(y22*z33-z23*y32) - y12*(x21*z33-z23*x31) + z13*(x21*y32-y22*x31)

# Cek apakah SPLTV memiliki solusi unik
if detA != 0:
    # Menghitung nilai x, y, z
    x = (b1*(y22*z33-z23*y32) - y12*(b2*z33-b3*z23) + z13*(b2*y32-b3*y22)) / detA
    y = (x11*(b2*z33-b3*z23) - b1*(x21*z33-z23*x31) + z13*(x21*b3-x31*b2)) / detA
    z = (x11*(y22*b3-y32*b2) - y12*(x21*b3-x31*b2) + b1*(x21*y32-y22*x31)) / detA
    print(f"Nilai x = {x}, y = {y}, z = {z}")
else:
    print("SPLTV tidak memiliki solusi unik")
