import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Statystyki Graczy NBA')

st.markdown(""" Aplikacja ta wykonuje prosty webscraping graczy NBA i ich statysyk
* **Biblioteki python:** base64, pandas, streamlit
* **Zródła danych:** [Basketball-reference.com](https://www.basketball-reference.com/) """)

# Sidebar - Wyświetlanie w określonych latach
st.sidebar.header('Twoje Filtry') 
selected_year = st.sidebar.selectbox('Lata', list(reversed(range(1950,2020)))) 

# Web scraping graczy NBA
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Usuwa powtarzające się nagłówki
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Wybór drużyny
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Drużyna', sorted_unique_team, sorted_unique_team)

# Sidebar - Wybór na jakiej pozycji gra gracz
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Pozycja', unique_pos, unique_pos)

# Filtrowanie danych
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Statysyki graczy z wybranych drużyn.')
st.write('Rozmiar Danych: ' + str(df_selected_team.shape[0]) + ' Wierszy i ' + str(df_selected_team.shape[1]) + ' Kolumn.')
st.dataframe(df_selected_team)


# Pobieranie statysyk graczy
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.button('Interkorelacje'):
    st.header('Mapa Interkorelacji')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()