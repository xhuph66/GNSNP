from math import sqrt
from matplotlib import pyplot
import numpy as np
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

count=1
count1=1
dataset_name="USDCNY"
for i in range(30):
    origin = read_csv('./GNSNP/CNYUSD/origin/' + str(i+1) + '_cnyusd.csv', delimiter=',',header=None).values
    predictions=read_csv('./GNSNP/CNYUSD/prediction/' + str(i+1) + '_cnyusd.csv', delimiter=',',header=None).values
    rmse = sqrt(mean_squared_error(origin, predictions))
    mse = mean_squared_error(origin, predictions)
    mae = mean_absolute_error(origin, predictions)
    mape = mean_absolute_percentage_error(origin, predictions)
    meanV = np.mean(origin)
    error = abs(origin - predictions)
    print(dataset_name + ' Test RMSE: %.15f ,MAE: %.15f ,MSE: %.15f ,MAPE: %.15f ' % (rmse, mae,mse, mape))


    # predicted
    fig4 = pyplot.figure()
    ax41 = fig4.add_subplot(111)
    pyplot.xticks(fontsize=15)
    pyplot.yticks(fontsize=15)
    ax41.set_xlabel("Time", fontsize=15)
    ax41.set_ylabel("Magnitude", fontsize=15)
    pyplot.plot(origin, '-', label='the original data')
    pyplot.plot(predictions, '--', label='the GNSNP predicted data')
    pyplot.legend()
    pyplot.title(dataset_name)
    count = count + 1
    pyplot.show()

    # error
    fig1 = pyplot.figure()
    ax42 = fig1.add_subplot(111)
    pyplot.xticks(fontsize=15)
    pyplot.yticks(fontsize=15)
    ax42.set_xlabel("Time", fontsize=15)
    ax42.set_ylabel("Magnitude", fontsize=15)
    pyplot.plot(error, '-', label='the GNSNP error data')
    pyplot.legend()
    pyplot.title(dataset_name)
    count1 = count1 + 1
    pyplot.show()
