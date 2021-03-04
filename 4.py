from lxml import etree
from selenium import webdriver
from openpyxl import Workbook
line_1 = ['价格','支付方式','几室几厅','楼层','面积','装修','朝向','建筑年代','小区：','楼型：','出租方式：','看房时间：','区域：',
          '地铁：','洗衣机','冰箱','电视','空调','热水器','天然气','暖气','床','网络','衣柜',
          '房源亮点','户型介绍','交通出行','周边配套','小区信息','交通','生活','品质','医疗','运动','物业']
def res(string, a=2 , b=2):
    string1 = string[a:]
    string2 = string1[:-b]
    # print(string2)
    return string2


def Getinfo(zf_url_list, wb):
    zp_url1 = zf_url_list

    browser.get(str(zp_url1))
    info_html = browser.page_source
    ele = etree.HTML(info_html)
    wb_bj = wb

    line_work = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
                 '','']

    y = ['','','','','','','','']

    # 价格
    y[0] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p/span[1]/text()')))
    # 支付方式
    y[1] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p/span[2]/text()[2]')),2,3)
    # 几室几厅
    y[2] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div/p[1]/text()')),74,30)
    # 楼层
    y[3] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div/p[2]/text()')))
    # 面积
    y[4] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[2]/div/p[1]/text()')))
    # 装修
    y[5] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[2]/div/p[2]/text()')))
    # 朝向
    y[6] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div/p[1]/text()')))
    # 建筑年代
    y[7] = res(str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div/p[2]/text()')))

    for i in range(0,8):
        line_work[i] = y[i]

    s1 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]//ul/li//text()')
    # print(s1)
    for j in range(0, len(s1)):
        for k in range(8, 14):
            if s1[j] == line_1[k]:
                line_work[k] = s1[j+1]
                j += 1

    s2 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/ul//li/span/@class')
    for i in range(0,10):
        if s2[i][-2] == '-':
            line_work[i+14] = "无"
        else:
            line_work[i + 14] = "有"



    s3 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[2]/div/ul//li//text()')


    for i in range(0, int(len(s3)/2)):
        line_work[i+24] = s3[2*i + 1]

    k1 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[5]/div[2]/div/div/div[1]//p/text()')
    # print(s1)
    jt = ''
    for tmp in k1:
        jt += tmp
    line_work[29] = jt

    k2 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[5]/div[2]/div/div/div[2]//p/text()')
    sh = ''
    for tmp in k2:
        sh += tmp
    line_work[30] = sh

    k3 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[5]/div[2]/div/div/div[3]//p/text()')
    pz = ''
    for tmp in k3:
        pz += tmp
    line_work[31] = pz

    k4 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[5]/div[2]/div/div/div[4]//p/text()')
    yl = ''
    for tmp in k4:
        yl += tmp
    line_work[32] = yl

    k5 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[5]/div[2]/div/div/div[5]//p/text()')
    yd = ''
    for tmp in k5:
        yd += tmp
    line_work[33] = yd

    wy = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[6]/div/div/ul//li//text()')
    for i in range(0, len(wy)):
        if wy[i] == '物业':
            line_work[34] = wy[i+1]

    ws_bj.append(line_work)
    wb_bj.save(file)





if __name__ == '__main__':

    file = 'C:\\Users\\LEGION\\Desktop\\3.xlsx'
    # C:\Users\Richard\Desktop
    # C:\Users\LEGION\Desktop
    wb_bj = Workbook()
    ws_bj = wb_bj.worksheets[0]
    ws_bj.title = '租房广告页面'

    ws_bj.append(line_1)
    wb_bj.save(file)


    zf_url_list = []


    browser = webdriver.Chrome()
    pags = int(input('需要几页?'))
    for i in range(1,pags+1):
        url = 'https://tj.5i5j.com/zufang/n{}/'
        fullurl = url.format(str(i))

        zf_url_list.append(fullurl)

    count = 0
    for urlt in zf_url_list:
        # url ：目录页
        browser.get(urlt)
        zp_info_html = browser.page_source
        zp_ele = etree.HTML(zp_info_html)

        for num in range(1, 30):#1,30
            url1 = str(zp_ele.xpath('/html/body/div[6]/div[1]/div[2]/ul/li[' + str(num) + ']/div[2]/h3/a/@href '))
            # /html/body/div[6]/div[1]/div[2]/ul/li[1]/div[2]/h3/a
            url2 = url1[2:]
            url3 = url2[:-2]
            url4 = 'https://tj.5i5j.com'+url3
            # print(url4)
            Getinfo(url4, wb_bj)
            count += 1
            print(count)
            # print(num)
        # Getinfo(zf_url_list, wb_bj)
        # print("*")


    browser.close()



# if __name__ == '__main__':
#     browser = webdriver.Chrome()
#     url = 'https://tj.5i5j.com/zufang/45004187.html'
#     Getinfo(url)
#
#     browser.close()

