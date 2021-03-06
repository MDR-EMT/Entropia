# -*- coding: utf-8 -*-
"""PCA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JoAq7E3qtaY_MvsUuThbEZDjYdhoL9ss
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#cargamos los datos de entrada
dataframe = pd.read_csv(r"soil_Rendimiento.csv")
print(dataframe.tail(10))

#normalizamos los datos
scaler=StandardScaler()
df = dataframe.drop(['Rendimiento'], axis=1) # quito la variable dependiente "Y"
scaler.fit(df) # calculo la media para poder hacer la transformacion
X_scaled=scaler.transform(df)# Ahora si, escalo los datos y los normalizo

#Instanciamos objeto PCA y aplicamos
pca=PCA(n_components=9) # Otra opción es instanciar pca sólo con dimensiones nuevas hasta obtener un mínimo "explicado" ej.: pca=PCA(.85)
pca.fit(X_scaled) # obtener los componentes principales
X_pca=pca.transform(X_scaled) # convertimos nuestros datos con las nuevas dimensiones de PCA
 
print("shape of X_pca", X_pca.shape)
expl = pca.explained_variance_ratio_
print(expl)
print('suma:',sum(expl[0:]))
#Vemos que con 5 componentes tenemos algo mas del 85% de varianza explicada

# Commented out IPython magic to ensure Python compatibility.
# Para que grafique
# %matplotlib inline 

# Tamaño y metodo
plt.rcParams['figure.figsize'] = 16, 9 # dimensiones de la figura
plt.style.use('ggplot')

# Graficamos el acumulado de varianza explicada en las nuevas dimensiones
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
plt.show()