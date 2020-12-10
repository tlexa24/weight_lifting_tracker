
import pymysql.cursors
import pandas as pd
import run_log_class
import weight_log_class
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
connection = pymysql.connect(host='localhost', user='root', password='troopsix', db='fitness', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

if __name__ == '__main__':
    while True:
        print('1. Log lift \n'
              '2. Log run \n'
              '3. Log weight \n'
              '4. Log diet\n'
              '5. Get exercise routine for next 4 days\n'
              '6. View information')
        choice = input('Enter one of the numbers above: ')
        try:
            if int(choice) in range(1, 6):
                break
            else:
                raise ValueError
        except ValueError:
            print("\nOnly enter one of the following numbers.\n")
            continue
    # if choice == '1':
    if choice == '2':
        run = run_log_class.create_run_instance()
        run.insert()
    if choice == '3':
        weight = weight_log_class.create_weight_instance()
        weight.insert()
    # if choice == '4':
    # if choice == '5':
    # if choice == '6':
