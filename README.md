# PersonalFinanceTrackerPy
This is an open-source personal finance and portfolio tracker that I made so I can keep track of my stocks, options, dollars, and cryptocurrencies. Automatically retrieves brokerage info and calculates beta weighted delta. Currently only supports Robinhood, with plans for TD Ameritrade, Interactive Brokers, Gemini, and bank accounts through Plaid.

## TODO:

### Features:

- Add options screener by custom formula
  - Currently available as a standalone repository: https://github.com/GrahamboJangles/PutPremiumProcessor

- Add support for other brokerages
  - TD Ameritrade
  - Interactive Brokers
  - Gemini (for trading crypto)
  
- Add bank support through Plaid

- Add ability to place trades
  - Stock
  - Options
  - Crypto

- Whole net worth tracker with support for other brokerages by manually entering positions

### Functionality:

- Put data fetching on another thread
  
### Tables:

- ~~Show open orders next to the positions~~

- ~~Make collateral an integer~~

- Add stocks position dataframe to GUI

- Show total cash being used by open orders

- Adjust collateral for spreads

### Graphs:

- Add another graph for historical options price

- Fix the portfolio graph
  - Add dropdown for span
  - Add a checkbox for whether to include bank transfers in graph 
  
- Print current portfolio balance next to portfolio chart
  - Print profit for day

### Known Bugs:
- The portfolio chart only works for 'all' span, and even then it doesn't look quite right
