#2
cupcakes_file = open('CupcakeInvoices.csv')

#3
for line in cupcakes_file:
    print(line)
cupcakes_file.seek(0)

#4
for line in cupcakes_file:
    print(line.strip().split(',')[2])
cupcakes_file.seek(0)

#5
for line in cupcakes_file:
    line_arr = line.strip().split(',')
    quantity = int(line_arr[3])
    price = round(float(line_arr[4]), 2)
    print(round((quantity * price), 2))
cupcakes_file.seek(0)

#6
total = 0
for line in cupcakes_file:
    line_arr = line.strip().split(',')
    quantity = int(line_arr[3])
    price = round(float(line_arr[4]), 2)
    total += price * quantity
print(round(total,2))
cupcakes_file.close()

#Part 3
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

cupcakes_file = open('CupcakeInvoices.csv')

choc_total = 0
van_total = 0
straw_total = 0

for line in cupcakes_file:
    line_arr = line.strip().split(',')
    type = line_arr[2]
    quantity = int(line_arr[3])
    price = round(float(line_arr[4]), 2)
    total = quantity * price
    if type == "Chocolate":
        choc_total += total
    elif type == "Vanilla":
        van_total += total
    elif type == "Strawberry":
        straw_total += total

cupcakes_file.close()
labels = np.array(["Chocolate", "Vanilla", "Strawberry"])
totals = np.array([round(choc_total,2), round(van_total,2), round(straw_total,2)])

plt.bar(labels, totals)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
