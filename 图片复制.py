def imgCopy(lib1,lib2):
    lib1 = open(lib1,'rb')
    lib2 = open(lib2,'wb')
    lib2.write(lib1.read(200000))
a = r'C:\Users\jay\Desktop\壁纸\59c0ab7859d2b.jpg'
b = r'C:\Users\jay\Desktop\壁纸\59c0-fuzhi.jpg'

if __name__ == '__main__':
    imgCopy(a, b)