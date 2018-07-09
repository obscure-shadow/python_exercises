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
    print(f'{ticker}: ${holdings}')

new_new_stockdict = {}

# finished second half of problem.

for tickers in purchases:
    if tickers[0] in new_new_stockdict:
        new_new_stockdict[tickers[0]] += [(tickers[1],tickers[2],tickers[3])]
    else:
        new_new_stockdict[tickers[0]] = [(tickers[1],tickers[2],tickers[3])]

print(new_new_stockdict)