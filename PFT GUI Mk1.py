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
style.use("ggplot") # can do a dark mode i forgot how

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

symbol = ''


def animate(i):
	#pullData = open("sampleText.txt","r").read()
	#dataList = pullData.split('\n')
	
	
	
	import os
	clear = lambda: os.system('cls')
	clear()
	
	total_equity = float(r.account.load_phoenix_account()['total_equity']['amount'])
	print(f'Portfolio balance: ${total_equity:.2f}')
	previous_close = float(r.account.load_phoenix_account()['portfolio_previous_close']['amount'])
	print(f"Today's profit: ${total_equity - previous_close:.2f}")
	
	#graph_historical_portfolio()
	#positions_df()
		
	#graph_balance(span='day')
	#graph_balance()
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

			frame.grid(row=0, column=0, sticky="nsew")

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
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		symbol = tk.StringVar()
		# cryptoinsert = ttk.Entry(self, textvariable=symbol)
		# cryptoinsert.get()
		# cryptoinsert.pack()
		# print(symbol)
		# #input()
		
		# # login button
		# crypto_button = ttk.Button(self, text="Crypto", command=graph_balance(symbol))
		# crypto_button.pack(fill='x', expand=True, pady=10)
		
		def graph_balance(interval='hour', span='week', bounds='24_7', info=None, self=self):
			"""
			interval_check = ['5minute', '10minute', 'hour', 'day', 'week']
			span_check = ['day', 'week', 'month', '3month', 'year', '5year', 'all']
			bounds_check = ['extended', 'regular', 'trading']
			"""
			
			#print(symbol)
			print(interval, span, bounds)
			label = Label( self , text = " " ) 
			label.pack() 
			label.config( text = symbol.get() )
			label.config( text = interval_var.get() )
			interval = interval_var.get()
			#symbol = input('Enter crypto ticker: ')
			print(symbol.get())
			historical_portfolio = r.crypto.get_crypto_historicals(symbol.get(), interval=interval, span=span, bounds=bounds, info=info) 
			# display(historical_portfolio)
			print(historical_portfolio[0])
			historicalbitcoin = historical_portfolio
			#input()
			close_prices_list = []
			dates_list = []
			for candle in historicalbitcoin:
				close_price = float(candle['close_price'])
				close_prices_list.append(close_price)
				date = candle['begins_at']
				dates_list.append(date)
		##		dates = []
		##		closingPrices = []
		##		openPrices = []
		##	 
		##		for data_point in historicalData:
		##			# print(data_point)
		##			dates.append(data_point['begins_at'])
		##			closingPrices.append(float(data_point['close_equity'])) # close_price
		##			openPrices.append(float(data_point['open_equity'])) # open_price
		 
			# input(dates)
			# change the dates into a format that matplotlib can recognize.
			print(dates_list)
			dates_list = [dt.datetime.strptime(d,'%Y-%m-%dT%H:%M:%SZ') for d in dates_list]
			print(dates_list)
			#input()
			print('plotting graph')
			a.clear()
			a.plot(dates_list,close_prices_list)
		from tkinter import messagebox
		
		Label(self, text='Enter Crypto Ticker Symbol').pack(pady=20)
		name_Tf = Entry(self, textvariable=symbol)
		name_Tf.bind('<Return>', graph_balance)
		name_Tf.pack()
		#name_Tf.focus()
		# Change the label text 
		def show():  
			label.config( text = symbol.get() )
			label.config( text = interval_var.get() )
			interval = interval_var.get()
			return interval

		# Dropdown menu options 
		options = [ 
			"5minute", 
			"10minute", 
			"hour", 
			"day", 
			"week"
		] 
		  
		# datatype of menu text 
		interval_var = StringVar() 
		  
		# initial menu text 
		interval_var.set( "5minute" ) 
		  
		# Create Dropdown menu 
		drop = OptionMenu( self , interval_var , *options ) 
		drop.pack() 
		  
		# Create button, it will change label text 
		button = Button( self , text = "Graph" , command = graph_balance ).pack() 
		button2 = Button( self , text = "Change interval", command = show).pack() 
		  
		# Create Label 
		label = Label( self , text = " " ) 
		label.pack() 
		print(symbol)
		
		
		canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		
		


app = SeaofBTCapp()
seconds = 17
ani = animation.FuncAnimation(f, animate, interval=seconds*1000)
app.mainloop()
