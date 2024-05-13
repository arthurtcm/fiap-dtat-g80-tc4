# fiap-dtat-g80-tc4

# App

O App é um dash criado utilziando o streamlit, feito para prever o Preço do Petróleo Bruto utilizando a base de dados fornecida pelo IPEADATA.

Para executá-lo localmente, primeiro rodar a Lambda Baixar Dados, e a Lambda Criar Modelo. Depois disso só executar o comando python -m streamlit run app/app.py

# Lambda Baixar Dados

O arquivo lambda_handler_baixar_dados.py baixa os dados que serão usados e salva em um csv. Para rodá-lo local, só executar o arquivo.

# Lambda Criar Modelo

O arquivo lambda_handles_criar_modelo.py cria o modelo e salva como um pkl. Para rodá-lo local, só executar o arquivo.
