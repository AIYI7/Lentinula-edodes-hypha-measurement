# import sys
#
# import tensorflow as tf
# import os
# import random
# import numpy as np
#
# import cv2
# from skimage.io import imread, imshow, imsave
# from skimage.transform import resize
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from skimage.morphology import label
#
# # from zipfile import ZipFile
# # from keras_preprocessing.image import img_to_array
# from keras_preprocessing.image import array_to_img
# from keras.callbacks import ModelCheckpoint
#
# IMG_HEIGHT = 512
# IMG_WIDTH = 512
# test_pic_path = r'C:\Users\AIYI_may\Desktop\come_more\section-2\ML\software\test\1\1.jpg'
#
# test_picture = cv2.imread(test_pic_path)
# test_pic = resize(test_picture, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
# # print(type(test_pic[1][1][1]))
# #
# # test_pic = [r.astype(int) for r in test_pic]
#
# # cv2.imshow('test_picture', array_to_img(test_pic))
# # cv2.waitKey(0)
#
# test_pic = test_pic.astype(np.uint8)
# test_pic = cv2.cvtColor(test_pic, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(15, 15))
# plt.imshow(array_to_img(test_pic, dtype=np.float64))
# # plt.imshow(test_pic)
# plt.axis('off')
# plt.show()
#
# # a = [1,2,3,4,5,6,7,8,9,0]
# #
# # # python 的列表自带迭代功能可依次接受可迭代对象并组成列表
# # b = [p for p in a if p < 5]
# #
# # print(b)



# from PySide2.QtCore import Qt, QEasingCurve, QPropertyAnimation
# from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.stacked_widget = QStackedWidget()
#
#         for i in range(3):
#             widget = QWidget()
#             layout = QVBoxLayout()
#             label = QLabel(f"Page {i+1}")
#             layout.addWidget(label)
#             widget.setLayout(layout)
#             self.stacked_widget.addWidget(widget)
#
#         self.setCentralWidget(self.stacked_widget)
#         self.show_next_page()
#
#     def show_next_page(self):
#         current_index = self.stacked_widget.currentIndex()
#         next_index = (current_index + 1) % self.stacked_widget.count()
#
#         current_widget = self.stacked_widget.widget(current_index)
#         next_widget = self.stacked_widget.widget(next_index)
#
#         animation_out = QPropertyAnimation(current_widget, b"windowOpacity")
#         animation_out.setDuration(500)
#         animation_out.setStartValue(1.0)
#         animation_out.setEndValue(0.0)
#         animation_out.setEasingCurve(QEasingCurve.InQuad)
#
#         animation_in = QPropertyAnimation(next_widget, b"windowOpacity")
#         animation_in.setDuration(500)
#         animation_in.setStartValue(0.0)
#         animation_in.setEndValue(1.0)
#         animation_in.setEasingCurve(QEasingCurve.OutQuad)
#
#         animation_out.finished.connect(lambda: self.stacked_widget.setCurrentIndex(next_index))
#
#         animation_out.start()
#         animation_in.start()
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()


for i in range(10):
    print(i)