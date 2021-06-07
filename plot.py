#import main.py
import matplotlib.pyplot as plt
import seaborn as sns
def count_chart(column_name):
    '''To plot a chart to have count of the entries in that 
       particular column.'''
    sns.set_theme(style="darkgrid")
    ax = sns.countplot(x=column_name, data=data)
def heatmap_chart():
    '''To obtain the heatmap which gives the overall correlation
    of the attributes in the dataset.'''
    plt.figure(figsize=(20,20))  
    sns.heatmap(data.corr(), annot=True, fmt='.0%')

#Function_call
count_chart("diagnosis")
heatmap_chart()
