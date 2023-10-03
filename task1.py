import cv2

png_img = cv2.imread('mario.png')

cv2.imwrite('mod.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY),100])