#By：Bend Function
# 视频地址：https://www.bilibili.com/video/av36835920/
from selenium import webdriver
import pyautogui as pag
import sys
import webbrowser
import time
from selenium.webdriver.firefox.options import Options

browser = webdriver.Firefox()
start = time.time()

def click(url):
    sys.path.append("libs")
    webbrowser.open(url)
    webbrowser.get()
    time.sleep(5)           # 可能要改延迟时间
    for _ in range(0, 10):
        time.sleep(0.1)
        pag.click(1537, 817, button="left")  # 点5下 可能要改坐标
    pag.keyDown('ctrlleft')
    pag.press("w")
    pag.keyUp('ctrlleft')


def find(word):
    start = word.rfind("http://live.bilibili.com")         # 先找到网站的位置
    box = word[int(start):int(start+35)]
    end = box.find("?")
    url = box[0:end]
    return url

if __name__ == '__main__':
    count = 0
    cv2.imshow("1", aa)

    browser.get("https://live.bilibili.com/2734746")
    print('success')

    brfore_url = ""
    while True:
        time.sleep(2)
        url = find(browser.page_source)
        if url != brfore_url:
            count += 1

            print(count)
            click(url)
        brfore_url = url

# 1 打开一个空直播间，，
# 2 持续读网页 selenium
# 3 识别到哪里可以抽奖
# 4 打开一个新浏览器到那个房间
# 5 点击~~

