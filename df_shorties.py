import pandas as pd

def set_defaults():
    pd.set_option('display.height', 100000)
    pd.set_option('display.max_rows', 10000)
    pd.set_option('display.max_columns', 10000)
    pd.set_option('display.width', 10000)
    return

def makeCSV(dataframe, csv_name, path='~/csvs'):
    ''' take a DF and a CSV name, create the CSV and move it to the CSV directory.
        provide a custom path to mv the csv to, else it will default to ~/csvs'''
    if not csv_name:
        print "failed to create csv because no name passed in"
        return
    dataframe.to_csv(csv_name)
    os.system("mv %s %s" % (csv_name, path))
    return 
