from gtsrb.model import Gtsrb
import matplotlib.pyplot as plt


class Trainer:

    def __init__(self, dataset):
        gt = Gtsrb()
        self.dataset = dataset

    def execute(self):
        gt = Gtsrb()
        dataset = self.dataset
        print("X 데이터셋".format(dataset.X.shape))
        print("Y 데이터셋".format(dataset.y.shape))

        plt.imshow(
            dataset.Y[0, :, :, :].reshape(gt.RESIZE_IMAGE)
        ) # 표본 이미지
        print("레이블: {}".format(dataset.y[0, :]))

        plt.imshow(dataset.Y[-1, :, :, :].reshape(gt.RESIZE_IMAGE))
        print("레이블: {}".format(dataset.y[-1, :]))

        plt.show()
