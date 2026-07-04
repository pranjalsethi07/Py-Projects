#read img
# instance text detector
#detect text on img
#drag box and test


# Check installed Python versions:
# py -0p

# deactivate
# Remove-Item -Recurse -Force .venv
# py -3.10 -m venv .venv
# .\.venv\Scripts\Activate.ps1
# python --version
# python -m pip install --upgrade pip
# pip install easyocr==1.6.2

# for wrong package installation
# python -m pip uninstall opencv-python-headless

import cv2
import easyocr
import matplotlib.pyplot as plt

# read image
img_path="./3.png"
img=cv2.imread(img_path)


#instance text detector
reader=easyocr.Reader(['en'],gpu=False)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  #essentially, this is to increase the size of the image, so that more text can be detected. If the image is too small, some text may not be detected. So, we are increasing the size of the image by 2 times in both x and y direction. by this we dont have to change the original image, we can just resize it and use it for text detection. This is especially useful for images with small text, as increasing the size of the image will make the text more readable and easier to detect. However, this will also increase the processing time, so we need to find a balance between image size and processing time. We can also use other interpolation methods like INTER_LINEAR or INTER_NEAREST, but INTER_CUBIC is generally better for enlarging images.Also ab threshold ki value zada rkh payenge, resize k bina threshold 0.15 rkhna padta tha, but now we can keep it 0.25 or 0.3, as the text is more clear and readable after resizing the image. So, we can keep the threshold value higher, which will give us more accurate results.

#detect txt on img
text_ = reader.readtext(img, text_threshold=0.4, low_text=0.2, mag_ratio=2) #in this line, we are using the readtext function of easyocr to detect text in the image. The parameters used are:
# text_threshold: This is the threshold for text detection. It is a value between 0 and 1, where 0 means no text will be detected and 1 means all text will be detected. A low threshold means you are accepting OCR results with lower confidence. In your script, threshold = 0.15 means EasyOCR can keep text it is only 15% confident about. More text will be detected, including faint or blurry text, but you will also get more false positives or wrong labels. So the tradeoff is: lower threshold = more detections, less accuracy; higher threshold = fewer detections, more accuracy.low_text: This is the threshold for low text detection. It is a value between 0 and 1, where 0 means no low text will be detected and 1 means all low text will be detected. A low threshold means you are accepting OCR results with lower confidence. In your script, low_text = 0.2 means EasyOCR can keep text it is only 20% confident about. More text will be detected, including faint or blurry text, but you will also get more false positives or wrong labels. So the tradeoff is: lower threshold = more detections, less accuracy; higher threshold = fewer detections, more accuracy.and mag_ratio: This is the magnification ratio for text detection. It is a value between 0 and 1, where 0 means no magnification and 1 means full magnification. A low magnification ratio means you are accepting OCR results with lower confidence. In your script, mag_ratio = 2 means EasyOCR can keep text it is only 2% confident about. More text will be detected, including faint or blurry text, but you will also get more false positives or wrong labels. So the tradeoff is: lower magnification ratio = more detections, less accuracy; higher magnification ratio = fewer detections, more accuracy.

threshold=0.25
#text_=reader.readtext(img)
#threshold=0.15 #ideally this should be set to 0.5, but for the sake of this demo, I set it to 0.15, or like to atleat 70-80% of the text to be detected, so that we can see the effect of filtering out low confidence results
#ye 0.25 mei 3rd img k bottom se text nhi aa rha tha,,so 0.15 rkha

#A low threshold means you are accepting OCR results with lower confidence.

# In your script, threshold = 0.15 meaans

# EasyOCR can keep text it is only 15% confident about
# more text will be detected, including faint or blurry text
# but you will also get more false positives or wrong labels
# So the tradeoff is:

# lower threshold = more detections, less accuracy
# higher threshold = fewer detections, more accuracy


#draw bbox and text
for t in text_:
    print(t)
    bbox,text,score=t
    
    if score>threshold:   #this is to filter out low confidence results,like blurry text or false positives in the background of the img
        cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),4)
        cv2.putText(img,text,bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0),1, cv2.LINE_AA)
    
#plt.imshow(img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()