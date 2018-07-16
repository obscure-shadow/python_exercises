# A block of publicly traded stock has a variety of attributes, we'll look at a few of them.
# A stock has a ticker symbol and a company name.
# Create a simple dictionary with ticker symbols and company names.

# Example
stockDict = { 'GM': 'General Motors',
    'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
# Create a simple list of blocks of stock.
# These could be tuples with ticker symbols, number of shares, dates and price.


purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 ) ]
# Create a purchase history report that computes the full purchase price (shares times dollars)
# for each block of stock and uses the stockDict to look up the full company name.
total_investment = 0
for shares in purchases:
    for k,y in stockDict.items():
        if k == shares[0]:
            investment = shares[1] * shares[3]
            print(f'{y}: {investment}')
            total_investment += investment

# Create a second purchase summary that which accumulates total investment by ticker symbol.
print(f'Total of Investments = {total_investment}')
# In the above sample data, there are two blocks of GM.
# These can easily be combined by creating a dict where the key is the ticker and
# the value is the list of blocks purchased.
# The program makes one pass through the data to create the dict.
# A pass through the dict can then create a report showing each ticker symbol and
# all blocks of stock.

# sample planning...
new_stockdict = {
                    'GM' : [
                        ( 100, '10-sept-2001', 48 ),
                        ( 200, '1-jul-1998', 56 )
                    ],
                    'CAT' : [
                        ( 100, '1-apr-1999', 24 )
                    ]
                }

for ticker, shares in new_stockdict.items():
    holdings = 0
    for share in shares:
        value = share[0] * share[2]
        holdings += value
    print(f'{ticker}:\n      ${holdings}')

# print('\n\n'.format())

new_new_stockdict = {}

# finished second half of problem.

for tickers in purchases:
    if tickers[0] in new_new_stockdict:
        new_new_stockdict[tickers[0]] += [(tickers[1],tickers[2],tickers[3])]
    else:
        new_new_stockdict[tickers[0]] = [(tickers[1],tickers[2],tickers[3])]

# for key, socks in new_new_stockdict
print(new_new_stockdict)

# stockDict = { 'GE': 'General Electric',
#  'MSFT': 'Microsoft',
#  'APPL': 'Apple',
#  'CAT':'Caterpillar', 'EK':'Eastman Kodak' }

# purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
#  ( 'CAT', 100, '1-apr-1999', 24 ),
#  ( 'MSFT', 1000, '1-apr-1999', 198 ),
#  ( 'MSFT', 250, '1-apr-1999', 75 ),
#  ( 'MSFT', 333, '1-apr-1999', 100 ),
#  ( 'APPL', 50, '1-apr-1999', 144 ),
#  ( 'EK', 300, '5-apr-2017', 9 ),
#  ( 'GE', 200, '1-jul-1998', 56 ) ]



























portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    minimal_purchase = (purchase[1], purchase[2], purchase[3])

    try:
        portfolio[ticker].append(purchase) # Append the purchase to the ticker list
    except KeyError:
        portfolio[ticker] = list() # If the key doesn't exist yet, create it
        portfolio[ticker].append(purchase)


    print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

print(portfolio)







for ticker,purchases in portfolio.items():
    print("------ {} ------".format(ticker))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print("    {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))