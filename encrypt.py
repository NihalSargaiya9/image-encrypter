from PIL import Image
import numpy as np


def imagenameWithoutExtention(imagename):
    return imagename.split('.')[0]

def encrypt(imagename):
    img = Image.open(imagename)
    data = np.array(img)
    myHash =  np.random.random_integers(0,255,(data.shape))
    np.savetxt(imagenameWithoutExtention(imagename)+'.enc', myHash.flatten(), delimiter=',',fmt="%d")
    toWrite=(data-myHash)
    tata = Image.fromarray((toWrite.astype('uint8')))
    tata.show()
    tata.save(imagenameWithoutExtention(imagename)+".png")


def decrypt(imagename):
    img = Image.open(imagenameWithoutExtention(imagename)+'.png')
    data = np.array(img)
    myHash=np.loadtxt(imagenameWithoutExtention(imagename)+".enc").reshape(data.shape)
    tata = Image.fromarray(((data+myHash).astype('uint8')))
    return tata

imagename= input("enter image name with extention: ")

encrypt(imagename)
decrypt(imagename).show()

