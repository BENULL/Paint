# coding = utf-8

from PyQt5.QtGui import QImage,qRed,qGreen,qBlue,qRgba,qAlpha,QColor
import cv2 as cv
import numpy as np
import copy

def bound(low,high,value):
    return low if value < low else high if value > high else value

def getPixel(x,y,pixels,w):
    i = (x + (y * w)) * 4
    return pixels[i:i + 3]

# 油漆桶
def floodFill(image,pos):
    fillPositions = []
    w, h = image.width(), image.height()
    pixels = image.bits().asstring(w * h * 4)
    targetColor = getPixel(pos.x(), pos.y(), pixels, w)

    haveSeen = set()
    queue = [(pos.x(), pos.y())]
    while queue:
        x, y = queue.pop()
        if getPixel(x, y,pixels,w) == targetColor:
            fillPositions.append((x,y))
            queue.extend(getCardinalPoints(haveSeen, (x, y),w,h))
    return fillPositions


def getCardinalPoints(haveSeen, centerPos,w,h):
    points = []
    cx, cy = centerPos
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        xx, yy = cx + x, cy + y
        if (xx >= 0 and xx < w and yy >= 0 and yy < h and (xx, yy) not in haveSeen):
            points.append((xx, yy))
            haveSeen.add((xx, yy))
    return points



# 调整亮度
def adjustBright(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width,height,QImage.Format_RGBA8888)
    for h in range(height):
        for w in range(width):
            pixel = QColor(image.pixel(h,w))
            red = (pixel.red() + value)
            red = bound(0,255,red)
            green = (pixel.green() + value)
            green = bound(0, 255, green)
            blue = (pixel.blue() + value)
            blue = bound(0,255,blue)
            newImage.setPixel(h,w,qRgba(red, green, blue, pixel.alpha()))
    return newImage

# 调整暖色调
def adjustWarm(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    for h in range(height):
        for w in range(width):
            pixel = QColor(image.pixel(h, w))
            red, green, blue = pixel.red(), pixel.green(), pixel.blue()
            if value >=0 :
                red += value
                red = bound(0,255,red)
                green += value
                green = bound(0,255,green)
            else:
                blue += abs(value)
                blue = bound(0,255,blue)
            newImage.setPixel(h, w, qRgba(red, green, blue, pixel.alpha()))
    return newImage

# 调整饱和度
def adjustSaturation(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    for h in range(height):
        for w in range(width):
            pixel = QColor(image.pixel(h, w)).toHsl()
            H = pixel.hue()
            S = pixel.saturation() + value
            L = pixel.lightness()
            S = bound(0,255,S)
            pixel.setHsl(H, S, L);
            newImage.setPixel(h, w, qRgba(pixel.red(), pixel.green(), pixel.blue(), pixel.alpha()))
    return newImage

# 调整对比度
def adjustContrast(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width, height, QImage.Format_RGBA8888)
    if value >= 0:
        value = 1 / (1 - value / 100.0) - 1
    else:
        value /= 100.0
    for h in range(height):
        for w in range(width):
            pixel = QColor(image.pixel(h, w))
            color = [bound(0,255,(c - 127) * value + c) for c in [pixel.red(), pixel.green(), pixel.blue()]]
            newImage.setPixel(h, w, qRgba(*color, pixel.alpha()))
    return newImage


def QImageToCvMat(incomingImage):
    incomingImage = incomingImage.convertToFormat(QImage.Format_RGBA8888)
    width = incomingImage.width()
    height = incomingImage.height()
    ptr = incomingImage.bits()
    ptr.setsize(height * width * 4)
    arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
    return arr

def CvMatToQImage(cvMat):
    if len(cvMat.shape) == 2:
        # 灰度图是单通道，所以需要用Format_Indexed8
        rows, columns = cvMat.shape
        bytesPerLine = columns
        return QImage(cvMat.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
    else:
        rows, columns, channels = cvMat.shape
        bytesPerLine = channels * columns
        return QImage(cvMat.data, columns, rows, bytesPerLine, QImage.Format_RGBA8888)

def blur(image:QImage):
    src = QImageToCvMat(image)
    blurImg = cv.GaussianBlur(src, (0, 0), sigmaX=15)
    return CvMatToQImage(blurImg)

def sharpen(image:QImage):
    src = QImageToCvMat(image)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    dst = cv.filter2D(src, -1, kernel)

    # blurImg = cv.GaussianBlur(src, (0, 0), 5)
    # usm = cv.addWeighted(src, 1.5, blurImg, -0.5, 0)
    return CvMatToQImage(dst)

def canny(image:QImage):
    blurred = cv.GaussianBlur(QImageToCvMat(image), (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150)
    return CvMatToQImage(edges)

def gray(image:QImage):
    src = QImageToCvMat(image)
    gray = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
    return CvMatToQImage(gray)

def binaryzation(image:QImage):
    src = QImageToCvMat(image)
    gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    ret,thresh1 = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    return CvMatToQImage(thresh1)

def invert(image:QImage):
    src = QImageToCvMat(image)
    # res = cv.bitwise_not(src)
    res = src.copy()
    if len(src.shape) == 2:
        rows, columns = src.shape
        for row in range(rows):
            for col in range(columns):
                res[row, col] = (255 - src[row, col])
    else:
        rows, columns, channels = src.shape
        for row in range(rows):
            for col in range(columns):
                res[row, col] = (255 - src[row, col][0], 255 - src[row, col][1], 255 - src[row, col][2],src[row, col][3])
    return CvMatToQImage(res)

def emboss(image:QImage):
    src = QImageToCvMat(image)
    kernel = np.array([[-2, -1, 0],
                       [-1, 1, 1],
                       [0, 1, 2]])
    dst = cv.filter2D(src, -1, kernel)
    return CvMatToQImage(dst)



