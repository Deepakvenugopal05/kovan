
from PIL import Image

img = Image.open("C:\\Users\\deepa\\Pictures\\Saved Pictures\\chair.jpg")
img = img.rotate(angle=90,expand=0,resample=Image.BICUBIC)
w,h = img.size 
print(w,h)
newSize = (10,10)
img.resize((300,300))
img.show()
img.save("C:\\Users\\deepa\\Pictures\\chair1.jpg")
print(img.size)


trans_img = img.transpose(Image.ROTATE_180)
trans_img.show()
img.show()
img.close()
print(img.mode)
print(img.size)
print(img.format)
w,h = img.size
newsize = (300,180)
r_img = img.resize(newsize,resample=Image.NEAREST)
r_img.save("C:\\Users\\deepa\\Pictures\\chair.jpg")
img = Image.open("C:\\Users\\deepa\\Pictures\\chair.jpg")
img.show()

filename = 'C:\\Users\\deepa\\Pictures\\profile.jpg'

with Image.open(filename) as img_file:
    w,h = img_file.size
    # crp_img = img_file.crop((80,85,450,415))
    # print(crp_img.size)
    # print(crp_img.mode)
    print(img_file.size)
    img_file.resize((w//15,h//15))
    print(img_file.size)
    img_file.save('C:\\Users\\deepa\\Pictures\\profile_resol.jpg',quality=50)


import threading,os

# def sum(num):
#     print(num+num,{os.getpid()})
# def mul(num):
#     print(num*num,{os.getpid()})

# if __name__ == "__main__" :
#     t1 = threading.Thread(target=sum,args=(10,))
#     #t2 = threading.Thread(target=mul,args=(10,))
#     mul(10)
#     t1.start()
#     #t2.start()

#     t1.join()
#     #t2.join()
#     print("done")

def print_names():
    print("deepak")

def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

def thread_fact(n):
    print(threading.current_thread().name)
    res = fact(n)
    print(res)

tfact = threading.Thread(target=thread_fact,args=(5,))
tfact.start()
tfact.join()

threads = []
for i in range(5):
    thread = threading.Thread(target=print_names)
    threads.append(thread)
    thread.start()

for i in threads:
    i.join()

'''
'''
#Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50.
def even(lst):
    try:
        global even_lst,odd_lst
        even_lst,odd_lst =[],[]
        for i in lst:
            if i%2==0:
                even_lst.append(i)
            else:
                odd_lst.append(i)
    except Exception as e:
        return e
    return even_lst,odd_lst

def thread_even(lst):
    res = even(lst)
    for i in res:
        print(i)

lst = [i for i in range(30, 51)]

teven = threading.Thread(target=thread_even,args=(lst,))
teven.start()
teven.join()

from threading import Thread
import time

def thread_1():                      
  for i in range(5):
    print('this is thread T')
    time.sleep(5)

T = Thread(target = thread_1) 

T.setDaemon(True)                   
T.start()                           
time.sleep(10)
print('this is Main Thread')  

import schedule,time

def dowork():
    print('This is work')
    return schedule.CancelJob
def go():
    print('go home')

schedule.every(17:00).do(dowork)

while True:
    schedule.run_pending()
    time.sleep(1)

