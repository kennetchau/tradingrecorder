# python 3 
# tradingrecorder.py
# obj: ask the user for stock trade and save them in a pandas dataframe

import pandas as pd
from datetime import datetime as dt
# ask the user for inputs and parse it using space
def partinputs(string):
	inputs = string.split()
	return inputs


# main function
def main():
	#create an empty dateframe with the variables of your record:
	df = pd.DataFrame(columns=['Currency','Action','Type','Company','Quantity','Amount'])
	choice = input("Which account are you trading today?\n")
	promote = ''
	while promote.upper() != 'Q':
		promote = input("Please enter your trade record as follows 'Currency Action Type Company Quantity Amount', if you want to quit press q:\n")
		if promote.upper() != 'Q':
			record = partinputs(promote.upper())
			now = dt.now()
			current_time = now.strftime('%m/%d/%Y, %H:%M:%S')
			print(current_time)
			df.loc[current_time]=[record[0],record[1],record[2],record[3],record[4],record[5]]
			print(df)
		if promote.upper() == 'Q':
			csv_name = '{}-trade-record.csv'.format(choice)
			df.to_csv(csv_name)



