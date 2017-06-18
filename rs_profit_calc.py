import urllib2
import os

os.system('cls' if os.name == 'nt' else 'clear')

buyItems = []
buyItemsAmount = []
sellItems = []
sellItemsAmount = []
url = 'https://www.ge-tracker.com/item/'
topSplit = '<td id="item_stat_offer_price">'
bottomSplit = '</td>'

print '--Profit calculator--\n'


def getPrice(url):
    try:
        sourceCode = urllib2.urlopen(url).read()
        sourceSplit = sourceCode.split(topSplit)[1].split(bottomSplit)[0]
        if 'span' in sourceSplit:
            return sourceSplit.split('ago">')[1].split('</span>')[0].replace('\n', '').replace(' ', '').replace(',', '')
        else:
            return sourceSplit.replace('\n', '').replace(' ', '').replace(',', '')
    except Exception, e:
        return


def addItems(buyOrSell):
    if (buyOrSell == 'buy'):
        item = raw_input('Which item do you want to buy?: ')
        amount = raw_input('How many do you want to buy?: ')
        if (getPrice(url + item.replace(' ', '-').replace('\'', '-').replace('(', '').replace(')', '')) == None):
            print '\nItem not found, please try again\n'
            addItems('buy')
        else:
            buyItems.append(url + item.replace(' ', '-').replace('\'', '-').replace('(', '').replace(')', ''))
            buyItemsAmount.append(int(amount))
            repeat = raw_input('\nDo you want to buy another item? (y/n): ')
            if (repeat == 'y'):
                addItems('buy')
            else:
                return
    elif (buyOrSell == 'sell'):
        item = raw_input('Which item do you want to sell?: ')
        amount = raw_input('How many do you want to sell?: ')
        if (getPrice(url + item.replace(' ', '-').replace('\'', '-').replace('(', '').replace(')', '')) == None):
            print '\nItem not found, please try again\n'
            addItems('sell')
        else:
            sellItems.append(url + item.replace(' ', '-').replace('\'', '-').replace('(', '').replace(')', ''))
            sellItemsAmount.append(int(amount))
            repeat = raw_input('\nDo you want to sell another item? (y/n): ')
            if (repeat == 'y'):
                addItems('sell')
            else:
                return


def calculateProfit():
    buyTotal = 0
    sellTotal = 0
    extraCosts = 0
    anyExtra = raw_input('\nAre there any extra costs? (y/n): ')
    if (anyExtra == 'y'):
        extraCosts = int(raw_input('How much are the extra costs?: '))
    for x in range(0, len(buyItems)):
        buyTotal += int(getPrice(buyItems[x])) * buyItemsAmount[x]
    for x in range(0, len(sellItems)):
        sellTotal += int(getPrice(sellItems[x])) * sellItemsAmount[x]
    print '\n-----------------------PROFIT-----------------------'
    return sellTotal - buyTotal - extraCosts


print '-----------------------BUY-----------------------'
addItems('buy')
print '\n-----------------------SELL-----------------------'
addItems('sell')
print 'Your profit is: ' + str(calculateProfit())