import statistics
import csv
import pandas as pd

df=pd.read_csv("height-weight.csv")

height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

#mean and median and mode: 

weight_mean=statistics.mean(weight_list)
height_mean=statistics.mean(height_list)

print("Mean of weight:",weight_mean)
print("Mean of height:",height_mean)

weight_median=statistics.median(weight_list)
height_median=statistics.median(height_list)

print("Median of weight:",weight_median)
print("Median of weight:",height_median)

weight_mode=statistics.mode(weight_list)
height_mode=statistics.mode(height_list)

print("Mode of weight:",weight_mode)
print("Mode of height:",weight_mode)

height_std_deviation=statistics.stdev(height_list)
weight_std_deviaition=statistics.stdev(weight_list)

height_first_std_deviation_start, height_first_std_deviation_end= height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end= height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end= height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

weight_first_std_deviation_start, weight_first_std_deviation_end= weight_mean-weight_std_deviaition, weight_mean+weight_std_deviaition
weight_second_std_deviation_start, weight_second_std_deviation_end= weight_mean-(2*weight_std_deviaition), weight_mean+(2*weight_std_deviaition)
weight_third_std_deviation_start, weight_third_std_deviation_end= weight_mean-(3*weight_std_deviaition), weight_mean+(3*weight_std_deviaition)

height_list_of_data_within_1_std_deviation=[result for result in height_list if result > height_first_std_deviation_start and result<height_list]
height_list_of_data_within_2_std_deviation=[result for result in height_list if result > height_second_std_deviation_start and result<height_list]
height_list_of_data_within_3_std_deviation=[result for result in height_list if result > height_third_std_deviation_start and result<height_list]

weight_list_of_data_within_1_std_deviation=[result for result in weight_list if result > weight_first_std_deviation_start and result<weight_list]
weight_list_of_data_within_2_std_deviation=[result for result in weight_list if result > weight_second_std_deviation_start and result<weight_list]
weight_list_of_data_within_3_std_deviation=[result for result in weight_list if result > weight_third_std_deviation_start and result<weight_list]

print("{}% of data for height lies within 1 std".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 std".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 std".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 std".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 std".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 std".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))































