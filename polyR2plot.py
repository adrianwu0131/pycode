import pandas as pd
import numpy
import matplotlib.pyplot as plt
df = pd.read_csv('收盤價.csv')
#print (df.columns)

x=df.index.values.tolist()
y=df['0050'].values.tolist()
l=len(df.index.values.tolist())
#--------------------------------------------
def polyfit(x, y, degree):
    results = {}

    coeffs = numpy.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()
    
    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot
    return results
#--------------------------------------------
    
print(polyfit(x,y,30))
p3 = numpy.poly1d(numpy.polyfit(x, y, 30))
xp = numpy.linspace(0, l, 1000)
plt.plot(x,y,'.',xp,p3(xp),'r--')
plt.show()