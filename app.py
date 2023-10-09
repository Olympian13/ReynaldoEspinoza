import streamlit as st
import pandas as pd
import numpy as np
st.write("US Housing")
df_housing = pd.read_csv("USA_Housing.csv")
import matplotlib.pyplot as plt
df_housing_2 = df_housing[['Avg. Area Income', 'Price']].copy()


st.dataframe(df_housing)

st.scatter_chart(df_housing_2, x = 'Avg. Area Income', y = 'Price')
