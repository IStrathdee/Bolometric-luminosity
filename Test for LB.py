import pandas as pd 
import scipy

#begin with finding the bolometric corrected luminosities of the galaxies 
#import the correction table and get python to read ecah column
lxcorr_table = pd.read_csv('lglx_kbol_tuv09.csv')

xp = lxcorr_table["LX_hard_corr"]
#print(xp)
fp = lxcorr_table["bolometric_correction"]
#print(fp)

lx_data_point = pd.read_csv('xL data points.csv')
x = lx_data_point["Log(L)"]
#pd.Series(['Log(L)']).convert_objects(convert_numeric=True)
# x = float(x)
print(x) 

for i in x:
  arr2 = np.interp(x, xp, fp)
print (arr2) 
