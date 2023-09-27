import cv2
import os
import time
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QWidget, QMainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QPixmap, QImage
from PySide2 import QtCore, QtGui, QtWidgets


# import matplotlib.pyplot as plt
# from PySide2.QtCore import QFile

# prediction = 1

class Stats(QWidget):
    n_pic = 0
    imgPath = []

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义

        # # 连接动态UI组件
        # tfile = QFile('UI/application1.ui')
        # # 读取动态UI
        # tfile.open(QFile.ReadOnly)
        # tfile.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # 或者一步定义已有的UI组件
        # __init__内写上哪些是一开始就处于激活状态的功能组件

        # 这一步已经是定义了一个新窗口（自带所有已设计的组件）
        # 注意引用函数和连接指定函数的区别，function()表已经调用了方法并给出返回值（或没有），function函数名则用于调用了/连接了函数
        self.test_n = 0

        self.ui = QUiLoader().load('UI/application1.ui')
        # window = QMainWindow()
        # window.setCentralWidget(self.ui.stackedWidget_main)
        ''' 查看组件下的所有控件'''
        # for child in self.ui.stackedWidget_main.widget(1).children():
        #     print(child.objectName())
        '''按钮组'''
        # 总控按钮
        self.pushButton_a_predict = self.ui.pushButton_a_predict
        self.pushButton_a_predict.clicked.connect(lambda: self.Control_stackedWidget_main(1))  ###/// 注意connect后需要连接函数，而非函数的返回值

        self.pushButton_a_help = self.ui.pushButton_a_help
        self.pushButton_a_help.clicked.connect(lambda: self.Control_stackedWidget_main(2))

        # 子页面1按钮
        self.Button_ceshitupian = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QPushButton,
                                                                                 "Button_ceshitupian")
        self.Button_ceshitupian.clicked.connect(self.testpic_load)
        self.Button_tupianchuli = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QPushButton,
                                                                                 "Button_tupianchuli")
        self.Button_tupianchuli.clicked.connect(self.testpic_chuli)
        self.Button_front = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QPushButton, "Button_front")
        self.Button_front.clicked.connect(self.front_pic)
        self.Button_next = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QPushButton, "Button_next")
        self.Button_next.clicked.connect(self.next_pic)
        self.ScrollBar_pic = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QScrollBar, "ScrollBar_pic")
        self.ScrollBar_pic.valueChanged.connect(self.pic_scrollbar)
        '''文字信息'''
        self.label_terminal = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QLabel, "label_terminal")
        '''图片展示'''
        self.label_2 = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QLabel, "label_2")
        self.label_1 = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QLabel, "label_1")
        # 监听页面的改变
        # self.ui.stackedWidget_stat.currentChanged.connect(self.pic_stat_pageChanged)
        self.n_button_stat = 0
        self.pushButton_show_pic_stat = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QPushButton,
                                                                                       "pushButton_show_pic_stat")
        self.pushButton_show_pic_stat.setText('统计结果')
        self.pushButton_show_pic_stat.clicked.connect(self.pic_stat_pageChanged)
        '''页面设置'''
        self.ui.stackedWidget_main.setCurrentIndex(0)
        ## 页面动画渐隐
        self.animation = None
        self.Button_test = self.ui.stackedWidget_main.widget(1).findChild(QtWidgets.QPushButton, "Button_test")
        self.Button_test.clicked.connect(self.Widge_opacity)
        self.stackedWidget_stat = self.ui.stackedWidget_main.widget(1).findChild(
            QtWidgets.QStackedWidget, "stackedWidget_stat"
        )

        # 传入图片，使用matplot
        # img = plt.imread(r'C:\Users\AIYI_may\Desktop\come_more\section-2\ML\software\test')
        # x = img.shape[1]  # 获取图像大小
        # y = img.shape[0]

    def Control_stackedWidget_main(self, n):
        print(n)
        self.ui.stackedWidget_main.setCurrentIndex(n)

    def Widge_opacity(self):
        # for i in range(10):
        #     # time.sleep(0.2)
        #     h = "QWidget\n{\nbackground-color:rgb(85, 255, 255, number)\n}".replace('number', str(255-i*25.5))
        #     self.ui.stackedWidget_stat.widget(self.n_button_stat).setStyleSheet(h)
        #     self.update()
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.stackedWidget_stat.widget(self.n_button_stat).setGraphicsEffect(
            self.opacity_effect)
        self.opacity = 1.0  # 初始透明度
        self.opacity_step = -0.1  # 透明度变化的步长
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_opacity)
        self.timer.start(150)  # 定时器每秒触发一次

    def update_opacity(self):
        self.opacity += self.opacity_step

        # 限制透明度的范围在 0.0 到 1.0 之间
        self.opacity = max(0.0, min(1.0, self.opacity))

        # 设置 QGraphicsOpacityEffect 的透明度
        self.opacity_effect.setOpacity(self.opacity)

        if self.opacity <= 0.0 or self.opacity >= 1.0:
            # 当透明度达到 0.0 或 1.0 时停止定时器
            self.timer.stop()

    def testpic_load(self):
        print('200')

        Stats.n_pic = 0
        # QMessageBox.about(self.ui, '正在预测菌丝生长', '这里将使用进度条表现')
        Stats.imgPath, imgType = QFileDialog.getOpenFileNames(self.ui, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if len(Stats.imgPath) > 1:
            self.label_terminal.setText(' 这是第1张图片,' +
                                        '总计有{}张图片'.format(str(len(Stats.imgPath))))
            jpg = QPixmap(Stats.imgPath[0]).scaled(self.label_2.size(),
                                                   aspectMode=QtCore.Qt.IgnoreAspectRatio)
            self.label_2.setPixmap(jpg)
            self.ScrollBar_pic.setMinimum(0)
            self.ScrollBar_pic.setMaximum(len(stats.imgPath) - 1)
        else:
            self.label_terminal.setText(' 这是第1张图片,' +
                                        '总计有{}张图片'.format(str(len(Stats.imgPath))))
            jpg = QPixmap(Stats.imgPath[0]).scaled(self.label_2.size(),
                                                   aspectMode=QtCore.Qt.IgnoreAspectRatio)
            self.label_2.setPixmap(jpg)
            self.ScrollBar_pic.setMinimum(0)
            self.ScrollBar_pic.setMaximum(0)

    def testpic_chuli(self):
        import prediction
        test_picture = cv2.imread(stats.imgPath[stats.n_pic])
        # QMessageBox.about(self.ui,
        #                   '正在预加载模型',
        #                   f'''第一次加载模型较慢，请耐心等待'''
        #                   )

        # QMessageBox.information(self.ui,
        #                   '正在预加载模型',
        #                   f'''第一次加载模型较慢，请耐心等待''',
        #                    QMessageBox.Ok)

        pic_prediction = prediction.PicPrediction(test_picture)
        pre_mask = pic_prediction.prediction_prepare()
        cv2.imwrite("image{}.jpg".format(str(stats.n_pic)), pre_mask)
        pixmap_yuce = QPixmap("image{}.jpg".format(str(stats.n_pic))).scaled(self.label_1.size(),
                                                                             aspectMode=QtCore.Qt.IgnoreAspectRatio)
        self.label_1.setPixmap(pixmap_yuce)
        if os.path.exists("image{}.jpg".format(str(stats.n_pic))):
            # 删除图像文件
            os.remove("image{}.jpg".format(str(stats.n_pic)))
        else:
            print("图像文件不存在")
        # print(type(pre_mask))
        # jpg = QImage(pre_mask).scaled(self.ui.label_2.size(), aspectMode=QtCore.Qt.IgnoreAspectRatio)
        # pre_mask = cv2.cvtColor(pre_mask, cv2.COLOR_BGR2RGB)
        # pre_mask = QImage(pre_mask.data, pre_mask.shape[1], pre_mask.shape[0], QImage.Format_ARGB32)
        # print(pre_mask.shape[0], pre_mask.shape[1])
        # pre_mask = QImage(pre_mask.data, pre_mask.shape[1], pre_mask.shape[0])

        # self.ui.label_1.setPixmap(QPixmap.fromImage(pre_mask))
        # self.ui.label_1.setScaledContents(True)
        # print(type(test_picture))
        # cv2.imshow('test_picture', test_picture)
        # prediction.PicPrediction.predicrion_prepare(test_picture)
        pass

    def front_pic(self):
        print('front')
        if Stats.n_pic - 1 < 0:
            QMessageBox.about(self.ui,
                              'warning',
                              f'''It's the first picture'''
                              )
        else:
            Stats.n_pic -= 1
            pre_pic = QPixmap(Stats.imgPath[Stats.n_pic]).scaled(self.label_2.size(),
                                                                 aspectMode=QtCore.Qt.IgnoreAspectRatio)
            self.label_2.setPixmap(pre_pic)

    def next_pic(self):
        print('next')
        if Stats.n_pic + 1 > (len(Stats.imgPath) - 1):
            QMessageBox.about(self.ui,
                              'warning',
                              f'''It's the last picture'''
                              )
        else:
            Stats.n_pic += 1
            pre_pic = QPixmap(Stats.imgPath[Stats.n_pic]).scaled(self.label_2.size(),
                                                                 aspectMode=QtCore.Qt.IgnoreAspectRatio)
            self.label_2.setPixmap(pre_pic)

    def pic_scrollbar(self):
        ''''''
        # print(self.ui.ScrollBar_pic.value())
        stats.n_pic = self.ScrollBar_pic.value()
        self.label_terminal.setText(' 这是第{}张图片,'.format(str(stats.n_pic + 1)) +
                                    '总计有{}张图片'.format(str(len(Stats.imgPath))))
        pre_pic = QPixmap(Stats.imgPath[self.ScrollBar_pic.value()]).scaled(
            self.label_2.size(), aspectMode=QtCore.Qt.IgnoreAspectRatio
        )
        self.label_2.setPixmap(pre_pic)

    def pic_stat_pageChanged(self):
        # 修改按钮名称
        # self.s = Stats()
        if self.n_button_stat == 0:

            self.pushButton_show_pic_stat.setText('图片预测')
            # self.s.startAnimation(1.0, 0.0, 1000)
            self.n_button_stat = 1
            # self.test_n += 1
            # self.ui.label_s_2.setText(str(self.test_n))
        else:
            self.ui.stackedWidget_main.widget(1).pushButton_show_pic_stat.setText('统计结果')
            # self.ui.stackedWidget_stat.setCurrentIndex(0)
            # self.s.startAnimation(0.0, 1.0, 300)

            # self.test_n += 1
            # self.ui.label_s_2.setText(str(self.test_n))
            self.n_button_stat = 0

        print(self.n_button_stat)
        # QMessageBox.information(self.ui,
        #                   '正在预加载模型',
        #                   f'''第一次加载模型较慢，请耐心等待''',
        #                    QMessageBox.Ok)


# 显然self仅限于同一类中，（子类，父类之中呢？）
# class app:
#     def __init__(self):
#         self.q = 0


app = QApplication([])
# 创建一个顶层窗口供额外引入   但他和UI界面是什么关系？为什么UI界面不需要这条语句
# MainWindow = QMainWindow()
stats = Stats()
stats.ui.show()
app.exec_()
