import csv

def read_csv(csv_file):
    return

def all_time_high(data):
    return

def all_time_low(data):
    return

def percent_change(data, start, end):
    return

def largest_intraday_percentage_change(data):
    return

def run_tests():
    return

if __name__ == '__main__':
    btc_data = read_csv('BTCUSD_day.csv')
    run_tests()

    print('Analysis of BTC/USD Price Data')
    ath_date, ath_price = all_time_high(btc_data)
    print('BTC/USD reached its all time high on {} at a price of ${:.2f}'.format(ath_date, ath_price))

    atl_date, atl_price = all_time_low(btc_data)
    print('BTC/USD reached its all time low on {} at a price of ${:.2f}'.format(atl_date, atl_price))

    date1 = '2015-10-09'
    date2 = '2021-03-08'
    print('Percent change from {} to {}: {:.2f}%'.format(date1, date2, percent_change(btc_data, date1, date2)))

    idc_date, idc_price = largest_intraday_percentage_change(btc_data)
    print('Largest intraday change occurred on {} and was {:.2f}%'.format(idc_date, idc_price))