import pandas as pd
import json

result = []
with open('prices.json') as f:
    page = json.load(f)
# print(page['hasMenu']['hasMenuSection'][0]['hasMenuItem'][0])

for drink_type in page['hasMenu']['hasMenuSection']:
    catagory = drink_type['name']
    print('---', catagory, '---')

    for drink in drink_type['hasMenuItem']: 
        drink_name = drink['name']
        drink_size = 'Grande'
        drink_price = drink['offers']['price']


        result.append([drink_name, drink_size, drink_price])

columnNames = ['drink_name', 'size', 'drink_price']
df = pd.DataFrame(result, columns=columnNames)

df.to_csv(path_or_buf='sbux_prices.csv', index=False)
print("----- Finished! -----")