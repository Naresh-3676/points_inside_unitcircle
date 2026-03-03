import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.random.uniform(-1,1,100)
y=np.random.uniform(-1,1,100)
z=np.random.uniform(-1,1,100)
w=np.random.uniform(-1,1,100)
df=pd.DataFrame()
df["x_values"]=x
df["y_values"]=y
df["z_values"]=z
df["w_values"]=w
df["x^2+y^2"]=df["x_values"]**2+df["y_values"]**2
df["x^2+y^2<=1"]=np.where(df["x^2+y^2"]<=1,"true","false")
df["x^2+y^2+z^2"]=df["x_values"]**2+df["y_values"]**2+df["z_values"]**2
df["x^2+y^2+z^2<=1"]=np.where(df["x^2+y^2+z^2"]<=1,"true","false")
df["x^2+y^2+z^2+w^2"]=df["x_values"]**2+df["y_values"]**2+df["z_values"]**2+df["w_values"]**2
df["x^2+y^2+z^2+w^2<=1"]=np.where(df["x^2+y^2+z^2+w^2"]<=1,"true","false")

print(df.to_string())
 
fig,axes=plt.subplots(1,3)
#  pie chart plotting 2-d
axes[0].pie(df["x^2+y^2<=1"].value_counts(),labels=df["x^2+y^2<=1"].value_counts().index,autopct='%1.1f%%')
axes[0].set_title(" x^2+y^2<=1 ")
#2nd plot 3-d
axes[1].pie(df["x^2+y^2+z^2<=1"].value_counts(),labels=df["x^2+y^2+z^2<=1"].value_counts().index,autopct='%1.1f%%')
axes[1].set_title(" x^2+y^2+z^2<=1 ")
#3 rd plot 4-d
axes[2].pie(df["x^2+y^2+z^2+w^2<=1"].value_counts(),labels=df["x^2+y^2+z^2+w^2<=1"].value_counts().index,autopct='%1.1f%%')
axes[2].set_title(" x^2+y^2+z^2+w^2<=1 ")
plt.show()

