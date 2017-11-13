

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

```


```python


d1 = pd.read_excel('population.xls')
d2 = pd.read_excel('restaurant.xls')
d3 = pd.read_excel('stores.xls')
d4 = pd.read_excel('tax.xls')
```

# Final Data Wrangling - Merging Clean Datasets


```python
result = pd.concat([d1, d4], axis=1, join_axes=[d1.index])
```


```python
result.head()
```


```python
result2 = pd.concat([d2, d3], axis=1, join_axes=[d2.index])
```


```python
result2.head()
```


```python
final = pd.concat([result, result2], axis=1, join_axes=[result.index])
```


```python
final.head()
```


```python
final.to_excel('final.xls', index=False)
```

# Modeling Starts Here


```python
test = pd.read_excel('final.xls')

```


```python
test.dtypes
```




    State                                         object
    County                                        object
    2010 Census Population                        object
    Population Estimate, 2014                     object
    Food & Retail Tax 2014                       float64
    Fast Food 2009                                 int64
    Fast Food 2014                                 int64
    Fast Food % Change 09-14                     float64
    Full Service 2009                              int64
    Full Service 2014                              int64
    Full Service % Change 09-14                  float64
    Grocery Store 09                               int64
    Grocery Store 2014                             int64
    Grocery Store % Change 09-14                 float64
    Supercenters & Club Stores 2009                int64
    Supercenters & Club Stores 2014                int64
    Supercenters & Club Stores % Change 09-14    float64
    Convenience Stores 2009                        int64
    Convenience Stores 2014                        int64
    Convenience Stores % Change 09-14            float64
    Specialized Food Stores 2009                   int64
    Specialized Food Stores 2014                   int64
    Specialized Food Stores % Change 09-14       float64
    dtype: object




```python

```


```python
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
feature_cols = ['Fast Food 2009']
feature_cols2 = ['Fast Food 2014']
X = test[feature_cols]
y = test[feature_cols2]
logreg.fit(X, y)
assorted_pred_class = logreg.predict(X)
```

  
    


```python
test.shape
```




    (3142, 23)




```python
assorted_pred_class
```




    array([19, 19, 10, ..., 10, 10,  5], dtype=int64)




```python
test['assorted_pred_class'] = assorted_pred_class
```


```python
plt.scatter(test[feature_cols], test[feature_cols2])
plt.plot(test[feature_cols], test.assorted_pred_class, color='green');
```


![png](output_18_0.png)



```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
