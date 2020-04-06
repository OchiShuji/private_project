import numpy as np
import random
from matplotlib import pyplot as plt 
from matplotlib import animation

print('''
sorting algorism visualization 

Creation Date:2020/03/14
       Author:ShujiOchi
     Language:Python
''')

flg = int(input("<アルゴリズムを選択>\n0:bubble  1:selection  2:insertion  3:merge  4:quick  5:count  6:cocktail  7:bogo\n>>"))
dflt_n = [30,30,30,100,100,100,30,5]
dflt_interval = [10,10,10,50,50,50,10,50]
n = input("<barの数を入力>\n>>")
n = dflt_n[flg] if n == "" else int(n)
interval = input("<intervalを入力>(単位：[ms])\n>>")
interval = dflt_interval[flg] if interval == "" else int(interval)

x = np.arange(n)
y = x + np.ones(n)
x,y = list(x),list(y)
yr = random.sample(y,len(y))
imgs = []
fig = plt.figure()

#Bubble sort
def bubble(lst):
    for i in range(0,len(lst)-1):
        for j in range(0,len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            img = plt.bar(x,lst,color="black")
            imgs.append(img)

#Selection sort
def selection(lst):
    for i in range(0,len(lst)-1):
        m = i
        for j in range(i+1,len(lst)):
            if lst[m] > lst[j]:
                m = j
            img = plt.bar(x,lst,color="black")
            imgs.append(img)
        lst[i],lst[m] = lst[m],lst[i]
    img = plt.bar(x,lst,color="black")
    imgs.append(img)

#Insertion sort                      
def insertion(lst):
    for i in range(1,len(lst)):
        j = i
        while j > 0:
            if lst[j] < lst[j-1]:
                lst[j],lst[j-1] = lst[j-1],lst[j]
                img = plt.bar(x,lst,color="black")
                imgs.append(img)
            j = j - 1

#Merge sort
def merge(lst):
    #split
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    l = merge(left)
    r = merge(right)

    #merge
    Z = []
    while (len(l) > 0 and len(r) > 0):
        if l[0] < r[0]:
            Z.append(l[0])
            del l[0]
        else:
            Z.append(r[0])
            del r[0]
    if len(l) > 0:
        Z.extend(l)
    else:
        Z.extend(r)
    
    #for drawing
    inds = []
    for z in Z:
        inds.append(yr.index(z))
    st = min(inds)
    ed = max(inds)
    yr[st:ed+1] = Z[:]
    img = plt.bar(x,yr,color="black")
    imgs.append(img)
    return Z

#Quick sort
def quick(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    right = []
    left  = []
    for i in range(1,len(lst)):
        if lst[i] <= pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])

    #for drawing
    splited = left + [pivot] + right
    ind_pivot = yr.index(pivot)
    yr[ind_pivot:ind_pivot+len(splited)] = splited
    img = plt.bar(x,yr,color="black")
    imgs.append(img)

    #recursion
    r = quick(right)
    l = quick(left)
    Z = l + [pivot] + r
    return Z

#Counting sort
def count(lst):
    c = [0] * (int(len(lst)) + 1)
    for i in range(0,len(lst)):
        val = int(lst[i])
        c[val] = c[val] + 1
    lst_srtd = []
    for i in range(0,len(lst)+1):
        j = 0
        while j < c[i]:
            lst_srtd.append(i)
            Y = lst_srtd + lst[len(lst_srtd):]
            img = plt.bar(x,Y,color="black")
            imgs.append(img)
            j = j + 1

#bogo sort
def bogo(lst):
    def is_sorted(lst):
        for i in range(1,len(lst)):
            if lst[i-1] > lst[i]:
                return False
        return True
    while True:
        random.shuffle(lst)
        print(lst)
        img = plt.bar(x,lst,color="black")
        imgs.append(img)
        if is_sorted(lst):
            break

#cocktail sort
def cocktail(lst):
    n = len(lst)
    top = n - 1
    bottom = 0
    temp = -1
    while bottom < top:
        print(top,bottom)
        for i in range(bottom,top):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                img = plt.bar(x,lst,color="black")
                imgs.append(img)
                temp = i
        top = temp
        for j in range(top,bottom,-1):
            if lst[j-1] > lst[j]:
                lst[j-1],lst[j] = lst[j],lst[j-1]
                img = plt.bar(x,lst,color="black")
                imgs.append(img)
                temp = j
        bottom = temp

#Gravity sort
def gravity(lst):
    def is_sorted(lst):
        for i in range(1,len(lst)):
            if lst[i-1] > lst[i]:
                return False
        return True
    while True:
        for i in range(0,n-1):
            if lst[i] > lst[i+1]:
                d = lst[i] - lst[i+1]
                lst[i+1] = lst[i+1] + d
                lst[i] = lst[i] - d
        img = plt.bar(x,lst,color="black")
        imgs.append(img)    
        if is_sorted(lst):
            break

print("Drawing frames...")

if flg == 0:
    title = "bubble_sort_{}_{}.gif".format(n,interval)
    bubble(yr)
elif flg == 1:
    title = "selection_sort_{}_{}.gif".format(n,interval)
    selection(yr)
elif flg == 2:
    title = "insertion_sort_{}_{}.gif".format(n,interval)
    insertion(yr)
elif flg == 3:
    title = "merge_sort_{}_{}.gif".format(n,interval)
    merge(yr)
elif flg == 4:
    title = "quick_sort_{}_{}.gif".format(n,interval)
    img = plt.bar(x,yr,color="black")
    imgs.append(img)
    quick(yr)
elif flg == 5:
    title = "counting_sort_{}_{}.gif".format(n,interval)
    count(yr)
elif flg == 6:
    title = "cocktail_sort_{}_{}.gif".format(n,interval)
    cocktail(yr)
elif flg == 7:
    title = "bogo_sort_{}_{}.gif".format(n,interval)
    bogo(yr)

#animation
print("Constituting the animation...")
anm = animation.ArtistAnimation(fig,imgs,interval=interval,repeat=False) if flg == 7 else animation.ArtistAnimation(fig,imgs,interval=interval,repeat_delay=5000)
#save&show
save_flg = input("Animation is completed. Do you want to save as gif? - y / n \n>>")
if (save_flg == "y" or save_flg == "Y"):
    anm.save(title,writer="imagemagick")
plt.show()

