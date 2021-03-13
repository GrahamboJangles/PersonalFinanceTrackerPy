# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

#https://pythonprogramming.net/embedding-live-matplotlib-graph-tkinter-gui/?completed=/how-to-embed-matplotlib-graph-tkinter-gui/

import robin_stocks.robinhood as r
login = r.login('', '')

import datetime as dt

from tkinter import *

import pandas as pd

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
try:
	from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
except ImportError:
	from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
style.use("dark_background") # ggplot is default

f = Figure(figsize=(5,5), dpi=100)
#g = Figure(figsize=(5,5), dpi=100)
graph1 = f.add_subplot(111)
#graph2 = f.add_subplot(111)

symbol = ''


def animate(i):
	#pullData = open("sampleText.txt","r").read()
	#dataList = pullData.split('\n')
	
	
	
	import os
	clear = lambda: os.system('cls')
	clear()
	
	total_equity = float(r.account.load_phoenix_account()['total_equity']['amount'])
	print(f'Portfolio balance: ${total_equity:.2f}')
	try: previous_close = float(r.account.load_phoenix_account()['portfolio_previous_close']['amount'])
	except Exception as e: print(f'previous_close error: {e}')
	print(f"Today's profit: ${total_equity - previous_close:.2f}")
	
	#graph_historical_portfolio()
		
	#graph_balance(span='day')
	positions_df()
	graph_balance()
	
	# PageThree()
	#"""Basic test frame for the table"""
	#from pandastable import Table, TableModel
	#def __init__(self, parent=None):
	#self.parent = parent
	#Frame.__init__(self)
	#main = master
	#geometry('600x400+200+100')
	#title('Table app')
	#f = Frame(self.main)
	#f.pack(fill=BOTH,expand=1)
	#df = TableModel.getSampleData()
	#table = pt = Table(f, dataframe=df,
	#					showtoolbar=True, showstatusbar=True)
	#pt.show()
	#return
	
	#__init__()
#class TestApp(Frame):

	# import tkinter as tk

	# import tksheet
	

	# top = tk.Tk()

	# sheet = tksheet.Sheet(top)

	# sheet.grid()

	# sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(1)])

	# # table enable choices listed below:

	# sheet.enable_bindings(("single_select",

							# "row_select",

							# "column_width_resize",

							# "arrowkeys",

							# "right_click_popup_menu",

							# "rc_select",

							# "rc_insert_row",

							# "rc_delete_row",

							# "copy",

							# "cut",

							# "paste",

							# "delete",

							# "undo",

							# "edit_cell"))
							
	#tk.Tk.__init__(self)
	# tksheet.grid_columnconfigure(0, weight = 1)
	# grid_rowconfigure(0, weight = 1)
	# frame = tk.Frame()
	# frame.grid_columnconfigure(0, weight = 1)
	# frame.grid_rowconfigure(0, weight = 1)
	# sheet = Sheet(frame,
						 # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
	# sheet.enable_bindings()
	# frame.grid(row = 0, column = 0, sticky = "nswe")
	# sheet.grid(row = 0, column = 0, sticky = "nswe")

