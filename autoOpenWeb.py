#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import mysql.connector
browser = webdriver.Chrome()
browser.get('https://mp.weixin.qq.com/')
#=======================================================
#获取数据库中内容
class GetContent():
    def getContent(self,label):	    
        db = mysql.connector.connect(user="root",password="###",database="###",charset='utf8')	   
        cursor = db.cursor()
        Content = []  		
        sql = "select title from spiderdb.security where sign='%s'" %label  

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:               
                Content.append("".join(row))		
        except:
            print "Error: unable to fetch data1"
        finally:
			title=[]		
			for c in Content:
				title.append(c+'\n')
			return title
 
# ###########################登录微信账号###################
browser.implicitly_wait(2)
#输入微信账号
browser.find_element_by_id("account").send_keys("###")
  
browser.implicitly_wait(2)
#输入密码
browser.find_element_by_id("pwd").send_keys("###")

#单击登陆
browser.find_element_by_id("loginBt").click()
# ############################################################

browser.implicitly_wait(5)    #加个时间延时，修复不能打开素材管理的bug
# ##########发消息###################
browser.find_element_by_xpath("//*[@id='menuBar']/dl[2]/dd[3]/a").click()  #点击素材管理

browser.implicitly_wait(2)
browser.find_element_by_css_selector("#js_main > div.sub_title_bar > a").click()  #单击新建图文消息


#===================转换到弹出的窗口===================
#获取当前的window handle
ch = browser.current_window_handle

#所有的window handles
wh = browser.window_handles
print "0:Title of current page is %s\n"%(browser.title)
print "0:url of current page is %s\n"%(browser.current_url)

#在所有的窗口中查找弹出窗口
for line in wh:
	if line == ch:
		browser.implicitly_wait(8)
		browser.switch_to_window(line)
		print "Handle=",line
		browser.implicitly_wait(8)    # 用此函数代替time.sleep(),因为更加智能，可以在一个时间范围内智能的等待。
		
		print "1:Title of current page is %s\n"%(browser.title)
		print "1:url of current page is %s\n"%(browser.current_url)
		
		browser.implicitly_wait(10)
		#  ###编辑新图文消息
		#browser.find_element_by_class_name("frm_input,js_title,js_counter").send_keys('yjuytututut')
		#browser.find_element_by_xpath("//input[@type='text']").send_keys("title")
		#browser.find_element_by_css_selector('#js_appmsg_editor > div > div.inner > div:nth-child(1) > span > input').send_keys(u"信息安全大小事一览")
		browser.find_element_by_css_selector('#js_appmsg_editor > div > div.inner > div:nth-child(1) > span > input').send_keys(u"信息安全大小事一览")

		
		#=================================================================================
		#从图库选择图片上传
		browser.implicitly_wait(8)
		browser.find_element_by_id("js_imagedialog").click()
		browser.find_element_by_css_selector("body > div.dialog_wrp.img_dialog_wrp.ui-draggable > div > div.dialog_bd > div > div.inner_main > div > div:nth-child(2) > div.img_pick > ul > li:nth-child(3) > label").click()
		#browser.find_element_by_css_selector("body > div.dialog_wrp.img_dialog_wrp.ui-draggable > div > div.dialog_bd > div > div.inner_main > div > div:nth-child(2) > div.img_pick > ul > li:nth-child(1) > label").click()		
		#browser.find_element_by_class_name("js_btn").click()
		browser.find_element_by_css_selector("body > div.dialog_wrp.img_dialog_wrp.ui-draggable > div > div.dialog_ft > span.btn.btn_input.js_btn_p.btn_primary > button").click()
		#=================================================================================
		#填写摘要
		browser.find_element_by_css_selector("#js_appmsg_editor > div > div.inner > div.js_desc_area.appmsg_edit_item.align_counter > span > textarea").send_keys(u"abstract：摘要")

		#================================================================================
		#填写作者
		browser.implicitly_wait(8)
		#browser.find_element_by_class_name("frm_input,js_counter,js_author").send_keys("IT大白")
		browser.find_element_by_css_selector("#js_appmsg_editor > div > div.inner > div:nth-child(2) > span > input").send_keys(u"IT大白")
		#=================================================================================
		#填写正文
		browser.implicitly_wait(8)
		browser.switch_to_frame("ueditor_0")
		#browser.find_element_by_css_selector("body").send_keys(u"contents：内容")
		#按照类别获取标题
		content=GetContent()
		g=content.getContent('g')
		c=content.getContent('c')	
		f=content.getContent('f')
		v=content.getContent('v')
		h=content.getContent('h')
		m=content.getContent('m')	
		s=content.getContent('s')	
		print v
		browser.find_element_by_css_selector("body").send_keys(u"如果您喜欢我们的内容，请点击上面蓝色的“安全张之家”进行关注！更多精彩内容为您播报！"+"\n")
		browser.find_element_by_css_selector("body").send_keys(u"A.国内政策"+"\n")
		if g:
			browser.find_element_by_css_selector("body").send_keys(g)
		browser.find_element_by_css_selector("body").send_keys(u"B.业界新闻-国内"+"\n")
		if c:
			browser.find_element_by_css_selector("body").send_keys(c)
		browser.find_element_by_css_selector("body").send_keys(u"C.业界新闻-国外"+"\n")
		if f:
			browser.find_element_by_css_selector("body").send_keys(f)
		browser.find_element_by_css_selector("body").send_keys(u"D.漏洞补丁"+"\n")
		if v:
			browser.find_element_by_css_selector("body").send_keys(v)
		browser.find_element_by_css_selector("body").send_keys(u"E.病毒木马"+"\n")
		if h:
			browser.find_element_by_css_selector("body").send_keys(h)
		browser.find_element_by_css_selector("body").send_keys(u"F.会议期刊"+"\n")
		if m:
			browser.find_element_by_css_selector("body").send_keys(m)
		browser.find_element_by_css_selector("body").send_keys(u"G.安全小技巧"+"\n")
		browser.find_element_by_css_selector("body").send_keys(s)
		if s:
			browser.find_element_by_css_selector("body").send_keys(u"长按二维码关注“安全张之家”！备注：本版所载内容全部来源于互联网，如有侵权，请联系版主，将立即删除！！")		
		
browser.switch_to_window(browser.window_handles[-1])  #	get the lastest window
print "2:Title of current page is %s\n"%(browser.title)
print "2:url of current page is %s\n"%(browser.current_url)
browser.find_element_by_id("js_submit").click()  #save

	
print browser.title

#browser.quit()
