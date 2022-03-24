# nilai = float(input('Input nilai mahasiswa:'))
# if nilai >= 80:
#     grade = 'A'
# elif nilai >= 70 and nilai < 80 :
#     grade = 'B'
# elif nilai >= 60 and nilai < 70 :
#     grade='C'
# elif nilai >= 40 and nilai < 60 :
#     grade='D'
# else: 
#     grade='E'

# print(f"Anda mendapatkan  {grade}")

# scores = [90,80,70,60,75,85]
# total_scores = 0

# for x in scores:
#     total_scores += x
    
# average = total_scores/len(scores)

# print('Total nilai\t=',total_scores)
# print('Rata-rata nilai\t=',average)

# jumlah = 0
# banyak = 0
# while True:
#     try:
#         user = float(input("masukkan nilai yg diinginkan: "))
#         if user == 0:
#             break
#         else:
#             banyak+=1
#         jumlah+=user
#     except:
#         print("masukkan kudu angka kawann!!!")            
        
# print(f"""jumlah nilai adalah {jumlah} 
# dengan banyak {banyak} """)
# print(f"rata-rata : {jumlah/banyak} ")


import statistics as st
import numpy as np

# a = [1,1,2,2,3,3,4,4,5,50]
# b = [1,1,2,2,3,3,4,4,5,5]

# print(st.mean(a))
# print(st.median(a))
# print(st.mean(b))
# print(st.median(b))

# print("")

# c = [60,70,70,70,80,80,80,80,90,100]
# d = [75,75,75,75,80,80,80,80,80,80]

# print(st.mean(c))
# print(st.median(c))
# print(max(c) - min(c))
# print(np.var(c))
# print(np.std(c))
# print("")
# print(st.mean(d))
# print(st.median(d))
# print(max(d) - min(d))
# print(np.var(d,ddof=1))
# print(np.std(d,ddof=1))

def lowercase(text):
    text = text.lower().split()
    print(text)

lowercase("Indonesia")
lowercase("INDONESIA")
lowercase("anda Gila")