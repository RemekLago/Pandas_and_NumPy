
import pandas as pd
import numpy as np

# creating a Series
list_of_companies_stock = ['Alior', 'CCC', 'CD Project', 'Cyfrowy Polsat', 'Dino', 'JSW', 'KGHM', 'Lotos', 'LPP',
                           'mBank', 'Orange', 'PEKAO SA', 'PGE', 'PGNIG', 'PKN ORLEN', 'PKO BP', 'PLAY', 'PZU', 'Santander', 'Tauron']

wig20 = pd.Series(list_of_companies_stock, name='WIG 20')
# capitalise names
wig20_names = wig20.apply(lambda word: word.upper())
wig20_names.isin(['CCC'])
wig20_names[wig20_names.isin(['CCC', 'PGE'])]

for company in wig20_names:
    print(company)
    
for company in wig20_names:
    company = company + "_PLN"
    print(company)

#
stock_with_len_4 = []
for company in wig20_names:
    if len(company) == 4:
        stock_with_len_4.append(company)
print(stock_with_len_4)
# list comprehension
stock_with_len_5 = [company for company in wig20_names if len(company) == 5]
print(stock_with_len_5)

stock_with_P = [company for company in wig20_names if company.startswith('P')]
print(stock_with_P)

stock_end_P = [company for company in wig20_names if company.endswith('P')]
print(stock_end_P)

stock_replace = [company.replace(' ', '_') for company in wig20_names]
print(stock_replace)
