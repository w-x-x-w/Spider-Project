#导入相关库
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import choice
#问卷网址
url='https://www.wjx.cn/vj/QRSMwtn.aspx'
#绕过问卷星的智能检测，将webdriver属性设置为undefined，设置其他属性......
option=Options()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)
web=Chrome(options=option)
web.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
#对页面进行请求
web.get(url)
#设置每个题目的选项列表
sex1=['//*[@id="divquestion1"]/ul/li[1]/a','//*[@id="divquestion1"]/ul/li[2]/a']
sex2=['//*[@id="divquestion2"]/ul/li[1]/a','//*[@id="divquestion2"]/ul/li[2]/a','//*[@id="divquestion2"]/ul/li[3]/a']
sex31=['//*[@id="divquestion3"]/table/tbody/tr[1]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[1]/td[2]/a','//*[@id="divquestion3"]/table/tbody/tr[1]/td[3]/a']
sex32=['//*[@id="divquestion3"]/table/tbody/tr[2]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[2]/td[3]/a','//*[@id="divquestion3"]/table/tbody/tr[2]/td[5]/a']
sex33=['//*[@id="divquestion3"]/table/tbody/tr[3]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[3]/td[5]/a']
sex34=['//*[@id="divquestion3"]/table/tbody/tr[4]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[4]/td[5]/a']
sex35=['//*[@id="divquestion3"]/table/tbody/tr[5]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[5]/td[5]/a']
sex36=['//*[@id="divquestion3"]/table/tbody/tr[6]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[6]/td[5]/a']
sex37=['//*[@id="divquestion3"]/table/tbody/tr[7]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[7]/td[5]/a']
sex38=['//*[@id="divquestion3"]/table/tbody/tr[8]/td[1]/a','//*[@id="divquestion3"]/table/tbody/tr[8]/td[5]/a']
sex4=['//*[@id="divquestion4"]/ul/li[1]/a','//*[@id="divquestion4"]/ul/li[2]/a']
sex5=['//*[@id="divquestion5"]/ul/li[2]/a','//*[@id="divquestion5"]/ul/li[1]/a']
sex61=['//*[@id="divquestion6"]/table/tbody/tr[1]/td[1]/a','//*[@id="divquestion6"]/table/tbody/tr[1]/td[2]/a']
sex62=['//*[@id="divquestion6"]/table/tbody/tr[2]/td[1]/a','//*[@id="divquestion6"]/table/tbody/tr[2]/td[3]/a']
sex63=['//*[@id="divquestion6"]/table/tbody/tr[3]/td[1]/a','//*[@id="divquestion6"]/table/tbody/tr[3]/td[4]/a']
sex64=['//*[@id="divquestion6"]/table/tbody/tr[4]/td[1]/a','//*[@id="divquestion6"]/table/tbody/tr[4]/td[5]/a']
sex65=['//*[@id="divquestion6"]/table/tbody/tr[5]/td[1]/a','//*[@id="divquestion6"]/table/tbody/tr[5]/td[2]/a']
sex7=['//*[@id="divquestion7"]/ul/li[1]/a','//*[@id="divquestion7"]/ul/li[2]/a']
sex81=['//*[@id="divquestion8"]/table/tbody/tr[1]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[1]/td[2]/a']
sex82=['//*[@id="divquestion8"]/table/tbody/tr[2]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[2]/td[5]/a']
sex83=['//*[@id="divquestion8"]/table/tbody/tr[3]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[3]/td[2]/a']
sex84=['//*[@id="divquestion8"]/table/tbody/tr[4]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[4]/td[3]/a']
sex85=['//*[@id="divquestion8"]/table/tbody/tr[5]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[5]/td[4]/a']
sex86=['//*[@id="divquestion8"]/table/tbody/tr[6]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[6]/td[3]/a']
sex87=['//*[@id="divquestion8"]/table/tbody/tr[7]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[7]/td[5]/a']
sex88=['//*[@id="divquestion8"]/table/tbody/tr[8]/td[1]/a','//*[@id="divquestion8"]/table/tbody/tr[8]/td[2]/a']
sex91=['//*[@id="divquestion9"]/table/tbody/tr[1]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[1]/td[3]/a']
sex92=['//*[@id="divquestion9"]/table/tbody/tr[2]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[2]/td[2]/a']
sex93=['//*[@id="divquestion9"]/table/tbody/tr[3]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[3]/td[5]/a']
sex94=['//*[@id="divquestion9"]/table/tbody/tr[4]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[4]/td[3]/a']
sex95=['//*[@id="divquestion9"]/table/tbody/tr[5]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[5]/td[2]/a']
sex96=['//*[@id="divquestion9"]/table/tbody/tr[6]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[6]/td[3]/a']
sex97=['//*[@id="divquestion9"]/table/tbody/tr[7]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[7]/td[4]/a']
sex98=['//*[@id="divquestion9"]/table/tbody/tr[8]/td[1]/a','//*[@id="divquestion9"]/table/tbody/tr[8]/td[3]/a']
sex10=['//*[@id="divquestion10"]/ul/li[1]/a','//*[@id="divquestion10"]/ul/li[2]/a']
sex11=['学习','拼命学习']
sex12=['一对一辅导','收费问答','无']
sex13=['www.leecode.com','力扣','giehub','gitee','acwing','bilibili']
#分别对每个题进行随机的，或者有倾向填充
web.find_element_by_xpath(choice(sex1)).click()
web.find_element_by_xpath(choice(sex2)).click()
web.find_element_by_xpath(choice(sex31)).click()
web.find_element_by_xpath(choice(sex32)).click()
web.find_element_by_xpath(choice(sex33)).click()
web.find_element_by_xpath(choice(sex34)).click()
web.find_element_by_xpath(choice(sex35)).click()
web.find_element_by_xpath(choice(sex36)).click()
web.find_element_by_xpath(choice(sex37)).click()
web.find_element_by_xpath(choice(sex38)).click()
web.find_element_by_xpath(choice(sex4)).click()
web.find_element_by_xpath(choice(sex5)).click()
web.find_element_by_xpath(choice(sex61)).click()
web.find_element_by_xpath(choice(sex62)).click()
web.find_element_by_xpath(choice(sex63)).click()
web.find_element_by_xpath(choice(sex64)).click()
web.find_element_by_xpath(choice(sex65)).click()
web.find_element_by_xpath(choice(sex7)).click()
web.find_element_by_xpath(choice(sex81)).click()
web.find_element_by_xpath(choice(sex82)).click()
web.find_element_by_xpath(choice(sex83)).click()
web.find_element_by_xpath(choice(sex84)).click()
web.find_element_by_xpath(choice(sex85)).click()
web.find_element_by_xpath(choice(sex86)).click()
web.find_element_by_xpath(choice(sex87)).click()
web.find_element_by_xpath(choice(sex88)).click()
web.find_element_by_xpath(choice(sex91)).click()
web.find_element_by_xpath(choice(sex92)).click()
web.find_element_by_xpath(choice(sex93)).click()
web.find_element_by_xpath(choice(sex94)).click()
web.find_element_by_xpath(choice(sex95)).click()
web.find_element_by_xpath(choice(sex96)).click()
web.find_element_by_xpath(choice(sex97)).click()
web.find_element_by_xpath(choice(sex98)).click()
web.find_element_by_xpath(choice(sex10)).click()
web.find_element_by_xpath('//*[@id="q11"]').send_keys(choice(sex11))
web.find_element_by_xpath('//*[@id="q12"]').send_keys(choice(sex12))
web.find_element_by_xpath('//*[@id="q13"]').send_keys(choice(sex13))
#点击提交按钮
web.find_element_by_xpath('//*[@id="submit_button"]').click()
sleep(2)
#点击智能验证按钮
web.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/div[2]/button').click()
sleep(2)
web.find_element_by_xpath('//*[@id="SM_BTN_1"]/div[1]/div[4]').click()
sleep(5)
web.quit()