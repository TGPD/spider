from lxml import etree
from selenium import webdriver
from openpyxl import Workbook


def res(string):
    string1 = string[2:]
    string2 = string1[:-2]
    return string2









def Getinfo(zf_url_list, wb):
    zp_url1 = zf_url_list

    browser.get(str(zp_url1))
    info_html = browser.page_source
    ele = etree.HTML(info_html)
    wb_bj = wb

    zp_info_num = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p[1]/text()'))
    zp_info_date = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div/p[1]/text()'))
    zp_info_floor = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[1]/text()'))
    zp_info_direction = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[2]/text()'))
    zp_info_construction_time = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[3]/text()'))
    zp_info_business = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[4]/text()'))
    zp_info_fitment = str(ele.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[5]/text()'))


    zp_info_avePrice = str(ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[1]/label/text()'))
    zp_info_numOFhouse = str(ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[3]/text()'))
    zp_info_green = str(ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[4]/text()'))
    zp_info_plot = str(ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[5]/text()'))
    zp_info_property = str(ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[7]/text()'))
    # /html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li[8]


    # zpt = str(ele.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li/a/text()'))
    # '/html/body/div[5]/div[3]/div[3]/div[1]/div/div/ul/li/a/text()'
    # print(zpt)
    # print(zp_info_direction, zp_info_construction_time, zp_info_business, zp_info_fitment, zp_info_avePrice)
    # print(zp_info_numOFhouse, zp_info_green, zp_info_plot, zp_info_property)

    num = res(zp_info_num)
    date = res(zp_info_date)
    floor = res(zp_info_floor)
    dir = res(zp_info_direction)
    con = res(zp_info_construction_time)
    business = res(zp_info_business)
    fitment = res(zp_info_fitment)
    avePrice = res(zp_info_avePrice)
    noh = res(zp_info_numOFhouse)
    green = res(zp_info_green)
    plot = res(zp_info_plot)
    property = res(zp_info_property)

    # if noh[-1] != '年':
    #     return

    print(avePrice, noh, green, plot, property)
    # print(num, '\t\t\t', date, '\t\t\t', floor)
    line_work = [date, num, floor, dir, con, business, fitment, avePrice, noh, green, plot, property]
    ws_bj.append(line_work)
    wb_bj.save(file)



if __name__ == '__main__':

    file = 'C:\\Users\\LEGION\\Desktop\\1.xlsx'
    # C:\Users\Richard\Desktop
    # C:\Users\LEGION\Desktop
    wb_bj = Workbook()
    ws_bj = wb_bj.worksheets[0]
    ws_bj.title = '房源信息表'
    line_1 = ['价格', '签约日期', '楼层', '朝向', '年代', '商圈', '装修', '小区均价', '总户数', '绿化率', '容积率', '小区物业']
    ws_bj.append(line_1)
    wb_bj.save(file)


    zf_url_list = []


    browser = webdriver.Chrome()
    pags = int(input('需要几页?'))
    for i in range(1,pags+1):
        url = 'https://bj.5i5j.com/leaseds/n{}/'
        fullurl = url.format(str(i))

        zf_url_list.append(fullurl)

    print(zf_url_list)

    for urlt in zf_url_list:
        # url ：目录页
        browser.get(urlt)
        zp_info_html = browser.page_source
        zp_ele = etree.HTML(zp_info_html)

        for num in range(1, 30):#1,30
            url1 = str(zp_ele.xpath('/html/body/div[6]/div[1]/ul/li[' + str(num) + ']/a/@href '))
            url2 = url1[2:]
            url3 = url2[:-2]
            url4 = 'https://bj.5i5j.com'+url3
            # print(url4)
            Getinfo(url4, wb_bj)
            # print(num)
        # Getinfo(zf_url_list, wb_bj)
        # print("*")


    browser.close()

