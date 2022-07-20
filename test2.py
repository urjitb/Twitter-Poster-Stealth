from PIL import Image 
import os 

path = '/Users/urjitb/Documents/twitimgs/'

i=0
for file in os.listdir(path): 
  

    if(".png" in file):
        print(file)
        try:
            im1 = Image.open(path+file)
        
            rgb_im = im1.convert('RGB')
            rgb_im.save(path+"jpgs/"+str(i)+"tw.jpg")
            
            im1.close()
            i+=1
        except:
            pass
        