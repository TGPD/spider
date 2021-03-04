from lxml import etree
from selenium import webdriver
from openpyxl import Workbook


def res(string):
    string1 = string[2:]
    string2 = string1[:-2]
    return string2

line_1 = ['价格', '签约日期', '楼层：', '朝向：', '年代：', '商圈：', '装修：', '小区均价', '建筑面积', '建筑年代', '总户数', '绿化率', '容积率', '所在商圈', '小区物业', '该住房面积']








def Getinfo(zf_url_list, wb):
    zp_url1 = zf_url_list

    browser.get(str(zp_url1))
    info_html = browser.page_source
    ele = etree.HTML(info_html)
    wb_bj = wb


    title = str(ele.xpath('/html/body/div[5]/div[1]/h1/text()'))[::-1]
    y1 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p[1]/text()')
    y2 = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div/p[1]/text()')


    line_work = [y1[0], y2[0], '', '', '', '', '', '', '', '', '', '', '', '', '']

    es = ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]//ul/li//text()')
    for j in range(0, len(es)):
        for k in range(2, 7):
            if es[j] == line_1[k]:
                line_work[k] = es[j+1]
                j += 1

    qs = ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div//ul/li//text()')

    for n in range(0, len(qs)):
        for m in range(7, 15):
            if qs[n] == line_1[m]:
                line_work[m] = qs[n+1]
                n += 1


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
    line_work.append(area)





    ws_bj.append(line_work)
    wb_bj.save(file)



if __name__ == '__main__':

    file = 'C:\\Users\\LEGION\\Desktop\\2.xlsx'
    # C:\Users\Richard\Desktop
    # C:\Users\LEGION\Desktop
    wb_bj = Workbook()
    ws_bj = wb_bj.worksheets[0]
    ws_bj.title = '房源信息表'

    ws_bj.append(line_1)
    wb_bj.save(file)


    zf_url_list = []


    browser = webdriver.Chrome()
    pags = int(input('需要几页?'))
    for i in range(1,pags+1):
        url = 'https://tj.5i5j.com/leaseds/n{}/'
        fullurl = url.format(str(i))

        zf_url_list.append(fullurl)

    # print(zf_url_list)

    for urlt in zf_url_list:
        # url ：目录页
        browser.get(urlt)
        zp_info_html = browser.page_source
        zp_ele = etree.HTML(zp_info_html)

        for num in range(1, 30):#1,30
            url1 = str(zp_ele.xpath('/html/body/div[6]/div[1]/ul/li[' + str(num) + ']/a/@href '))
            url2 = url1[2:]
            url3 = url2[:-2]
            url4 = 'https://tj.5i5j.com'+url3
            # print(url4)
            Getinfo(url4, wb_bj)
            print(num)
        # Getinfo(zf_url_list, wb_bj)
        # print("*")


    browser.close()

