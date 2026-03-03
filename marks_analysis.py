import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ID=np.arange(2326107037,2326107137)
np.size(ID)
maths=np.random.randint(40,101,100)
science=np.random.randint(40,101,100)
english=np.random.randint(40,101,100)
bins=[0,50,60,70,80,90,100]
labels=["fail",'E','D','C','B','A']
data={"ID_NO":ID,"Maths":maths,"Science":science,"English":english}
df=pd.DataFrame(data)
df["total"]=df["Maths"]+df["Science"]+df["English"]
df["average"]=df["total"]/3
df["Grade"]=pd.cut(df["average"],bins=bins,labels=labels )
print(df.to_string())


#plotting --> bar
sub_avg=[df["Maths"].mean(),df["Science"].mean(),df["English"].mean()]
subjects=["Maths","Science","English"]
plt.bar(subjects,sub_avg)
plt.xlabel("subjects")
plt.ylabel("average marks")
plt.title("average marks visualization")
plt.show()

#plotting --> histogram
plt.hist(df["average"],bins=10)
plt.xlabel("average marks")
plt.ylabel("no of students")
plt.title("average marks visualization Hist")
plt.show()

# plotting -->piechart

plt.pie(df["Grade"].value_counts(),labels=df["Grade"].value_counts().index,autopct='%1.1f%%')
plt.legend( title="marks distribution",
    loc="center left",
    bbox_to_anchor=(1, 0.5))
plt.title("grade distribution")
plt.show()

