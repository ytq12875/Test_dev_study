#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image, text):
    font = ImageFont.truetype('C:\Windows\Fonts\simhei.ttf', 36)

    # 添加背景
    new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # 添加水印
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(0, rgba_image.size[0], font_len*40+100):
        for j in range(0, rgba_image.size[1], 200):
            image_draw.text((i, j), text, font=font, fill=(255, 255, 255, 50))
    text_overlay = text_overlay.rotate(-45)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    # 裁切图片
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text


if __name__ == '__main__':
    # print("打开图片：")
    # img = Image.open("test.png")
    # print("转换图片，并打上水印：")
    # im_after = add_text_to_image(img, u'仅用于测试认证')
    # print("保存图片：")
    # im_after.save(u'test1.png')
    # a = 2 + 2j


    def func(x):
        lis = x.strip().split('.')
        li = [bin(int(i)) for i in lis]
        print(li)
        li2 = [i.replace('0b', (10 - len(i)) * '0') for i in li]
        print(li2)
        return int(''.join(li2), 2)
    ret = func('19.168.200.100')
    print(ret)