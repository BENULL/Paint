# PyQt5 画图板

## 主要技术

- PyQt5
- qtDesigner
- openCV

## 主要功能

- 绘画
  - 画笔
  - 油漆桶
  - 直线
  - 矩形
  - 椭圆
  - 橡皮擦
- 图片处理
  - 旋转、翻转
  - 亮度、饱和度、对比度、色调调节
  - 灰度化
  - 二值化
  - 反相（反色）
  - 浮雕
  - 边缘检测
  - 模糊
  - 锐化

## 详细代码

[github仓库](https://github.com/BENULL/Paint)

## 实现过程遇到的问题

### 在pycharm上使用qtDesigner

配置qtDesigner

配置UIC

参考 [Mac下pycharm+qtdesigner环境搭建](https://blog.csdn.net/u013667527/article/details/97657621)

### 绘图时图像不能留存或重影问题

采取双缓冲绘图方法

我们再添加一个辅助画布，如果正在绘图，也就是鼠标按键还没有释放的时候，就在这个辅助画布上绘图，只有当鼠标按键释放的时候，才在真正的画布上绘图

参考[2D绘图（八）双缓冲绘图](http://shouce.jb51.net/qt-beginning/22.html)



### 油漆桶Flood Fill算法问题

泛洪算法—Flood Fill，用于确定连接到多维数组中给定节点的区域。

基本原理就是从一个像素点出发，以此向周边的像素点扩充着色，直到图形的边界。

实现方法包括传统递归方式dfs、bfs和描绘线算法(Scanline Fill)等

在QImage上实现效率很低，因为getPixel操作很慢，可以进一步优化

```python
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
```



参考[Implementing QPainter flood fill in PyQt5/PySide](https://www.learnpyqt.com/blog/implementing-qpainter-flood-fill-pyqt5pyside/)

[图像分割经典算法--《泛洪算法》（Flood Fill)](https://www.pianshen.com/article/172962944/)

### Mac上pyqt5 与 cv库冲突问题

问题`You might be loading **two sets of Qt binaries** into the same process`

删除原有的opencv       

`pip3 uninstall opencv-python`

安装opencv–headless版本

`pip3 install opencv-contrib-python-headless`

参考[Mac下使用opencv与pyqt发生冲突](https://blog.csdn.net/qq_43444349/article/details/106602543)

### pyqt QImage 与opencv MAT格式转化问题

在使用opencv过程中需要传入QImage对象进行处理

QImage转化成opencv下的 MAT(numpy ndarray) 对象

```python
def CvMatToQImage(cvMat):
    if len(cvMat.shape) == 2:
        rows, columns = cvMat.shape
        bytesPerLine = columns
        return QImage(cvMat.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
    else:
        rows, columns, channels = cvMat.shape
        bytesPerLine = channels * columns
        return QImage(cvMat.data, columns, rows, bytesPerLine, QImage.Format_RGBA8888)
```

MAT(numpy ndarray) 转QImage

```python
def QImageToCvMat(incomingImage):
    incomingImage = incomingImage.convertToFormat(QImage.Format_RGBA8888)
    width = incomingImage.width()
    height = incomingImage.height()
    ptr = incomingImage.bits()
    ptr.setsize(height * width * 4)
    arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
    return arr
```

参考[Python 中如何将 Pyqt5 下的 QImage 对象转换成 PIL image 或 opencv MAT (numpy ndarray) 对象](https://blog.csdn.net/lch551218/article/details/104882183/)

## 效果预览

### 绘画


![](https://github.com/BENULL/Resource/raw/master/paint1.png)


### 油漆桶效果

![](https://github.com/BENULL/Resource/raw/master/paint2.png)

### 图像处理部分展示

### 原图

![](https://github.com/BENULL/Resource/raw/master/paint3.png)

### 亮度调节

![](https://github.com/BENULL/Resource/raw/master/paint4.png)

### 色调调节

![](https://github.com/BENULL/Resource/raw/master/paint5.png)



### 反相

![](https://github.com/BENULL/Resource/raw/master/paint56png.png)



### 灰度化

![](https://github.com/BENULL/Resource/raw/master/paint8png.png)

### 二值化

![](https://github.com/BENULL/Resource/raw/master/paint9.png)

### 边缘检测

![](https://github.com/BENULL/Resource/raw/master/paint10.png)


## 部分参考

[https://www.cnblogs.com/lfri/p/10599420.html](https://www.cnblogs.com/lfri/p/10599420.html)

[https://blog.csdn.net/qq_43444349/article/details/106602543](https://blog.csdn.net/qq_43444349/article/details/106602543)

[https://www.pianshen.com/article/172962944/](https://www.pianshen.com/article/172962944/)

[https://blog.csdn.net/lzwarhang/article/details/93209166](https://blog.csdn.net/lzwarhang/article/details/93209166)

## 联系
EMAIL ltobenull@163.com

QQ 327137362