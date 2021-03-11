import robin_stocks.robinhood as r
login = r.login('username/email','password')

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
def graph_historical_portfolio(show_transfers=False):
 
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

  print()
  display(historical_transfers_df)
  # input()
 
  plt.plot(historical_transfer_dates, historical_transfers)
  # plt.plot(x, openPrices)
  plt.ylabel('Transfers')
  plt.xlabel('Date')
  plt.show()
  # input(historical_transfers)
  def graph_balance(interval='5minute', span='all', bounds='regular', info=None, historical_transfers_df=historical_transfers_df):
    """
    interval_check = ['5minute', '10minute', 'hour', 'day', 'week']
    span_check = ['day', 'week', 'month', '3month', 'year', '5year', 'all']
    bounds_check = ['extended', 'regular', 'trading']
    """
    historical_portfolio = r.get_historical_portfolio(interval=interval, span=span, bounds=bounds, info=info) ###### could change info to close_equity
    # display(historical_portfolio)
    # input()
 
    historicalData = historical_portfolio['equity_historicals']
 
    dates = []
    closingPrices = []
    openPrices = []
 
    for data_point in historicalData:
      # print(data_point)
      dates.append(data_point['begins_at'])
      closingPrices.append(float(data_point['close_equity'])) # close_price
      openPrices.append(float(data_point['open_equity'])) # open_price
 
    balance_datetimes_list_cleaned = []
    for datetime in dates:
      datetime = datetime.split('T')[0]
      balance_datetimes_list_cleaned.append(datetime)
    # print(balance_datetimes_list_cleaned)
    
    portfolio_balance_dates = [dt.datetime.strptime(datetime,'%Y-%m-%d') for datetime in balance_datetimes_list_cleaned]
    import numpy as np
    # a1, a2 = df1.align(df2, join='outer', axis=1)
    # print(portfolio_balance_dates, closingPrices)
    # input()
    portfolio_balance_dates_df = pd.DataFrame(np.array(closingPrices), columns = list(['portfolio balance']), index=portfolio_balance_dates)

    display(portfolio_balance_dates_df.tail(n=60))
    display(historical_transfers_df.tail(n=60))
    print(len(portfolio_balance_dates_df))
    print(len(historical_transfers_df))
    # test = portfolio_balance_dates_df.merge(historical_transfers_df, left_index=True, right_index=True)
    


    # test = np.where(portfolio_balance_dates_df.index == historical_transfers_df.index, print('shit'), print('fart'))
    # display(test)

    # test = test['portfolio balance'] - test['historical transfers']

    # plt.plot(test)
    # # plt.plot(x, openPrices)
    # plt.ylabel('Price')
    # plt.xlabel('Date')
    # plt.show()

    # input(dates)
    # change the dates into a format that matplotlib can recognize.
    portfolio_balance_dates = [dt.datetime.strptime(d,'%Y-%m-%dT%H:%M:%SZ') for d in dates]
    
    # plot the data.
    # plt.plot(x, closingPrices, 'ro')
    # plt.plot(x, openPrices, 'bo')
    # plt.title("Option price for {} over time".format(symbol_name))
    # plt.xlabel("Dates")
    # plt.ylabel("Price")
    # plt.show()

    portfolio_balances_df = pd.DataFrame(np.array(closingPrices), columns = list(['portfolio balances']))
    portfolio_balance_dates_df = portfolio_balance_dates_df.merge(historical_transfers_df,
      how='outer',
      left_index=True,
      right_index=True,
    ).fillna(0)

    # for row in portfolio_balance_dates_df[::-1].iterrows():
    #   row['running balance'] = row['portfolio balance'] - row['historical transfers']

    # for i in range(portfolio_balance_dates_df):
    # for row in portfolio_balance_dates_df:
    #   row['running transfers'] = row['historical transfers'] + row['historical transfers'][:-1]

    i = len(portfolio_balance_dates_df)-1
    portfolio_balance_dates_df['running transfers'] = 0.00

    # while i >= 0:
    #   portfolio_balance_dates_df['running transfers'][i] = portfolio_balance_dates_df['running transfers'][i-1] + portfolio_balance_dates_df['historical transfers'][i]
    #   i = i - 1

    for i in range(len(portfolio_balance_dates_df)):
      portfolio_balance_dates_df['running transfers'][i] = portfolio_balance_dates_df['running transfers'][i-1] + portfolio_balance_dates_df['historical transfers'][i]


    i = len(portfolio_balance_dates_df)

    while i >= 0:
      portfolio_balance_dates_df['running balance'] = portfolio_balance_dates_df['portfolio balance'] - portfolio_balance_dates_df['running transfers']
      i = i - 1


    # portfolio_balance_dates_df['running balance'] = portfolio_balance_dates_df['portfolio balance'][-1] - portfolio_balance_dates_df['historical transfers']
    # portfolio_balance_dates_df.loc[portfolio_balance_dates_df['portfolio balance'] > 0, 'running balance'] = portfolio_balance_dates_df['portfolio balance'] - portfolio_balance_dates_df['historical transfers']


    #portfolio_balance_dates_df = portfolio_balance_dates_df['portfolio balance'] - portfolio_balance_dates_df['historical transfers']
    print('portfolio_balance_dates_df')
    display(portfolio_balance_dates_df.tail(n=60))
    portfolio_balance_dates_df.loc[portfolio_balance_dates_df['running balance'] < 0, 'running balance'] = 0

    plt.plot(portfolio_balance_dates_df['running balance'])
    # plt.plot(x, openPrices)
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.show()

    # plt.plot(portfolio_balance_dates, closingPrices)
    plt.plot(portfolio_balance_dates_df)
    # plt.plot(x, openPrices)
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.show()
    #input()
 
    # for price in closingPrices:
    #   print(portfolio_balance_dates)
    #   print(historical_transfer_dates)
    #   input
    #   if portfolio_balance_dates == historical_transfer_dates:
    #     price = closingPrices - historical_transfers
 
    # import numpy as np
    # plt.plot(portfolio_balance_dates, closingPrices)
    # # plt.plot(x, openPrices)
    # plt.ylabel('Price')
    # plt.xlabel('Date')
    # plt.show()
 
  total_equity = float(r.account.load_phoenix_account()['total_equity']['amount'])
  print(f'Portfolio balance: ${total_equity:.2f}')
  previous_close = float(r.account.load_phoenix_account()['portfolio_previous_close']['amount'])
  print(f"Today's profit: ${total_equity - previous_close:.2f}")
 
  graph_balance(historical_transfers_df=historical_transfers_df)
  graph_balance(span='day')
 
def positions_df():
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
  display(stocks_df)
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
  # Adjusting collateral for credit spreads
  for i in range(len(options_df)):
    if (options_df['average filled price'][i] < 0) and (options_df['expiration'][i] == options_df['expiration'][i+1]):
      options_df['collateral'][i] = (abs(options_df['strike'][i] - options_df['strike'][i+1]) * 100) * options_df['quantity'][i]
      options_df['collateral'][i+1] = 0
  options_df['total credit'] = (abs(options_df['average filled price']) * abs(options_df['quantity'])) * 100
  options_df['% return left'] = (((options_df['collateral'] + (options_df['total credit'] - options_df['profit'])) - options_df['collateral']) / (options_df['collateral'] + (options_df['total credit'] - options_df['profit']))) * 100
 
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
  display(options_df)
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
 
graph_historical_portfolio()
positions_df()
