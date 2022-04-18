
import streamlit as st

def action():
    
    st.markdown('''
    O objetivo dessa página é detalhar os passos deste projeto. 

    Aqui, você deve encontrar links para repositórios no github, python scripts e os notebooks 
    usados para a **extração**, **tratamento**,**armazenamento**, **atualização** e **distribuição** da base de dados 
    que alimenta as análises apresentadas. 

    --- 

    # Extração e tratamento

    Para a extração de dados em tempo real, foi usada a [API](https://www.coingecko.com/en/api) 
    da plataforma Coingecko.
    Um pouco mais sobre o [wrapper](https://github.com/man-c/pycoingecko) (não oficial) usado,
    sua instalação e exemplo de usabilidade pode ser encontrado neste breve [post](https://medium.com/@Gabrielhxg/connecting-python-to-coingeckoapi-83026b72455a).
   
    --- 

    ##### Primeiro passo 
    **Quantos tokens diferentes tem na API? Quais São Relevantes?**

    Como o projeto se propõe a acompanhar métricas diárias de criptomoedas, o primeiro passo foi 
    identificar aquelas de maior relevância. Existem mais de 12 mil tokens listados na plataforma da Coingecko, 
    muitos deles são [**crypto-derivatives**](https://research.aimultiple.com/crypto-derivatives/#:~:text=Cryptocurrency%20derivatives%20exchange%20can%20be,otherwise%20be%20inaccessible%20to%20you.) 
    e nao têm efeito para nossa análise, já que não são propriamente projetos de criptocurrency.

    O notebook comentado de todo o processo pode ser encontrado [aqui](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Database%20building%20workflow/Coin%20Gecko%20API%20%7C%20Extraction.ipynb).

    --- 
    
    ##### Segundo passo 
    **Quais são os 50 mais relevantes?**

    Terminamos o primeiro passo com cerca de 5 mil projetos, todos rastreados pela API em relação às métricas relevantes para esses projeto.
    Como a API utilizada possui limitação de _requests_ (50 requests/min), nossa **watchlist** foi limitada à
    exatamente 50 tokens, para otimização de custos de **storage**. 
    > Nada impede a escalabilidade deste workflow para acompanhar todos eles, a não ser o custo citado.

    O notebook (e o algoritmo) responsável pela seleção dos 50 tokens mais relevantes pode ser consultado [aqui](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Database%20building%20workflow/Finding%20top%2050%20%7C%20cgAPI.ipynb).

    --- 
    
    ##### Terceiro passo 
    **Criação de séries temporais.**

    Nosso objetivo é analisar como essas métricas se comportam em relação ao tempo. Por isso, o terceiro
    passo é dedicado à criação das séries temporais através de requests diários de cada um das 50 criptomoedas. 

    **Resumo da ópera:** Para coletar a série histórica de 1000 dias de uma moeda, é necessário fazer 1000 requests para a API. 
    Para 50 moedas e 1095 dias (3 anos) de análise, isso significa cerca de 55 mil requests. Considerando a limitação da API de 50 requests/min, 
    a coleta desses dados demora cerca de 18 horas. 

    [Este](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Updating%20workflow/preOperations.ipynb) 
    notebook detalha as automatizações de requests para criação das séries temporais (1095 dias). 
    E [este](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Database%20building%20workflow/csv_final_prep.ipynb),
    detalha o tratamento e armazenamento local destes dados, condicionando-os à alimentação inicial da nossa base em nuvem. 

    ---

    # Armazenamento em Nuvem 
    Existem muitas vantagens no ambiente Cloud, a principal delas é **escalabilidade**, mas a verdade intrínseca está na **distribuição**.
    O objetivo dos próximos passos é tornar os dados armazenados localmente acessíveis à plataformas online.
    
    ##### Quarto passo 
    **Google Cloud Storage**

    Aramazenaremos os dados no cloud Storage, lá ele ficará disponível ao Google BigQuery (consequentemente ao Streamlit, Databricks, Data Studio, Tableau, Power BI).
    [Este](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Updating%20workflow/GCP%20Storage%20Transfering.ipynb) notebook detalha a conexão com o Google Client API, 
    e a transferência dos dados locais aos buckets do GCP. 

    ---

    # Atualização
    A peculiaridades de séries temporais é que elas perdem relevância exponencialmente. 
    Caso não sejam atualizadas (diária, mensal ou anualmente), perdem valor a cada dia. 

    ##### Quinto passo 
    **Deploy do script de atualização ao ambiente Cloud**

    Para que o data warehouse seja atualizado de forma automatizada, o GCP disponibiliza o uso de **_Virtual Machines_**, 
    responsáveis pela computação independente necessária (acesso à API e atualização de GStorage buckets). 

    Para redução de custos com máquinas virtuais, usaremos **_Preemptible Vitrual Machines_** (PVM), 
    que são acionadas apenas quando necessário. Além de acionarmos a PVM através do **Cloud Scheduler**, 
    adicionaremos **Cron Jobs** para acionar [este](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Updating%20workflow/daily_gs_update.ipynb) script, 
    que atualiza diariamente nossa base de dados. 
    
    ---
    ''')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
            # Distribuição
            Outra funcionalidade do **Google Cloud Platform** é a **Cloud Function**. 

            ##### Sexto passo 

            [Este](https://github.com/Gabrielhxg/streamlit_cg/blob/master/Updating%20workflow/GStoBQ_cloudFunction.ipynb) script, 
            quando acionado pela **Cloud Function**, será responsável pela tranferência dos dados 
            do **Cloud Storage** para o **BigQuery**, sempre que o último bucket for atualizado pelas máquinas virtuais. 

            ---

            Depois desses passos, os dados estão disponíveis através de links do **Google BigQuery Client API**, 
            e prontos para o cloud deployment desse Streamlit App.

            Ao lado, você pode observar o database workflow do projeto.
            ''')

    with col2:
        st.graphviz_chart('''
            digraph {Coingecko_API -> initialFeed_onPrem 
                    initialFeed_onPrem -> Cloud_Storage
                    Coingecko_API -> Preemptible_VM
                    Preemptible_VM -> Cloud_Storage
                    Cloud_Storage -> Cloud_Functions
                    Cloud_Storage -> BigQuery
                    Cloud_Functions -> BigQuery
                    BigQuery -> BigQuery_ClientAPI
                    BigQuery -> Streamlit
                    BigQuery_ClientAPI -> Streamlit
                    }
                            ''')
