# -*- coding: utf-8 -*-

"""
# 1. Currency
"""

from Currency.currency import Currency
from Tool.sendMail import Send_Mail
import numpy as np

# -------- Entry of Program ------------------
print u"""#---------------------------------------
#   Program: Crawler of currency
#   Version: 1.0
#   Author: 虫二
#   Date: 2013-05-16
#   Language: Python 2.7
#   Operations: Crawler the currency from the 'union pay'.
#   Functions: get current currency of chf, and email to me if it reaches a threshold
#---------------------------------------
"""

selectCurrency = 'chf'
cc = Currency(selectCurrency, 1, 'current')
twoDaysInfo = cc.get_info()

cc = Currency(selectCurrency, 7, 'current')
oldPeriodInfo = cc.get_info()

# email or not
mail_server = Send_Mail('send_log@yahoo.com', 'send_log@yahoo.com')

old = float(twoDaysInfo[1][0])

if len(twoDaysInfo[1]) == 2:
    current = float(twoDaysInfo[1][1])
else:
    current = old

averageOfOld = np.average([float(x) for x in oldPeriodInfo[1]])

print u'Yesterday\'s currency is {0}'.format(old)
print u'Today\'s currency is {0}'.format(current)

if (current <= old) and (current < 6.5):
    mail_server.send_mail('Currency! Low enough', 'current currency of chf is: ' + str(current) + ' !')
elif (current > old) and (averageOfOld > 6.7):
    mail_server.send_mail('Currency! Be careful', 'current currency of chf is: ' + str(current) + ' ! And the average currency of last week is ' + str(averageOfOld))
elif (current <= 6.4):
    mail_server.send_mail('Currency! Extremely low', 'current currency of chf is: ' + str(current) + ' !')


"""
# 2. System check
"""


