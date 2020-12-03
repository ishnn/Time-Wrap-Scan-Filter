import cv2
import os

cap = cv2.VideoCapture(1) #calling webcam

for i in range(1,121):

    ret, frame = cap.read() #reading image

    img = cv2.resize(frame,(640,480))# resizing image

    y=(i-1)*4
    crop_img = img[y:y+4, 0:0+640]

    cv2.imwrite('./images/'+str(i)+'.png', crop_img)

    if i==2:
        img1 = cv2.imread('./images/'+str(i-1)+'.png')
        img2 = cv2.imread('./images/'+str(i)+'.png')
        v_img = cv2.vconcat([img1, img2])
        cv2.imwrite('./images/temp.png', v_img)
    if i==1:
        pass
    else:
        img1 = cv2.imread('./images/temp.png')
        img2 = cv2.imread('./images/'+str(i)+'.png')
        v_img = cv2.vconcat([img1, img2])
        cv2.imwrite('./images/temp.png', v_img)
    try:
      y2=480-((i-1)*4)
      y1 = 480-y2

      img = img[y1:y2+y1, 0:0+640]

      img1 = cv2.imread('./images/temp.png')
      img2 = cv2.imread('./line.png')
      v_img2 = cv2.vconcat([img1, img2])

      v_img3 = cv2.vconcat([v_img2, img])

      cv2.imshow('time wrap', v_img3)

    except:
      pass
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        pass

for i in range(1,121):
  os.remove('./images/'+str(i)+'.png')
  
  
lt = os.listdir('./images')
n = 0
for i in lt:
  i = i.split('.')
  if 'image' in i and 'png' in i:
    n=int(i[1])
name = './images/image.'+str(n+1)+'.png'
os.rename('./images/temp.png',name)