##def positions_df():
##	beta_reference = 'SPY'
## 
##	positions_data = r.get_open_stock_positions()
## 
##	# option_positions_data = r.get_all_option_positions()
##	option_positions_data = r.get_open_option_positions()
##	# print(option_positions_data)
##	## Note: This for loop adds the stock ticker to every order, since Robinhood
##	## does not provide that information in the stock orders.
##	## This process is very slow since it is making a GET request for each order.
## 
##	positions_symbol_list = []
##	positions_qty_list = []
##	positions_average_price = []
##	positions_current_price = []
## 
##	for position in positions_data:
##		"""
##		Maybe use r.build_holdings() instead?
##		"""
##		# print(position)
##		symbol = r.get_symbol_by_url(position['instrument']) 
##		position['symbol'] = symbol
##		positions_symbol_list.append(symbol)
##		positions_qty_list.append(float(position['quantity']))
##		positions_average_price.append(float(position['average_buy_price']))
##		positions_current_price.append(float(r.get_stock_quote_by_symbol(symbol)['last_trade_price']))
## 
##	# print(position_symbol_list, position_qty_list)
##	# input()
##	# df.set_index('position',inplace=False)
## 
##	# item['symbol']
##	# display(position)
##	# input()
##	# symbol = positions_data['chain_symbol']
##	# print(symbol)
## 
##	option_positions_symbol_list = []
##	option_positions_qty_list = []
##	fill_prices_list = []
##	option_positions_option_id_list = []
##	option_positions_delta_list = []
##	option_positions_beta_weighted_delta_list = []
##	option_prices_list = []
##	strike_prices_list = []
##	expirations_list = []
## 
##	for option_position in option_positions_data:
##		# print(option_position)
##		# print(option_position['chain_symbol'])
##		# option_position['symbol'] = r.get_symbol_by_url(option_position['instrument'])
##		symbol = option_position['chain_symbol']
##		option_positions_symbol_list.append(symbol)
##		qty = int(float(option_position['quantity']))
##		option_positions_qty_list.append(qty)
## 
##		fill_price = float(option_position['average_price'])/100
##		fill_prices_list.append(fill_price)
## 
##		option_id = option_position['option_id']
##		option_positions_option_id_list.append(option_id)
##		
##		delta = float(r.get_option_market_data_by_id(option_id)[0]['delta'])
##		option_positions_delta_list.append(delta)
## 
##		option_price = float(r.get_option_market_data_by_id(option_id)[0]['last_trade_price'])
##		option_prices_list.append(option_price)
## 
##		strike_price = float(r.get_option_instrument_data_by_id(option_id)['strike_price'])
##		strike_prices_list.append(strike_price)
## 
##		expiration = r.get_option_instrument_data_by_id(option_id)['expiration_date']
##		expirations_list.append(expiration)
## 
##		reference_price = float(r.get_stock_quote_by_symbol(beta_reference)['last_trade_price'])
##		underlying_price = float(r.get_stock_quote_by_symbol(symbol)['last_trade_price'])
##		beta = 2.04 ##################################################################################
##		delta = delta * qty
##		beta_weighted_delta = (beta * underlying_price * delta) / reference_price 
##		option_positions_beta_weighted_delta_list.append(beta_weighted_delta)
## 
##	# Create the pandas DataFrame 
##	# df = pd.DataFrame({
##	#									 'symbol': position['symbol'],
##	#									 'quantity': position['quantity']					
##	#									 }, index=[0])
##	stocks_df = pd.DataFrame({
##										'symbol': positions_symbol_list,
##										'price': positions_current_price,
##										'average filled price': positions_average_price,
##										'quantity': positions_qty_list				 
##										}, index=[0])
##	stocks_df['profit'] = (stocks_df['price'] - abs(stocks_df['average filled price'])) * stocks_df['quantity']
##	print('\t Stocks')
##	try: display(stocks_df)
##	except: print(stocks_df)
##	print(f'Total stocks profit: ${stocks_df.profit.sum():.2f}')
##	print()
##	
##	options_df = pd.DataFrame({
##										'symbol': option_positions_symbol_list,
##										'strike': strike_prices_list,
##										'quantity': option_positions_qty_list,
##										'average filled price': fill_prices_list,
##										'price': option_prices_list,
##										'expiration': expirations_list,
##										'beta weighted delta': option_positions_beta_weighted_delta_list 
##										# 'delta': option_positions_delta_list			
##										})
##	options_df['profit'] = ((abs(options_df['average filled price']) - options_df['price']) * options_df['quantity']) * 100
##	options_df['collateral'] = (options_df['strike'] * 100) * abs(options_df['quantity'])
##	options_df['total credit'] = (abs(options_df['average filled price']) * abs(options_df['quantity'])) * 100
##	options_df['% return left'] = (((options_df['collateral'] + (options_df['total credit'] - options_df['profit'])) - options_df['collateral']) / (options_df['collateral'] + (options_df['total credit'] - options_df['profit']))) * 100
## 
##	# if options_df['% return left'].item < 25 and (options_df['profit'] == (options_df['total credit'] / 2)):
##	#	 options_df['test'] = 'Closing this position for profit is recommended'
##	# max_shares = stock['balance'].div(stock['close'].values,axis=0)
##	# import numpy as np
##	# test = np.where(options_df['% return left'] < 25, 'Closing this position for profit is recommended', '')
##	# df['Result'] = np.where((df.S == 1) & (df.A == 1), 1,	 #when... then
##	#								np.where((df.S == 1) & (df.A == 0), 0,	#when... then
##	#								 np.where((df.S == 2) & (df.A == 1), 0,	#when... then
##	#									 1)))																	#else
##	# options_df['test'] = test
## 
##	from datetime import datetime
##	from datetime import date
## 
##	# Returns the current local date 
##	today = date.today() 
##	#print("Today date is: ", today) 
## 
##	def days_between(d1, d2):
##			d1 = datetime.strptime(d1, "%Y-%m-%d")
##			d2 = datetime.strptime(d2, "%Y-%m-%d")
##			return abs((d2 - d1).days)
## 
##	# days_to_expiration = days_between(options_df['expiration'], str(today))
##	# options_df['DTE'] = days_between(options_df['expiration'], str(today))
##	DTE_list = []
##	for expiration in options_df['expiration']:
##		DTE_list.append(days_between(expiration, str(today)))
##	options_df['DTE'] = DTE_list
##	options_df['annual % return left'] = (options_df['% return left'] / options_df['DTE']) * 365
## 
##	print('\t Options')
##	try: display(options_df)
##	except: print(options_df)
##	total_beta_weighted_delta = sum(option_positions_beta_weighted_delta_list)
##	print()
##	print(f'Total options profit: ${options_df.profit.sum():.2f}')
##	print(f'Portfolio beta weighted delta: {total_beta_weighted_delta:.3f}')
 

class SeaofBTCapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.iconbitmap(self, default="")
		tk.Tk.wm_title(self, "Open source Robinhood client")
		
		
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=1, column=1, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

		
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self, text="Visit Page 1",
							command=lambda: controller.show_frame(PageOne))
		button.pack()

		button2 = ttk.Button(self, text="Visit Page 2",
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text="Graph Page",
							command=lambda: controller.show_frame(PageThree))
		button3.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text="Page Two",
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text="Page One",
							command=lambda: controller.show_frame(PageOne))
		button2.pack()


class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
		#label.pack(pady=10,padx=10)
		label.grid()
		button1 = ttk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		#button1.pack()
		button1.grid()
		
		symbol = tk.StringVar()
		# cryptoinsert = ttk.Entry(self, textvariable=symbol)
		# cryptoinsert.get()
		# cryptoinsert.pack()
		# print(symbol)
		# #input()
		
		# # login button
		# crypto_button = ttk.Button(self, text="Crypto", command=graph_balance(symbol))
		# crypto_button.pack(fill='x', expand=True, pady=10)
		
		
		global positions_df
		def positions_df():

			# r.markets.get_markets()
			import datetime as dt
			import datetime
			market_next_open_datetime = r.markets.get_market_next_open_hours('ARCX')['opens_at']
			print(market_next_open_datetime)

			market_close_datetime = r.markets.get_market_today_hours('ARCX')['closes_at']
			market_close_datetime = dt.datetime.strptime(market_close_datetime,'%Y-%m-%dT%H:%M:%SZ')

			market_next_open_datetime = dt.datetime.strptime(market_next_open_datetime,'%Y-%m-%dT%H:%M:%SZ')
			current_datetime = datetime.datetime.now()

			# Input own current_datetime to test functionality
			# current_datetime = '2021-03-13 02:51:10.383190'
			# current_datetime = current_datetime[:-3]
			# current_datetime = dt.datetime.strptime(current_datetime,'%Y-%m-%d %H:%M:%S.%f')

			print(market_close_datetime, "\n", 
			      current_datetime)

			if (current_datetime > market_close_datetime) and (current_datetime < market_next_open_datetime):
			  market_open = False
			else: 
			  market_open = True

			if market_open:
			  print('market open')
			else: print('market closed')

			global already_got_options
			try: already_got_options
			except: already_got_options = False

			if (already_got_options == False) and not market_open:
				beta_reference = 'SPY'

				positions_data = r.get_open_stock_positions()

				# option_positions_data = r.get_all_option_positions()
				option_positions_data = r.get_open_option_positions()
				# print(option_positions_data)
				## Note: This for loop adds the stock ticker to every order, since Robinhood
				## does not provide that information in the stock orders.
				## This process is very slow since it is making a GET request for each order.

				positions_symbol_list = []
				positions_qty_list = []
				positions_average_price = []
				positions_current_price = []

				for position in positions_data:
					"""
					Maybe use r.build_holdings() instead?
					"""
					# print(position)
					symbol = r.get_symbol_by_url(position['instrument']) 
					position['symbol'] = symbol
					positions_symbol_list.append(symbol)
					positions_qty_list.append(float(position['quantity']))
					positions_average_price.append(float(position['average_buy_price']))
					positions_current_price.append(float(r.get_stock_quote_by_symbol(symbol)['last_trade_price']))

				# print(position_symbol_list, position_qty_list)
				# input()
				# df.set_index('position',inplace=False)

				# item['symbol']
				# display(position)
				# input()
				# symbol = positions_data['chain_symbol']
				# print(symbol)

				option_positions_symbol_list = []
				option_positions_qty_list = []
				fill_prices_list = []
				option_positions_option_id_list = []
				option_positions_delta_list = []
				option_positions_beta_weighted_delta_list = []
				option_prices_list = []
				strike_prices_list = []
				expirations_list = []
				open_order_list = []

				for option_position in option_positions_data:
					# print(option_position)
					# print(option_position['chain_symbol'])
					# option_position['symbol'] = r.get_symbol_by_url(option_position['instrument'])
					symbol = option_position['chain_symbol']
					option_positions_symbol_list.append(symbol)
					qty = int(float(option_position['quantity']))
					option_positions_qty_list.append(qty)

					fill_price = float(option_position['average_price'])/100
					fill_prices_list.append(fill_price)

					option_id = option_position['option_id']
					option_positions_option_id_list.append(option_id)

					delta = float(r.get_option_market_data_by_id(option_id)[0]['delta'])
					option_positions_delta_list.append(delta)

					option_price = float(r.get_option_market_data_by_id(option_id)[0]['last_trade_price'])
					option_prices_list.append(option_price)

					strike_price = float(r.get_option_instrument_data_by_id(option_id)['strike_price'])
					strike_prices_list.append(strike_price)

					expiration = r.get_option_instrument_data_by_id(option_id)['expiration_date']
					expirations_list.append(expiration)

					# Getting open positions
					open_option_orders = r.get_all_open_option_orders(info=None)

					open_order_option_id_list = []
					open_order = ''

					for open_option_order in open_option_orders:

					  if symbol in open_option_order['chain_symbol']:

					    # print(int(float(open_option_order['quantity'])))
					    # print(open_option_order['legs'])

					    for leg in open_option_order['legs']:
					      
					      open_order_option_id = leg['option']
					      open_order_option_id = open_order_option_id.split('/')
					      open_order_option_id = open_order_option_id[5]
					      open_order_option_id_list.append(open_order_option_id)

					      if open_order_option_id == option_id:
					        open_order = str(int(float(open_option_order['quantity']))) + ' ' + leg['position_effect'] + ' ' + str(round(float(open_option_order['price']), 2))

					open_order_list.append(open_order)

					# /end Getting open positions

					reference_price = float(r.get_stock_quote_by_symbol(beta_reference)['last_trade_price'])
					underlying_price = float(r.get_stock_quote_by_symbol(symbol)['last_trade_price'])
					beta = 2.04 ################################################################################## find a way to dynamically get beta of SPY
					delta = delta * qty
					beta_weighted_delta = (beta * underlying_price * delta) / reference_price 
					option_positions_beta_weighted_delta_list.append(beta_weighted_delta)

				# Create the pandas DataFrame 
				# df = pd.DataFrame({
				#                   'symbol': position['symbol'],
				#                   'quantity': position['quantity']          
				#                   }, index=[0])
				stocks_df = pd.DataFrame({
				                'symbol': positions_symbol_list,
				                'price': positions_current_price,
				                'average filled price': positions_average_price,
				                'quantity': positions_qty_list         
				                }, index=[0])
				stocks_df['profit'] = (stocks_df['price'] - abs(stocks_df['average filled price'])) * stocks_df['quantity']
				print('\t Stocks')
				#display(stocks_df)
				print(f'Total stocks profit: ${stocks_df.profit.sum():.2f}')
				print()

				options_df = pd.DataFrame({
				                'symbol': option_positions_symbol_list,
				                'strike': strike_prices_list,
				                'quantity': option_positions_qty_list,
				                'average filled price': fill_prices_list,
				                'price': option_prices_list,
				                'expiration': expirations_list,
				                'beta weighted delta': option_positions_beta_weighted_delta_list,
				                'open orders': open_order_list
				                # 'delta': option_positions_delta_list      
				                })

				options_df['profit'] = ((abs(options_df['average filled price']) - options_df['price']) * options_df['quantity']) * 100
				# portfolio_balance_dates_df.loc[portfolio_balance_dates_df['running balance'] < 0, 'running balance'] = 0
				options_df['collateral'] = (options_df['strike'] * 100) * abs(options_df['quantity'])
				# Convert 'collateral' column from float to integer
				options_df['collateral'] = pd.to_numeric(options_df['collateral'], downcast='integer')
				options_df = options_df.sort_values(by='expiration')

				options_df['total credit'] = (abs(options_df['average filled price']) * abs(options_df['quantity'])) * 100
				# Adjusting collateral for credit spreads
				for i in range(len(options_df)):
					if (options_df['average filled price'][i] < 0) and (options_df['expiration'][i] == options_df['expiration'][i+1]):
						options_df['collateral'][i] = (abs(options_df['strike'][i] - options_df['strike'][i+1]) * 100) * options_df['quantity'][i]
						options_df['collateral'][i+1] = 0

						options_df['total credit'][i] = options_df['total credit'][i] - options_df['total credit'][i+1]
						options_df['total credit'][i+1] = 0

						# options_df['profit'][i] = options_df['profit'][i+1] - options_df['profit'][i+1]
						options_df['profit'][i] = ((abs(options_df['average filled price'][i]) - options_df['average filled price'][i+1]) - (options_df['profit'][i] - options_df['profit'][i+1])) * 100
						options_df['profit'][i] = (options_df['price'][i] - options_df['average filled price'][i]) - (options_df['price'][i+1] - options_df['average filled price'][i+1])

				options_df.loc[options_df['collateral'] == 0, 'total credit'] = 0

				# /end Adjusting collateral for credit spreads

				options_df['% of total credit'] = (options_df['profit'] / options_df['total credit']) * 100
				options_df.loc[options_df['collateral'] == 0, '% of total credit'] = 0
				options_df['% return left'] = (((options_df['collateral'] + (options_df['total credit'] - options_df['profit'])) - options_df['collateral']) / (options_df['collateral'] + (options_df['total credit'] - options_df['profit']))) * 100
				options_df.loc[options_df['collateral'] == 0, '% return left'] = 0
				# if options_df['% return left'].item < 25 and (options_df['profit'] == (options_df['total credit'] / 2)):
				#   options_df['test'] = 'Closing this position for profit is recommended'
				# max_shares = stock['balance'].div(stock['close'].values,axis=0)
				# import numpy as np
				# test = np.where(options_df['% return left'] < 25, 'Closing this position for profit is recommended', '')
				# df['Result'] = np.where((df.S == 1) & (df.A == 1), 1,   #when... then
				#                np.where((df.S == 1) & (df.A == 0), 0,  #when... then
				#                 np.where((df.S == 2) & (df.A == 1), 0,  #when... then
				#                   1)))                                  #else
				# options_df['test'] = test

				from datetime import datetime
				from datetime import date

				# Returns the current local date 
				today = date.today() 
				#print("Today date is: ", today) 

				def days_between(d1, d2):
				  d1 = datetime.strptime(d1, "%Y-%m-%d")
				  d2 = datetime.strptime(d2, "%Y-%m-%d")
				  return abs((d2 - d1).days)

				# days_to_expiration = days_between(options_df['expiration'], str(today))
				# options_df['DTE'] = days_between(options_df['expiration'], str(today))
				DTE_list = []
				for expiration in options_df['expiration']:
					DTE_list.append(days_between(expiration, str(today)))
				options_df['DTE'] = DTE_list
				options_df['annual % return left'] = (options_df['% return left'] / options_df['DTE']) * 365

				print('\t Options')
				#display(options_df)
				total_beta_weighted_delta = sum(option_positions_beta_weighted_delta_list)
				print()
				print(f'Total options profit: ${options_df.profit.sum():.2f}')
				print(f'Option portfolio beta weighted delta: {total_beta_weighted_delta:.3f}')

				print()

				cash_balances = r.account.load_phoenix_account()

				total_crypto_equity = float(cash_balances['crypto']['equity']['amount'])
				total_options_collat = float(cash_balances['cash_held_for_options_collateral']['amount'])
				buying_power = cash_balances['account_buying_power']['amount']
				cash_in_orders = cash_balances['cash_held_for_equity_orders']['amount']

				total_equity = float(cash_balances['total_equity']['amount'])

				print(f'Portfolio balance: ${total_equity:.2f}')

				print(f'Total crypto equity: ${total_crypto_equity}')
				print(f'Total options collateral: ${total_options_collat}')
				print(f'Buying power: ${buying_power}')
				print(f'Total cash in open orders: ${cash_in_orders}')

				print(f'% of portfolio in crypto: {(total_crypto_equity/total_equity)*100:.2f}%')
				print(f'% of portfolio in options collateral: {(total_options_collat/total_equity)*100:.2f}%')

				# take the data 
				# lst = [(1,'Raj','Mumbai',19), 
				# 	   (2,'Aaryan','Pune',18), 
				# 	   (3,'Vaishnavi','Mumbai',20), 
				# 	   (4,'Rachna','Mumbai',21), 
				# 	   (5,'Shubham','Delhi',21)] 

				# headers = [	'option_positions_symbol_list',
				# 			'strike_prices_list',
				# 			'option_positions_qty_list',
				# 			'fill_prices_list',
				# 			'option_prices_list',
				# 			'expirations_list',
				# 			'option_positions_beta_weighted_delta_list',
				# 			'open_order_list']
				headers = 'symbol	strike	quantity	average filled price	price	expiration	beta weighted delta	open orders	profit	collateral	total credit	% of total credit	% return left	DTE	annual % return left'
				headers = headers.split('	')

				lst = 	[[headers],
						option_positions_symbol_list,
						strike_prices_list,
						option_positions_qty_list,
						fill_prices_list,
						option_prices_list,
						expirations_list,
						option_positions_beta_weighted_delta_list,
						open_order_list]

				# 'symbol': option_positions_symbol_list,
				# 'strike': strike_prices_list,
				# 'quantity': option_positions_qty_list,
				# 'average filled price': fill_prices_list,
				# 'price': option_prices_list,
				# 'expiration': expirations_list,
				# 'beta weighted delta': option_positions_beta_weighted_delta_list,
				# 'open orders': open_order_list

				# lst = options_df
				# lst = option_positions_symbol_list
				   
				# find total number of rows and 
				# columns in list 
		
				# total_rows = len(lst) 
				# total_columns = len(lst[0])
				total_rows = len(lst)
				total_columns = 3
				# print(total_rows, total_columns)
				#input()
				# total_columns = len(options_df.columns)
				
				# code for creating table 
				# for i in range(total_rows): 
				# 	for j in range(total_columns): 
						  
				# 		self.e = Entry(self, width=20, fg='white', bg='black',
				# 					   font=('Arial',16,'bold')) 
						  
				# 		self.e.grid(column=j+1, row=i+1, sticky='nsew', padx=0, pady=0)

				# 		#self.e.pack()
				# 		self.e.insert(END, lst[i][j]) 

				
				#print(len(options_df), len(options_df.columns))
				#input()

				for column in range(len(headers)):
					self.e = Entry(self, width=0, fg='white', bg='black',
										   font=('Arial',12,'bold')) 
							  
					self.e.grid(column=column+1, row=2, sticky='nsew', padx=0, pady=0)

					#self.e.pack()
					self.e.insert(END, headers[column]) 

				for row in range(len(options_df)):
					for column in range(len(options_df.columns)):
						self.e = Entry(self, width=0, fg='white', bg='black',
											   font=('Arial',12,'bold')) 
								  
						self.e.grid(column=column+1, row=row+3, sticky='nsew', padx=0, pady=0)

						#self.e.pack()
						self.e.insert(END, options_df.iloc[row,column]) 
				   
				# create root window 
				#self = Tk() 
				#t = Table(self)

			
			already_got_options = True



		#graph_historical_portfolio()
		
		global graph_balance
		def graph_balance(interval='hour', span='week', bounds='24_7', info=None, self=self):
			"""
				FOR STOCKS ONLY
			interval_check = ['5minute', '10minute', 'hour', 'day', 'week']
			span_check = ['day', 'week', 'month', '3month', 'year', '5year', 'all']
			bounds_check = ['extended', 'regular', 'trading']
			"""
			bank_transfers = r.get_bank_transfers() # info=amount

			historical_transfers = []

			for transfer in bank_transfers:
				state = transfer['state']
				if state != "completed":
					continue
				amount = float(transfer['amount'])
				direction = transfer['direction']
				# print(amount, state, direction)
				if direction != 'deposit':
					amount = -amount
				historical_transfers.append(amount)

			transfer_datetimes_list = []

			for transfer in bank_transfers:
				state = transfer['state']
				if state != "completed":
					continue
				transfer_datetime = transfer['updated_at']
				transfer_datetimes_list.append(transfer_datetime)

			# change the dates into a format that matplotlib can recognize.
			# historical_transfer_dates = [dt.datetime.strptime(datetime,'%Y-%m-%dT%H:%M:%S.%f%z') for datetime in transfer_datetimes_list]
			# print(transfer_datetimes_list)
			# '2021-02-17T14:59:49.452230Z'
			transfer_datetimes_list_cleaned = []
			for datetime in transfer_datetimes_list:
				datetime = datetime.split('T')[0]
				transfer_datetimes_list_cleaned.append(datetime)
				# print(transfer_datetimes_list_cleaned)

			historical_transfer_dates = [dt.datetime.strptime(datetime,'%Y-%m-%d') for datetime in transfer_datetimes_list_cleaned]
			import numpy as np
			historical_transfers_df = pd.DataFrame(np.array(historical_transfers), columns = list(['historical transfers']), index=historical_transfer_dates)

			print(symbol.get())
			print(interval, span, bounds)
			label = Label( self , text = " " ) 
			#label.pack()
			
			label.config( text = symbol.get().upper() )
			label.grid(column=5, row=0, sticky='nsew', padx=0, pady=0)
			#label.config( text = interval_var.get() )
			interval = interval_var.get()
			span = span_var.get()
			#symbol = symbol.get()
			#symbol = input('Enter crypto ticker: ')
			print(symbol.get())
			print(interval)
			historical_portfolio = r.get_historical_portfolio(interval=interval, span='all', info=info) ###### could change info to close_equity
			historical_portfolio = historical_portfolio['equity_historicals']
			dates = []
			close_equity_list = []
			open_equity_list = []
			for data_point in historical_portfolio:
				# print(data_point)
				dates.append(data_point['begins_at'])
				close_equity_list.append(float(data_point['close_equity'])) # close_price
				open_equity_list.append(float(data_point['open_equity'])) # open_price
			balance_datetimes_list_cleaned = []
			for datetime in dates:
				datetime = datetime.split('T')[0]
				balance_datetimes_list_cleaned.append(datetime)
			# print(balance_datetimes_list_cleaned)
			
			portfolio_balance_dates = [dt.datetime.strptime(datetime,'%Y-%m-%d') for datetime in balance_datetimes_list_cleaned]
			import numpy as np
			# a1, a2 = df1.align(df2, join='outer', axis=1)
			# print(portfolio_balance_dates, close_equity_list)
			# input()
			portfolio_balance_dates_df = pd.DataFrame(np.array(close_equity_list), columns = list(['portfolio balance']), index=portfolio_balance_dates)
			portfolio_balance_dates_df = portfolio_balance_dates_df.merge(historical_transfers_df,
																				  how='outer',
																				  left_index=True,
																				  right_index=True,
																				).fillna(0)
			i = len(portfolio_balance_dates_df)-1
			portfolio_balance_dates_df['running transfers'] = 0.00
			for i in range(len(portfolio_balance_dates_df)):
				portfolio_balance_dates_df['running transfers'][i] = portfolio_balance_dates_df['running transfers'][i-1] + portfolio_balance_dates_df['historical transfers'][i]


			i = len(portfolio_balance_dates_df)

			while i >= 0:
				portfolio_balance_dates_df['running balance'] = portfolio_balance_dates_df['portfolio balance'] - portfolio_balance_dates_df['running transfers']
				i = i - 1

			portfolio_balance_dates_df.loc[portfolio_balance_dates_df['running balance'] < 0, 'running balance'] = 0

			# plt.plot(portfolio_balance_dates_df['running balance'])
			# # plt.plot(x, openPrices)
			# plt.ylabel('Price')
			# plt.xlabel('Date')
			# plt.show()

			if symbol.get() != '':
				
				try:
					bounds = '24_7'
					historical_security = r.crypto.get_crypto_historicals(symbol.get(), interval=interval, span=span, bounds=bounds, info=info) 
				# except Exception as e:
					# if 'Not found for url' in str(e):
				except TypeError:
					#print(interval)
					
					bounds = 'regular'
					historical_security = r.get_stock_historicals(symbol.get(), interval=interval, span=span, bounds=bounds, info=info) ###### could change info to close_equity
				# display(historical_portfolio)
				#print(historical_portfolio[0])
			
				#input()
				close_prices_list = []
				dates_list = []

				for candle in historical_security:
					close_price = float(candle['close_price'])
					close_prices_list.append(close_price)
					date = candle['begins_at']
					dates_list.append(date)
			
		##		dates = []
		##		close_equity_list = []
		##		open_equity_list = []
		##	 
		##		for data_point in historical_portfolio:
		##			# print(data_point)
		##			dates.append(data_point['begins_at'])
		##			close_equity_list.append(float(data_point['close_equity'])) # close_price
		##			open_equity_list.append(float(data_point['open_equity'])) # open_price
		 
				# input(dates)
				# change the dates into a format that matplotlib can recognize.
				print(dates_list)
				dates_list = [dt.datetime.strptime(d,'%Y-%m-%dT%H:%M:%SZ') for d in dates_list]
				print(dates_list)
				#input()
				print('plotting graph')
				graph1.clear()
				
				graph1.plot(dates_list, close_prices_list)
			
			f2 = Figure(figsize=(3,3), dpi=100)
			
			a = f2.add_subplot(111)
			
			# a.plot(dates, close_equity_list)
			a.plot(portfolio_balance_dates_df['running balance'])
			
			canvas2 = FigureCanvasTkAgg(f2, self)
			
			canvas2.get_tk_widget().grid(column=10, row=1, sticky='nsew', padx=0, pady=0, columnspan=10)#.place(relx=1,rely=0.100)
			# toolbar_frame2 = tk.Frame(self)
			# toolbar_frame2.grid(column = 0, row = 1)

			# toolbar2 = NavigationToolbar2TkAgg(canvas, toolbar_frame2)

			# toolbar2 = NavigationToolbar2TkAgg(canvas2, self)
			# toolbar2.update()

			canvas2._tkcanvas.grid(column=10, row=1, sticky='nsew', padx=0, pady=0, columnspan=10)#.place(relx=1,rely=0.100)
			#graph2.plot(dates, close_equity_list)
			

			
		from tkinter import messagebox
		
		#Label(self, text='Enter Crypto Ticker Symbol').pack(pady=20)
		Label(self, text='Enter Crypto or Stock Ticker Symbol').grid(pady=0)
		name_Tf = Entry(self, textvariable=symbol)
		name_Tf.bind('<Return>', graph_balance)
		#name_Tf.pack()
		name_Tf.grid()

		Label(self, text=symbol.get()).grid(column=0, row=0, sticky='nsew', padx=0, pady=0)

		#name_Tf.focus()
		# Change the label text 
		# def show():  
			# label.config( text = symbol.get() )
			# label.config( text = interval_var.get() )
			# interval = interval_var.get()
			# return interval

		# Dropdown menu options 
		interval_options = [ 
			"5minute", 
			"10minute", 
			"hour", 
			"day", 
			"week"
		] 
		
		span_options = ['day', 'week', 'month', '3month', 'year', '5year', 'all']
		  
		# datatype of menu text 
		interval_var = StringVar() 
		span_var = StringVar()
		  
		# initial menu text 
		interval_var.set('hour') 
		span_var.set('day')
		  
		# Create Dropdown menu 
		interval_dropdown = OptionMenu( self , interval_var , *interval_options ) 
		#interval_dropdown.pack() 
		interval_dropdown.grid()
		# Create Dropdown menu 
		span_dropdown = OptionMenu( self , span_var , *span_options ) 
		#span_dropdown.pack() 
		span_dropdown.grid() 
		# Create button, it will change label text 
		# button = Button( self , text = "Graph" , command = graph_balance ).pack() 
		# button2 = Button( self , text = "Change interval", command = show).pack() 
		  
		# Create Label 
		label = Label( self , text = " " ) 
		#label.pack()
		label.grid()
		print(symbol)
		



		frame1 = tk.Frame()
		canvas = FigureCanvasTkAgg(f, self)
		#canvas2 = FigureCanvasTkAgg(f, self) # self is the page/window
		#canvas.show()
		canvas.draw()
		#canvas2.draw()
		#canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas.get_tk_widget().grid(column=0, row=1, sticky='nsew', padx=0, pady=0, columnspan=10) # -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
		#canvas2.get_tk_widget().grid(column=10, row=1, sticky='nsew', padx=0, pady=0, columnspan=10)
		# toolbar_frame = tk.Frame(self)
		# toolbar_frame.grid(column = 0, row = 1)

		# toolbar = NavigationToolbar2TkAgg(canvas, toolbar_frame)


		# toolbar = NavigationToolbar2TkAgg(canvas, self).grid()
		# toolbar.update()
		#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.grid(column=0, row=1, sticky='nsew', padx=0, pady=0, columnspan=10)
		#canvas2._tkcanvas.grid(column=10, row=1, sticky='nsew', padx=0, pady=0, columnspan=10)



		
		
		


app = SeaofBTCapp()
seconds = 20
ani = animation.FuncAnimation(f, animate, interval=seconds*1000)
app.mainloop()
