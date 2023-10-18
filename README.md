# Dashboard Streamlit 📈

# Set Environment di Google Colab
```
# Upload data terlebih dahulu
# Read Data
import pandas as pd
dashboard_dataset = pd.read_csv('dashboard_dataset.csv', parse_dates=[2, 3])

# Install streamlit
!pip instal streamlit

# Set Workfile untuk Code Streamlit
# Seluruh code yang digunakan untuk build elements hingga layout dashboard akan diletakkan di workfile ini
# penamaan file .py dapat disesuaikan dengan kebutuhan
%%writefile app.py 
import streamlit as st
import matplotlib.pyplot as plt

# Mendapatkan Endpoint IP untuk LocalTunnel
!wget -q -O - ipv4.icanhazip.com

# Set App di Port Local
!streamlit run app.py & npx localtunnel --port 8501

# Kode streamlit di workfile .py akan otomatis run dalam localtunnel
```

# URL Dashboard pada Streamlit Community Cloud 
https://dashboard-app-u2hzj7c3dofxykpegebdbv.streamlit.app/

# Mock Dashboard
![Screenshot (2907)](https://github.com/raflidzaky/dashboard-streamlit/assets/104545005/4b839849-dfba-4c9d-a10a-d8e457b80655)
