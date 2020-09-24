# coding = utf-8

from PyQt5.QtGui import QImage,qRed,qGreen,qBlue,qRgba,qAlpha,QColor

def getPixel(x,y,pixels,w):
    i = (x + (y * w)) * 4
    return pixels[i:i + 3]

def setPixel(x,y,pixels,w,newColor):
    i = (x + (y * w)) * 4
    return s[:i] + newColor + s[i + 3:]

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




def adjustBright(image:QImage,value) -> QImage:
    width, height = image.width(), image.height()
    newImage = QImage(width,height,QImage.Format_RGBA8888)
    for h in range(height):
        for w in range(width):
            pixel = QColor(image.pixel(h,w))
            red = (pixel.red() + value)
            red = 0x00 if red < 0x00 else 0xff if red > 0xff else red
            green = (pixel.green() + value)
            green = 0x00 if green < 0x00 else 0xff if green > 0xff else green
            blue = (pixel.blue() + value)
            blue = 0x00 if blue < 0x00 else 0xff if blue > 0xff else blue
            newImage.setPixel(h,w,qRgba(red, green, blue, pixel.alpha()))
    return newImage