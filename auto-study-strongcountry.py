# _*_ coding: utf-8 _*_
import json
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
HOME_PAGE = 'https://www.xuexi.cn/' 
SCORES_LINK = 'https://pc.xuexi.cn/points/my-points.html'
LOGIN_LINK = 'https://pc.xuexi.cn/points/login.html'

A_L=[
'https://www.xuexi.cn/72ac54163d26d6677a80b8e21a776cfa/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html',
'https://www.xuexi.cn/c06bf4acc7eef6ef0a560328938b5771/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/89acb6d339cd09d5aaf0c2697b6a3278/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/588a4707f9db9606d832e51bfb3cea3b/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/6db80fbc0859e5c06b81fd5d6d618749/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/2e5ffrom selenium.webdriver.common.keys import Keysc9557e56b14ececee0174deac67f/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/682fd2c2ee5b0fa149e0ff11f8f13cea/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/13e9b085b05a257ed25359b0a7b869ff/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/9ca612f28c9f86ad87d5daa34c588e00/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/d05cad69216e688d304bb91ef3aac4c6/9a3668c13f6e303932b5e0e100fc248b.html',
'https://www.xuexi.cn/7097477a9643eacffe4cc101e4906fdb/9a3668c13f6e303932b5e0e100fc248b.html'
]
V_L=[
'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5',
'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1koo357ronk-5',
'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1742g60067k-5'
]
ARTICLES_LINK =random.choice(A_L)
VIDEO_LINK=random.choice(V_L)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome(executable_path=r'C:\Users\peter\Desktop\chromedriver.exe',options=options)


def login_simulation():
    # 自己扫码登录
    browser.get(LOGIN_LINK)
    browser.maximize_window()  # 窗口最大化
    browser.execute_script("var q=document.documentElement.scrollTop=1000")
    time.sleep(20)
    browser.get(HOME_PAGE)
    print("模拟登录完毕\n")

def read_articles():
    """阅读文章"""
    browser.get(ARTICLES_LINK)
    time.sleep(5)
    articles = set(browser.find_elements_by_class_name("text")) #获取文章连接,用set函数去重
    print(type(articles))
    print(articles)
    for index,article in enumerate(articles): # 遍历文章连接
        if index > 6: # 点击6个文章链接
            break            
        print(index,article)        
        article.click()
        # browser.get(browser.current_url)  #获取当前窗口连接
        time.sleep(5)
        # browser.close()
        print(browser.current_url)
    all_handles = browser.window_handles #获取当前窗口的句柄
    for handle in all_handles[1:]:
        browser.switch_to.window(handle) #切换到当前窗口
        browser.execute_script("var q=document.documentElement.scrollTop=100000")  # 窗口滑动到底部
        time.sleep(120)
        print(browser.current_url + "阅读完毕")
        browser.close()	
	# browser.switch_to.window(all_handles[-1])  #切换到倒数第一个窗口  
    # browser.execute_script("var q=document.documentElement.scrollTop=100000")  # 窗口滑动到底部
    # time.sleep(20)
    browser.switch_to.window(all_handles[0]) #回到第一个窗口
    # browser.get(HOME_PAGE)
    time.sleep(5)
    print("阅读文章完毕\n")

def watch_videos():
    """观看视频"""
    browser.get(VIDEO_LINK)
    time.sleep(10)
    videos = set(browser.find_elements_by_class_name("textWrapper")) # 获取视频链接，用set函数去重
    print(type(videos))
    print(videos)  
    for i , video in enumerate(videos):  # 遍历视频链接
        if i > 6:  # 点击6个视频链接
            break
        print(i,video)
        video.click()
        print(browser.current_url)
    all_handles = browser.window_handles # 获取当前窗口的句柄
    for handle in all_handles[1:]:  # 对除第一个窗口句柄以外的句柄进行操作
        try:
            browser.switch_to.window(handle) # 切换到当前窗口
            video_duration_str = browser.find_element_by_class_name("duration").get_attribute('innerText')  #获取视频时长的字段内容，几分几秒，这里用find_elements方法会报错
            video_duration = int(video_duration_str.split(':')[0])* 60 + int(video_duration_str.split(':')[1])  # 将时长转换成秒数
            time.sleep(video_duration+5) # 保持窗口到视频时长结束
            print(video_duration)
            print(browser.current_url + '观看完毕')
            browser.close()
        except:
            print("E")
        else:
            continue
    browser.switch_to.window(all_handles[0]) # 回到第一个窗口
    time.sleep(5)
    print("观看视频完毕\n")

	
def get_scores():
    """获取当前积分"""
    browser.get(SCORES_LINK)
    time.sleep(2)
    gross_score = browser.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[2]/div[2]/span[1]")\
        .get_attribute('innerText')
    today_score = browser.find_element_by_xpath("//span[@class='my-points-points']").get_attribute('innerText')
    print("当前总积分：" + str(gross_score))
    print("今日积分：" + str(today_score))
    print("获取积分完毕，即将退出\n")
	
if __name__ == '__main__':
    login_simulation()  # 模拟登录
    read_articles()     # 阅读文章
    time.sleep(5)
    watch_videos()      # 观看视频
    get_scores()        # 获得今日积分
    browser.quit()	

	
