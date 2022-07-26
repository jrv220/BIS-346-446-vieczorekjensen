# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:52:10 2022

@author: jense
"""

a = [[83, '\t', 'Electric sander', 7, '\t', '57.98'], [24, '\t', \
     'Power saw', '\t', 18, '\t', '99.99'], [7, '\t', '\t', 'Sledge hammer', \
     11, '\t', '21.50', '\t'], [77, '\t', 'Hammer', '\t', '\t', 76, '\t', \
     '11.99'], [39, '\t', 'Jig saw', '\t', '\t', 3, '\t', '79.50']]
    
print('Part no.', 'Part description', 'Quantity', 'Price')
for row in a:
    for item in row:
        print(item, end='  ')
    print()

# a

from operator import itemgetter

itemgetter('Part description')

# b

from operator import itemgetter

itemgetter('Price')

# c

from operator import itemgetter

itemgetter('Part description', 'Price')




# solution
invoices = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]

from operator import itemgetter

# sort the tuples by part description
for part, desc, quant, price in sorted(invoices, key=itemgetter(1)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
# sort the tuples by price
for part, desc, quant, price in sorted(invoices, key=itemgetter(3)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
# Map each invoice tuple to a tuple containing the part description
# and quantity, sort the results by quantity, then display the results.
quantities = [(desc, quant) for part, desc, quant, price in invoices]

for desc, quant in sorted(quantities, key=itemgetter(1)):
    print(f'{desc:<16}{quant:>3}')
    
# Map each invoice tuple to a tuple containing the part description and
# the value of the invoice, sort the results by the invoice value
prices = [(desc, quant * price) for part, desc, quant, price in invoices]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# Modify Part (d) to filter the results to invoice values in the range $200 to $500.
prices = [(desc, quant * price) for part, desc, quant, price in invoices\
          if 200 <= quant * price <= 500]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# Calculate the total of all the invoices. 
total = sum([(quant * price) for part, desc, quant, price in invoices])

print(f'Total for all invoices is: {total:.2f}')



