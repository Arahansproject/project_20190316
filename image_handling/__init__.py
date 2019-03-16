from image_handling.service import ImageService
import cv2

if __name__=='__main__':
    image = ImageService('lena.jpg', 'gray')
    image.changeColor()

