from lxml import etree
from selenium import webdriver
from openpyxl import Workbook


def res(string):
    string1 = string[2:]
    string2 = string1[:-2]
    return string2


def Getinfo(zf_url_list):
    zp_url1 = zf_url_list

    browser.get(str(zp_url1))
    info_html = browser.page_source
    ele = etree.HTML(info_html)

    title = str(ele.xpath('/html/body/div[5]/div[1]/h1/text()'))[::-1]
    area = ""
    flag = 0
    for i in range(2,len(title)):
        if title[i] != ' ':
            flag = 1
            area += title[i]

        else:
            if flag == 1:
                break
    area = area[::-1]





    # q = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div//ul/li//text()')
    # print(q)
    # print(q[1])

    # es = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]//ul/li//text()')
    # print(es)

    # t1 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[1]//text()')
    # t2 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[2]//text()')
    # t3 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[3]//text()')
    # t4 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[4]//text()')
    # t5 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[5]//text()')
    # t6 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[6]//text()')
    # t7 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[7]//text()')
    # t8 = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[8]//text()')
    # print(t1[1])
    # print(t2[1])
    # print(t3[1])
    # print(t4[1])
    # print(t5[1])
    # print(t6[1])
    # print(t7[1])
    # print(t8[1])
    #
    # y1 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p[1]/text()')
    # y2 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div/p[1]/text()')
    # y3 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[1]/text()')
    # y4 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[2]/text()')
    # y5 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[3]/text()')
    # y6 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[4]/text()')
    # y7 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[5]/text()')
    # print(y1[0])
    # print(y2[0])
    # print(y3[0])
    # print(y4[0])
    # print(y5[0])
    # print(y6[0])
    # print(y7[0])

    # line_work = [y1[0], y2[0], y3[0], y4[0], y5[0], y6[0], y7[0], t1[1], t2[1], t3[1], t4[1], t5[1], t6[1], t7[1], t8[1]]



if __name__ == '__main__':
    browser = webdriver.Chrome()
    url = 'https://tj.5i5j.com/leased/44855037.html'
    Getinfo(url)
    line_1 = ['价格', '签约日期', '楼层', '朝向', '年代', '商圈', '装修', '小区均价', '建筑面积', '建筑年代', '总户数', '绿化率', '容积率', '所在商圈', '小区物业']

    # browser.close()