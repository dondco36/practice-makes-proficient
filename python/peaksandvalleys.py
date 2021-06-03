# - Peaks and Valleys - #

# Data to be run through
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks = []
valleys = []
counter = 0

for i in range(1, len(data) - 1):
    counter += 1
    if data[i] > data[i-1] and data[i] > data[i+1]:
        peaks.append(counter)
    elif data[i] < data[i-1] and data[i] < data[i+1]:
        valleys.append(counter)

pv = peaks + valleys

print(f'Peaks: {peaks}')
print(f'Valleys: {valleys}')
print(f'Peaks and Valleys: {pv}')

## Next up is returning list with 'X' drawring the peaks and valleys ##

# peak = []
# valley = []
# coutner = 0
# big_num = 0

# to be continued #