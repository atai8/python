# -*- coding:utf-8 -*-
import urllib2
import os

# 打开URL，返回HTML信息
def open_url(url):
    # 根据当前URL创建请求包
    req = urllib2.Request(url)
    # 添加头信息，伪装成浏览器访问
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    # 发起请求
    response = urllib2.urlopen(req)
    # 返回请求到的HTML信息
    return response.read()

# 查找当前页面所有图片的URL
def find_imgs(url):
    # 请求网页
    html=open_url(url).decode('utf-8')
    img_addrs=[]
    # 找图片
    a = html.find('data-img=')
    #不带停，如果没找到则退出循环
    while a != -1:
        # 以a的位置为起点，找以jpg结尾的图片
        b = html.find('.jpg',a, a+55)
        # 如果找到就添加到图片列表中
        if b != -1:
            img_addrs.append(html[a+10:b+4])
        # 否则偏移下标
        else:
            b=a+10
        # 继续找
        a=html.find('data-img=',b)
    return img_addrs

# 保存图片
def save_imgs(img_addrs):
    for each in img_addrs:
        print('download image:%s'%each)
        filename=each.split('/')[-2]+".jpg"
        with open(filename,'wb') as f:
            img=open_url("http://www.niwaka.com"+each)
            f.write(img)

# 下载图片测试
# folder 文件夹前缀名
# pages 爬多少页的资源，默认只爬10页
def download_imgs(folder='niwaka'):
    # folder+= str(time.time())
    # 创建文件夹
    # os.mkdir(folder)
    # 将脚本的工作环境移动到创建的文件夹下
    os.chdir(folder)

    # 本次脚本要爬的网站
    url='http://www.niwaka.com/bridal/niwaka/wedding/'
    # 获得当前页面的页码
    # 爬完当前页面下所有图片
    img_addrs=find_imgs(url)
    # 将爬到的页面保存起来
    save_imgs(img_addrs)

if __name__ == '__main__':
    download_imgs()
