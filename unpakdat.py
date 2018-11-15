import io,os,struct,glob,codecs,math,re,zlib

src='package.dat'
hsize=os.path.getsize(src)
fl = open(src,'rb')
filename = os.path.basename(src)
if os.path.isdir(filename+'_unpacked') == False:
    os.makedirs(filename+'_unpacked')

k=0
size_list=[]
while fl.tell()<hsize :
    print(k,fl.tell())
    file = open(filename+'_unpacked\\'+str(k)+'.bin','wb')
    size_list=[]
    size,=struct.unpack('<H',fl.read(2))
    while size!=55928 :
        size_list.append(size)
        size,=struct.unpack('<H',fl.read(2))
    fl.seek(-2,1)
    
    for i in range(len(size_list)):
        if k>=3994 :
            print(fl.tell(),size_list[i])
        size,=struct.unpack('<H',fl.read(2))
        fl.seek(-2,1)
        if size!=55928 :
            break
        data = zlib.decompress(fl.read(size_list[i]))
        file.write(data)
    file.close()
    k=k+1
fl.close()

