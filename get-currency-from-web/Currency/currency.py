# -*- coding: utf-8 -*-

# Import package
import urllib
import urllib2
import re
import os
import datetime
from datetime import date

class Currency:
    def __init__(self, selectCurrency, period, folderStatus):
        self.baseURL = 'http://www.kuaiyilicai.com/huilv/d-unionpay-'
        if selectCurrency not in ['chf', 'eur', 'gbp', 'cad', 'usd']:
            self.siteURL = self.baseURL + 'chf.html'
            self.currency = 'chf'
        else:
            self.siteURL = self.baseURL + selectCurrency + '.html'
            self.currency = selectCurrency

        # user agent
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : user_agent  }

        # define time
        dateTo = date.today()
        if period is None:
            dateFrom = dateTo - datetime.timedelta(1)
        else:
            dateFrom = dateTo - datetime.timedelta(period)

        # define request form
        values = {"datefrom": str(dateFrom),"dateto": str(dateTo)}
        self.data = urllib.urlencode(values)
        # Global file variance, the object to write.
        self.file = None
        # Define the status of folder that will have file to write
        self.folder = folderStatus
        # Report status
        print u'爬虫报告: Start ' + self.currency + ' !'
        print u'爬虫报告: The URL: ' + self.siteURL + '\n          The Start Time: ' + str(dateFrom) + '\n          The end Time: ' + str(dateTo)

    def get_page(self):
        request = urllib2.Request(self.siteURL, self.data, self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def get_content(self):
        page = self.get_page()
        pattern = re.compile('<input id="hidChart_sell".*?value="(.*?)" />', re.S)
        items = re.findall(pattern, page)
        new_pattern = re.compile("new Date\('(.*?)'\),(.*?)]", re.S)
        matchedItems = re.findall(new_pattern, items[0])
        contents = [[],[]]
        for item in matchedItems:
            contents[0].append(item[0])
            contents[1].append(item[1])
        return contents

    def mkdir(self, path):
        path = path.strip()
        is_exists = os.path.exists(path)
        if not is_exists:
            print u'爬虫报告: Build folder ', path, 'to store the data!'
            os.makedirs(path)
            return True
        else:
            print u'爬虫报告: Folder:', path, ' already build!'
            return False

    def save_info(self, content):
        path = '/Volumes/DATA/Education/Knowledge/Automation/code/currency/data/' + self.folder + '/' + self.currency
        self.mkdir(path)
        self.file = open(path+ '/' + self.folder + ".txt", "w+")

        print u'爬虫报告: Start writing!'
        try:
            for i in range(len(content[0])):
                self.file.write(content[0][i] + '\t' + content[1][i] + '\n')
        except IOError, e:
            print u'爬虫报告: Writing error!! Reason: ' + e.message
        finally:
            print u'爬虫报告: Finish writing!'

    def start(self):
        content = self.get_content()
        self.save_info(content)

    def get_info(self):
        content = self.get_content()
        # print u'爬虫报告: Current (' + content[0][0] + ') currency of ' + self.currency + ' is ' + content[1][0]
        return content

"""
# -------- Entry of Program ------------------
print u"""#---------------------------------------
#   Program: Crawler of currency
#   Version: 1.0
#   Author: 虫二
#   Date: 2013-05-16
#   Language: Python 2.7
#   Operations: Crawler the currency from the 'union pay'.
#   Functions: We can select which currency and which  period to download
#---------------------------------------
"""

print u"Input which currency that you want:"
selectCurrency = str(raw_input(u'we can select chf, eur, gbp, cad & usd: '))
cc = Currency(selectCurrency, 365, 'history_data')
cc.start()
"""











