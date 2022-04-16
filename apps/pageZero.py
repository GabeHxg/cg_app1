
import streamlit as st

def action():
    
    st.title('Previsão de preços de criptomoedas usando séries temporais históricas de mídias sociais.')

    st.markdown('''O texto a seguir descreve a **Apresentação do projeto final Awari de Data Science e Analytics**. Ela é seguida por todas as etapas do projeto, desde a **coleta de dados até as informações finais sobre o comportamento da ação do preço das criptomoedas**, cada uma com um repositório dedicado.

--- 

## O problema

Prever o comportamento do preço de um ativo tem sido um objetivo tentador na ciência de investimentos há anos, e nunca um objetivo fácil.

Para criptoativos, a **intangibilidade prática** extrapola ainda mais a **subjetividade dos métodos de avaliação**, incentivando a necessidade de **novos pontos de vista**.


## Abordagem da solução pela Lei de Metcalfe
A lei de Metcalfe, **um desses pontos de vista**, não é nada nova: concebida em **1983** em uma apresentação ao time de vendas da 3Com, **ela afirmava que o valor das tecnologias de comunicação** (especificamente a Ethernet) seria proporcional ao **número total de conexões possíveis**, ou **n^2** (**n** = usuários).

Em 1995, impressionado com a variedade de aplicações da _'principia'_ de Metcalfe, o venture capitalist **George Gilder** a chamou de **Lei de Metcalfe**. As palavras de Metcalfe: [clique aqui](https://www.youtube.com/watch?v=pPXCuf7xLsM).

A prova conceitual veio apenas em **julho de 2013**, quando pesquisadores holandeses conseguiram analisar os padrões de uso da Internet na Europa por um tempo suficiente e encontraram a proporcionalidade **n^2** para pequenos valores de **n** e **n log(n)** proporcionalidade para grandes valores de **n**, solidificando o que hoje é conhecido como '**Network Effect**'.

Alguns meses depois, **o próprio Metcalfe** forneceu mais provas, usando os dados do Facebook nos últimos 10 anos para mostrar um bom ajuste à lei de Metcalfe (o modelo é n^2).

**O que há de novo** é que há apenas 3 anos, [Peterson](https://sci-hub.se/10.2139/ssrn.3356098) vinculou **conceitos de valor do dinheiro no tempo ao valor de Metcalfe** , usando **Bitcoin** como exemplos numéricos da prova e mostrando que mais de **70% da variação** no valor do Bitcoin foi **explicada pela aplicação da lei de Metcalfe para aumentos no tamanho da rede Bitcoin**.

## Impacto
O trabalho de Peterson **não apenas contribuiu para a declaração da lei de Metcalfe**, mas usando a ação de preço do Bitcoin para fazê-lo, ele também **desencadeou o conceito de prova matemática para modelos de precificação de criptomoedas**.


## Limitações da abordagem de Metcalfe
Uma crítica antiga ([Odlyzko](https://en.wikipedia.org/wiki/Andrew_Odlyzko), [2006](https://spectrum.ieee.org/metcalfes-law-is-wrong)) afirma que ** Metcalfe está errado** ao supor que o **valor de cada nó (n, usuário) é de igual benefício** e que a aplicabilidade de sua lei é **restringida a séries temporais 'longas o suficiente'**, pois os padrões podem reduzir a discrepância de utilidade.

Portanto, com este projeto, tentaremos **encontrar uma composição de métricas de rede (um usuário composto)** que sirva como um **indicador do desempenho futuro** de um determinado criptoativo.

---


## Objetivos do projeto
Inspirado no '**Efeito de Rede**' da Lei de Metcalfe, este projeto visa recuperar insights da análise de séries temporais sobre diferentes 'Usuários' de tokens de criptografia.

Coletaremos **3 anos de dados diários**, para **50 tokens diferentes**, para as seguintes métricas:

**Dados da comunidade social**

> 'twitter_followers'

> 'reddit_subscribers'

> 'reddit_average_posts_48h'

> 'reddit_avg_comments_48h'


**Dados da comunidade de desenvolvedores** | repositório github de criptomoedas

> 'forks'

> 'stars'

> 'github_subs'

> 'total_issues'

> 'closed_issues'

> 'pull_rqst_merged'

> 'pull_request_contributors'



**Market_cap, total_volume, current_price**

> Em USD, EUR e BRL


**Ao final, estaremos em condições de responder à pergunta:**

> Alguma das variáveis ​​consideradas (ou qualquer conjuntura delas) ajuda a estimar o 'valor justo' e o 'preço futuro' de uma criptomoeda?

---

## Engenharia Analítica | Tecnologias
O fluxo de trabalho será hospedado pelos serviços do **Google Cloud Platform**.


**Processamento e armazenamento em nuvem**

O banco de dados será **armazenado no Google Storage**, atualizado por meio de um script python **programado com cron jobs**, executado em uma **máquina virtual preemptiva** do **Cloud Compute Engine**.

**Distribuição de banco de dados**

O **Google Storage** também abastecerá as tabelas no BigQuery através de uma **Google Cloud Function**, acionada diariamente, tornando os dados disponíveis para deployment por API´s e 
acessíveis por meio do **DataStudio** e do **Tableau**.
    ''')