import os
import pandas as pd
import streamlit as st

from io import BytesIO
from sklearn.preprocessing import StandardScaler
from pycaret.classification import setup, load_model, predict_model

# Função para converter DataFrame para CSV
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função para converter DataFrame para Excel
@st.cache_data
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()  # Atualizado
    processed_data = output.getvalue()
    return processed_data

def main():
    # Configuração da página
    st.set_page_config(
        page_title='Projeto Final',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    st.write('## Avaliando o modelo gerado no Pycaret')
    st.markdown('---')

    # Upload de arquivo
    st.sidebar.write('## Suba o arquivo')
    data_file_1 = st.sidebar.file_uploader('Bank Credit Dataset', type=['csv', 'ftr'])

    if data_file_1 is not None:
        # Leitura do arquivo de dados
        df_credit = pd.read_feather(data_file_1)
        df_credit = df_credit.sample(50000)
        df_credit['bom'] = 1 - df_credit.mau

        # Configuração do PyCaret
        pipe = setup(
            data=df_credit,
            target='mau',
            numeric_imputation='mean',
            normalize=True,
            remove_outliers=True,
            pca=True,
            pca_components=5,
            normalize_method='zscore',
            transformation=True,
            transformation_method='quantile',
            fix_imbalance=True
        )

        # Carregando o modelo treinado
        model_path = os.path.join(os.getcwd(), 'pycaret_model')  # Certifique-se que o modelo esteja neste diretório
        model_saved = load_model(model_path)

        # Fazendo previsões
        predict = predict_model(model_saved, data=pipe.X)

        # Baixar o arquivo Excel
        df_xlsx = to_excel(predict)
        st.download_button(
            label='Download Previsões',
            data=df_xlsx,
            file_name='predict.xlsx',  # Corrigido
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

if __name__ == '__main__':
    main()
