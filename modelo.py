import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Exemplo de dados: [tamanho, quartos], preço
X = np.array([
    [100, 3],
    [150, 4],
    [120, 2],
    [300, 5],
    [200, 3],
    [250, 4],
    [180, 3],
    [140, 2],
    [320, 5],
    [210, 3]
])
y = np.array([200000, 300000, 180000, 500000, 400000, 450000, 360000, 220000, 520000, 410000])

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Avaliando o modelo com o conjunto de teste
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse}")

# O modelo agora pode ser usado para fazer previsões

import joblib

# Salvando o modelo treinado
joblib.dump(modelo, 'modelo_casas.pkl')