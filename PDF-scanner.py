import img2pdf
from PIL import Image
import cv2
from fpdf import FPDF
import os
print("Press p to choose image from disc.")
print("Press v to connect camera.")
k = input("Press a button and hit enter:")
if k == "p":
 img_path = input("Enter image path:")
 pdf_path = input("Enter path for pdf:")
 image = Image.open(img_path)
 pdf_b = img2pdf.convert(image.filename)
 file = open(pdf_path, "wb")
 file.write(pdf_b)
 file.close()
 print("Your pdf has been saved")
elif k == "v":
 url = 'http://192.168.29.39:8080/video'
 cap = cv2.VideoCapture(url)
 ret = True
 f1 = 0
 i = 0
 path = "D://sayan//scan//img"
 doc = input("Enter pdf name:")
 doc = "D://sayan//output//" + doc
 while ret:
 ret, frame = cap.read()
 if f1 == 0:
 print("Press s to scan the document")
 f1 = f1 + 1
 frame = cv2.resize(frame, (585, 780),
interpolation=cv2.INTER_AREA)
 cv2.imshow("camera feed", frame)
 k = cv2.waitKey(1)
 if k == ord("s"):
 cv2.destroyWindow("camera feed")
 cv2.imshow("scanned photo", frame)
 print("Press u if unreadable")
 print("Press b to convert into B&W") 
 print("Press o to keep the original scan")
 print("Press h to get HSV image")
 print("Press g to detect edges")
 print("Press n to reduce noise")
 print("Press d to delete the scan")
 print("Press q to finish scanning")
 k = cv2.waitKey(0)
 if k == ord("u"):
 cv2.destroyWindow('scanned photo')
 gray = cv2.cvtColor(frame,
cv2.COLOR_BGR2GRAY)
 th = cv2.adaptiveThreshold(gray, 255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,
1)
 cv2.imwrite(path + "%d.jpg" % i, th)
 i = i + 1
 continue
 elif k == ord("b"):
 cv2.destroyWindow('scanned photo')
 gray = cv2.cvtColor(frame,
cv2.COLOR_BGR2GRAY)
 cv2.imwrite(path + "%d.jpg" % i, gray)
 i = i + 1
 continue
 elif k == ord("o"):
 cv2.destroyWindow('scanned photo')
 cv2.imwrite(path + "%d.jpg" % i, frame)
 i = i + 1
 continue
 elif k == ord("h"):
 cv2.destroyWindow('scanned photo')
 hue = cv2.cvtColor(frame,
cv2.COLOR_BGR2HSV)
 cv2.imwrite(path + "%d.jpg" % i, hue)
 i = i + 1
 continue
 elif k == ord("g"):
 cv2.destroyWindow('scanned photo')
 cann_img = cv2.Canny(frame, 150, 255)
 cv2.imwrite(path + "%d.jpg" % i,
cann_img)
 i = i + 1
 continue
 elif k == ord("n"):
 cv2.destroyWindow('scanned photo') 
 blurr = cv2.GaussianBlur(frame, (9, 9),
0, 0)
 cv2.imwrite(path + "%d.jpg" % i, blurr)
 i = i + 1
 continue
 elif k == ord("d"):
 cv2.destroyWindow('scanned photo')
 i = i + 1
 continue
 if k == ord("q"):
 ret = False
 break
 cv2.destroyAllWindows()
 imagelist = os.listdir("D://sayan//scan")
 pdf = FPDF()
 FPDF.set_margins(pdf, 2, 10, 1)
 for image in imagelist:
 image = "D://sayan//scan//" + image
 pdf.add_page()
 pdf.image(image)
 pdf.output(doc + ".pdf", "F")
 print("your pdf has been saved")
