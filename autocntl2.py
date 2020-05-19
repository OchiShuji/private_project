import numpy as np 
from matplotlib import pyplot as plt 

print("(step0) 状態方程式、観測方程式を設定してください")
print("参考：(状態方程式) x = Ax + Bu\n      (観測方程式) y = Cx")
m = int(input("入力数="))
n = int(input("次元="))
r = int(input("出力数="))

A = np.zeros((n,n))
B = np.zeros((n,m))
C = np.zeros((r,n))
for i in range(0,n):
    for j in range(0,n):
        def input_A():
            try:
                A[i,j] = input("A：{}行{}列要素=".format(i+1,j+1))
            except ValueError:
                print("エラー：不正な入力")
                input_A()
        input_A()

for i in range(0,n):
    for k in range(0,m):
        def input_B():
            try:
                B[i,k] = input("B：{}行{}列要素=".format(i+1,k+1))
            except ValueErro
                print("エラー：不正な入力")
                input_B()
        input_B()

for l in range(0,r):
    for i in range(0,n):
        def input_C():
            try:
                C[l,i] = input("C：{}行{}列要素=".format(l+1,i+1))
            except ValueError:
                print("エラー：不正な入力")
                input_C()
        input_C()

print("\n(step1) 極配置を求めます\n")
lmd,V = np.linalg.eig(A)
lmd_c = np.zeros(3)
stbl_flg = 0
for i in range(0,n):
    print("極{}:{}".format(i+1,lmd[i]))
    if lmd[i].real < 0.0:
        stbl_flg = stbl_flg + 1
if stbl_flg == n:
    print("\n極の安定性：安定")
else:
    print("\n極の安定性：不安定")

print("\n(step2) 可制御性を判定します")
M_c = np.zeros((n,n*m))
M_c[0:n+1,0:m] = B
for i in range(0,n):
    B_prev = M_c[0:n+1,i*m:(i+1)*m]
    M_c[0:n+1,(i+1)*m:(i+2)*m] = np.dot(A,B_prev)
print("\n可制御行列：\n",M_c)
rank_M_c = np.linalg.matrix_rank(M_c)
if rank_M_c == n:
    print("\nこのシステムは可制御です")
    ctrl_flg = 1
else:
    print("\nこのシステムは不可制御です")
    ctrl_flg = 0

print("\n(step3) 可観測性を判定します")
M_o = np.zeros((n*r,n))
M_o[0:r,0:n+1] = C
for i in range(0,n):
    C_prev = M_o[i*r:(i+1*r),0:n+1]
    M_o[(i+1)*r:(i+2)*r,0:n+1] = np.dot(C_prev,A)
print("\n可観測行列：\n",M_o)
rank_M_o = np.linalg.matrix_rank(M_o)
if rank_M_o == n:
    print("\nこのシステムは可観測です")
    obsv_flg = 1
else:
    print("\nこのシステムは不可観測です")
    obsv_flg = 0

coefs = np.poly(lmd)
coefs_rev = coefs[::-1]

L = np.zeros((n,n))
for i in range(0,n):
    L[:n-i,i] = coefs_rev[i+1:n+1]
    L[n-i-1,i] = 1.0

def cd_trans(A,B,C,T):
    '''座標変換を行う関数'''
    T_inv = np.linalg.inv(T)
    A_t = np.dot(T,np.dot(A,T_inv))
    B_t = np.dot(T,B)
    C_t = np.dot(C,T_inv)
    return A_t,B_t,C_t

def feedback(f):
    
    pass

def observer(g):
    pass

if ctrl_flg == 1:
    print("\n(step4) 可制御正準形を求めます")
    T_c = np.linalg.inv(np.dot(M_c,L))
    print("T_c=\n",np.round(T_c,2))
    A_c,B_c,C_c = cd_trans(A,B,C,T_c)
    print("A_c=\n",np.round(A_c,2),"\nB_c=\n",np.round(B_c,2),"\nC_c=\n",np.round(C_c,2))

if obsv_flg == 1:
    print("\n(step4) 可観測正準形を求めます")
    T_o = np.dot(L,M_o)
    print("T_o\n",np.round(T_o,2))
    A_o,B_o,C_o = cd_trans(A,B,C,T_o)
    print("A_o=\n",np.round(A_o,2),"\nB_o=\n",np.round(B_o,2),"\nC_o=\n",np.round(C_o,2))

