from flask import Flask, request
from retrievestockinfo import getStockPrice
from stocks import *

application = Flask(__name__)

def getCompanyName(stock_name):
	return 'test'

def getFiveDaysEndPrice(stock_name):
	return 'test'
	
def ethicalInvesting(money):
	com1 = getCompanyName()
	com2 = getCompanyName()
	com3 = getCompanyName()
	info1 = getFiveDaysEndPrice()
	info2 = getFiveDaysEndPrice()
	info3 = getFiveDaysEndPrice()
	#return json string
	return 'test'
	
def growthInvesting(money):
	com1 = getCompanyName()
	com2 = getCompanyName()
	com3 = getCompanyName()
	info1 = getFiveDaysEndPrice()
	info2 = getFiveDaysEndPrice()
	info3 = getFiveDaysEndPrice()
	#return json string
	return 'test'
	
def indexInvesting(money):
	com1 = getCompanyName()
	com2 = getCompanyName()
	com3 = getCompanyName()
	info1 = getFiveDaysEndPrice()
	info2 = getFiveDaysEndPrice()
	info3 = getFiveDaysEndPrice()
	#return json string
	return 'test'
	
def qualityInvesting(money):
	com1 = getCompanyName()
	com2 = getCompanyName()
	com3 = getCompanyName()
	info1 = getFiveDaysEndPrice()
	info2 = getFiveDaysEndPrice()
	info3 = getFiveDaysEndPrice()
	#return json string
	return 'test'
	
def valueInvesting(money):
	com1 = getCompanyName()
	com2 = getCompanyName()
	com3 = getCompanyName()
	info1 = getFiveDaysEndPrice()
	info2 = getFiveDaysEndPrice()
	info3 = getFiveDaysEndPrice()
	#return json string
	return 'test'

#return json string (if 2 strategies: combine 2 json strings and then return)	
@application.route('/')

#Stocks defined in stocks.py


def test():	

	money = request.args.get('money')
	strategy = request.args.get('strategy')
	
	#return error if money is not given
	if not money:
		return 'The amount of money must be given'
		
	#return error if strategy is not chosen	
	if not strategy:
		return 'Must choose at least 1 strategy'
		
	strategy = strategy.split(',')
	
	#return error if more than 2 strategies are chosen
	if len(strategy) > 2:
		return 'Cannot choose more than 2 strategies'
		
	try:
		money = int(money)
		if money >= 5000:
			#return str(money)
			print strategy
			portfolio_info = []
			remainmon = SuggestinEngine(money, strategy, portfolio_info)
			return str(remainmon)

		else:
			return 'Money has to be at least 5000'
			
	#return error if input money is not an integer
	except ValueError:
		return 'Input (money) is not an integer'

def test2():	
	money = 6000
	strategy = [1,2]

	portfolio_info = []
	remainmon = SuggestinEngine(money, strategy, portfolio_info)
	print remainmon

	for Entry in portfolio_info:
		Entry.printinfo()

	return


def SuggestinEngine(money, strategy, portfolio_info):

	money_per_stgy = money / len(strategy)
	print money_per_stgy

	for stgy in strategy:

		print stgy;
		remain_money = RunStrategy(money_per_stgy, int(stgy), portfolio_info)
		money_per_stgy = (money / len(strategy)) + remain_money

	return remain_money

def RunStrategy(money, strategy, portfolio_info):

	money_per_stock = money / len(strategystocks[strategy])

	for stock in strategystocks[strategy]:

		portfolio_entry = PortfolioStockEntry(stock)
		print stock
		portfolio_entry.stockfullname = getStockPrice(stock, portfolio_entry.price, portfolio_entry.date)

		print money_per_stock
		portfolio_entry.quantity = int(money_per_stock / portfolio_entry.price[-1])

		print portfolio_entry.price[-1]
		print portfolio_entry.quantity

		remain_cash = money_per_stock  - (portfolio_entry.price[-1] * portfolio_entry.quantity)
		money_per_stock = (money / len(strategystocks[strategy])) + remain_cash

		portfolio_entry.strategy = strategy

		#Append the entry into a list
		portfolio_info.append(portfolio_entry)

	return remain_cash


if __name__ == '__main__':
    application.run(host='0.0.0.0',debug = True)
    #test2()

# input  1. money   2. strategy (http://0.0.0.0:5000/?money=3000&strategy=1,2)

# return each stock information (JSON)
# stock name, company name, 5 days end price, 5 days date, quantity, (left money?)