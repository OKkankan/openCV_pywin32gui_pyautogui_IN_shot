import pyautogui as pg
import time
import cv2
######!!!!!!!!!!!!!!做识别样本的图片尽量截取类似正方形，方便坐标定位
class click_one_time:
    def get_xy(image_modle_path):
        pg.screenshot().save(r'C:\Users\15536\Desktop\111\screenshot.png')
        img = cv2.imread(r'C:\Users\15536\Desktop\111\screenshot.png')#读取屏幕截图
        img_terminal = cv2.imread(image_modle_path)
        height, weight, channel = img_terminal.shape#读取标准图的xy
        result = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED)#匹配截图与标准图
        upper_left = cv2.minMaxLoc(result)[2]
        lower_right = (upper_left[0]+height,upper_left[1]+weight)
        avg = (int((upper_left[0]+lower_right[0]))/2,int((upper_left[1]+lower_right[1])/2))
        print(avg)
        return avg
    def auto_click(var_avg,button):
        pg.click(var_avg[0],var_avg[1],button=f'{button}')
        time.sleep(1)
    def routine(image,name,button):
        result_1 = click_one_time.get_xy(image)
        click_one_time.auto_click(result_1,button)
        print(f'正在点击:{name}')
click_one_time.routine(r"C:\Users\15536\Desktop\image_modle\a097ba2b-d485-4c1b-860b-1727e5424cc0.png",'开始游戏','left')
time.sleep(5)

