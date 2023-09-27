import tensorflow as tf
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from skimage.morphology import label

# IMG_WIDTH = 1280
# IMG_HEIGHT = 1280
IMG_WIDTH = 512
IMG_HEIGHT = 512
IMG_CHANNELS = 3

# TEST_PATH = 'test/'
#
# test_ids = next(os.walk(TEST_PATH))[-1]
# print(type(test_ids))
# print(next(os.walk(TEST_PATH)))

#
# good mans
__author__ = "Sreenivas Bhattiprolu"
__license__ = "Feel free to copy, I appreciate if you acknowledge Python for Microscopists"

# Credits https://github.com/bnsreenu/python_for_microscopists

"""
@author: Sreenivas Bhattiprolu
"""

# a_test = sys.argv


class PicPrediction:

    __init_flag = False
    model = tf.keras.models.load_model('ML_model_save_512.h5')


    def __init__(self, test_picture):
        self.test_picture = test_picture


    def prediction_prepare(self):
        test_pic = resize(self.test_picture, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
        # test_pic = resize(self.test_picture, (IMG_HEIGHT, IMG_WIDTH))
        # test_pic = [r.astype(int) for r in test_pic]
        # cv2.imshow('test_picture', test_pic)
        # plt.figure(figsize=(15, 15))
        # plt.imshow(test_pic)
        # plt.axis('off')
        # plt.show()

        sample_image = test_pic
        # prediction = model.predict(sample_image[tf.newaxis, ...])[0]
        prediction = PicPrediction.model.predict(sample_image[tf.newaxis, ...])[0]
        predicted_mask = (prediction > 0.5).astype(np.uint8)
        # predicted_mask = cv2.cvtColor(predicted_mask, cv2.COLOR_BGR2RGB)
        # image.save("image.png")
        # plt.imshow(predicted_mask)
        # plt.show()

        image_data = predicted_mask
        # image_data = predicted_mask.reshape((512, 512))
        image_data = (image_data * 255).astype(np.uint8)
        # imsave('mask_1.jpg', predicted_mask)
        # cv2.imwrite('prediction_test_1_mask.png', predicted_mask)
        # plt.savefig('prediction_test_1_mask.png')
        return image_data
    #     self.display([sample_image, predicted_mask])
    #
    # def display(self, display_list):
    #     plt.figure(figsize=(15, 15))
    #     title = ['Input image', 'Predicted mask']
    #     for i in range(len(display_list)):
    #         plt.subplot(1, len(display_list), i+1)
    #         plt.title(title[i])
    #         plt.imshow(array_to_img(display_list[i]))
    #         plt.axis('off')
    #     plt.show()


# model = tf.keras.models.load_model('ML_model_save_2.h5')
# sample_image = a_test
#
# prediction = model.predict(sample_image[tf.newaxis, ...])[0]
# predicted_mask = (prediction > 0.5).astype(np.uint8)
# display([sample_image, predicted_mask])


