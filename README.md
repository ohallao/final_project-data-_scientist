# **Projeto Final - Cientista de Dados**

## **Visão Geral do Projeto**

Este projeto aborda a construção de um pipeline completo de modelagem preditiva, desde o tratamento dos dados até a criação de uma aplicação interativa em Streamlit para escoragem.

### **Desenho Amostral**
- Utilização de **15 safras**.
- Análise baseada em **12 meses de performance**.

### **Variáveis e Pré-processamento**
- Seleção e transformação de variáveis com **Weight of Evidence (WOE)**.
- Tratamento de valores nulos com pipeline do `sklearn`.
- Remoção de outliers com **EllipticEnvelope**.
- Seleção de variáveis com **RandomForestClassifier**.
- Redução dimensional com **PCA** (5 componentes principais).
- Criação de variáveis dummies.

### **Modelos Utilizados**
- **Regressão Logística** com `statsmodels`.
- Pipeline no `sklearn` com:
  - Tratamento de nulos.
  - Remoção de outliers.
  - Seleção de variáveis.
  - PCA.
  - Criação de dummies.
- Modelo avançado com **LightGBM**, treinado via **PyCaret**.

### **Validação Out of Time (OOT)**
- Separação de uma base de teste com os **três últimos meses** para validação.

### **Aplicação Web (Streamlit)**
- Aplicação disponível no arquivo `projeto_final.py`.
- Permite **carregar bases de dados** e **gerar previsões** exportadas em planilhas.

[![Assistir ao vídeo](https://via.placeholder.com/600x400.png?text=Assistir+ao+vídeo)](https://github.com/ohallao/final_project-data_scientist/blob/680ca31455dc085f30f8ba52deff50032b41bf29/Streamlit_Projeto_Final.webm)
---

## **Como Executar**

1. Clone este repositório:
   ```bash
   git clone https://github.com/ohallao/final_project-data_scientist.git
   cd final_project-data_scientist
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Execute a aplicação:
   ```bash
   streamlit run Streamlits/projeto_final.py
4. Faça o upload de um arquivo .csv para realizar as previsões.
   
## **Tecnologias Utilizadas**
- Python: Desenvolvimento de scripts e pipelines.
- Streamlit: Interface web interativa.
- PyCaret: Treinamento e avaliação de modelos.
- Sklearn: Pré-processamento e modelagem.
- Pandas/Numpy: Manipulação de dados.
