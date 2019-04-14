import numpy as np
import pandas as pd


X=pd.Series([1,2,3,4,5])

X+100

(X**2)+100

X>2

larger_than2 = X>2
larger_than2.any()
larger_than2.all()



def f(X):
    if X%2==0:
        return X**2
    else:
        return X**3


X.apply(f)


X.astype("float64")


Y=X.copy()


Y[0]=100


data=[0,1,2,3,4,5,6,7,8,9]
df=pd.DataFrame(data,columns=["x"])


df["x_plus_2"]=df["x"]+2


df["x_square"]=df["x"]**2

df["x_factorial"]=df["x"].apply(np.math.factorial)


df.drop("x_square",1)

df.describe()



dataset = pd.read_csv("matches.csv")





