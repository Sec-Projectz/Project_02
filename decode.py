from PIL import Image
import Steganography as st
import cv2

img=cv2.imread('result/merged_image.png',1)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hid_image=st.unmerge(img)
cv2.imwrite('result/secret_image.png',hid_image)

