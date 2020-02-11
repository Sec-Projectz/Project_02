from PIL import Image
import Steganography as st
import cv2


img1=cv2.imread('img1.jpg',1)
img2=cv2.imread('img2.jpg',1)
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

output_image=st.merge(img1,img2)
cv2.imwrite('result/merged_image.png',output_image)





