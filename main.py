import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = "data_incl_demographics filtered.csv"

    file = open(path, "r")

    data = pd.read_csv(path, header=None, skiprows=[0])
    data.columns = pd.read_csv(path, nrows=0).columns.tolist()

    data.info()
    data.head()

    # just to test
    worried = data[data['worry'] == 'high']
    plt.plot(worried['chosen_emotion'], worried['relaxation'], 'b+')
    plt.show()
