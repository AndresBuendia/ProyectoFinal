
import streamlit as st
import pandas as pd
import numpy as np
import talib

def load_data(symbol):
    # Esta función simula la carga de datos históricos para una criptomoneda
    # En una aplicación real, se conectaría a una API o base de datos
    date_rng = pd.date_range(start='1/1/2022', end='1/10/2022', freq='H')
    df = pd.DataFrame(date_rng, columns=['date'])
    df['price'] = np.random.random(size=(len(date_rng))) * 10000
    return df

def calculate_indicators(df):
    # Calcular indicadores técnicos, ejemplo simple
    df['SMA'] = talib.SMA(df['price'], timeperiod=14)
    return df

def main():
    st.title('Aplicación de Trading de Criptomonedas')

    # Selector de criptomonedas
    option = st.selectbox(
        '¿Qué criptomoneda te gustaría analizar?',
        ('BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'LTC/USDT')
    )

    # Carga de datos
    data = load_data(option)
    data = calculate_indicators(data)

    # Mostrar datos
    st.write('Datos de la Criptomoneda Seleccionada:', data.tail())

    # Visualización de indicadores técnicos
    st.line_chart(data[['price', 'SMA']])

if __name__ == '__main__':
    main()
