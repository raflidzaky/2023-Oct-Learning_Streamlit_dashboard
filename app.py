import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from babel.numbers import format_currency


st.set_page_config(
                   page_title='Dashboard',
                   page_icon='📊',
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items=
                    {
                      'About': 'dzakyrafliansyah@gmail.com'
                    })


st.title('Product Sales in E-commerce',)
dashboard_dataset = pd.read_csv('dashboard_dataset.csv', parse_dates=[2,3])


min_date = dashboard_dataset['order_purchase_timestamp'].min()
max_date = dashboard_dataset['order_purchase_timestamp'].max()


with st.sidebar:
  st.header('Parameters')
  st.markdown('You can interact with the chart through this parameters 👇')
  products = st.selectbox(
                          'Select Product',
                            ('cama_mesa_banho', 'beleza_saude', 'esporte_lazer', 'moveis_decoracao', 'informatica_acessorios')
                         )
  start_date = st.date_input(
                             label='Rentang Waktu',
                             min_value=min_date,
                             max_value=max_date,
                             value=[min_date, max_date],
                            )
 


col1, col2, col3 = st.columns(3)
freight_value = format_currency(dashboard_dataset['freight_value'].mean().round(2), 'BRL', locale='es_co')
col1.metric('Rerata Freight Value', freight_value)


c1 = st.columns((9, 3))

st.markdown('### Freight Value Over Time')
dashboard_dataset['Tahun'] = dashboard_dataset['order_purchase_timestamp'].dt.year
dashboard_dataset['Month'] = dashboard_dataset['order_purchase_timestamp'].dt.month

freight_value_per_bulan = pd.DataFrame(dashboard_dataset['freight_value'].groupby(by=dashboard_dataset['Month']).mean().round(2)).reset_index(drop=False)
freight_value_per_bulan.columns = ['Month', 'Rerata']

fig, ax = plt.subplots(figsize=[10, 8])
plt.plot(freight_value_per_bulan['Month'], freight_value_per_bulan['Rerata'], marker='o')

plt.xticks(freight_value_per_bulan['Month'])
plt.ylabel('Rerata Freight Value (Brazilian Real)', fontweight='bold')
plt.xlabel('Month', fontweight='bold')

for i, count in enumerate(freight_value_per_bulan['Rerata']):
  plt.annotate(str(count), [freight_value_per_bulan['Month'][i], count], textcoords="offset points", xytext=(0, 10),
                    ha='center')

st.pyplot(fig) 

c2 = st.columns((9, 3))
top_3_product = (dashboard_dataset.groupby(('product_category_name')).size().sort_values(ascending=False)).head(3)
top_3_product_df = pd.DataFrame(top_3_product).reset_index(drop=False)
top_3_product_df.columns = ['Kategori Produk', 'Total']

figure, ax = plt.subplots(figsize=[12, 5])
top_3_product_df.plot.bar(color='blue', ax=ax)

ax.set_xticklabels(top_3_product_df['Kategori Produk'], rotation=0)
ax.set_ylabel('Total Sales')
ax.set_xlabel('Kategori Produk')
ax.bar_label(ax.containers[0], label_type='edge')

st.pyplot(figure)
