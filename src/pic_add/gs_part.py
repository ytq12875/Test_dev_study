#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 下午22:18
# @Author  : ytq
# @FileName: gs_part.py
# @Software: PyCharm


from PIL import Image, ImageFilter


class MyGaussianBlur(ImageFilter.Filter):

    def __init__(self, radius, bounds):
        self.radius = radius
        self.bounds = bounds

    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)


class PicDeal:

    def __init__(self, file, new_file):
        self.image = Image.open(file)
        self.new_file = new_file

    def __save_pic(self):
        self.image.save(self.new_file)

    def my_gaussian_blur(self, radius=2, bounds=None):
        '''
        :param radius: 处理的模糊度
        :param bounds: 处理的范围(left, upper, right, lower)，不传则全图
        :return:  None
        '''
        self.image = self.image.filter(MyGaussianBlur(radius, bounds))
        self.__save_pic()

    def pic_rotate(self,angle):
        self.image = self.image.rotate(angle)
        self.__save_pic()

if __name__ == '__main__':
    bounds = (120, 200, 450, 270)
    deal = PicDeal("1.png", "11.png")
    # deal.my_gaussian_blur(radius=15,bounds=bounds)
    deal.pic_rotate(1)