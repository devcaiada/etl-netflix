# ETL Dados Netflix

Este projeto representa um esforço concentrado para tratar e limpar dados brutos provenientes do Netflix. O objetivo principal é garantir a confiabilidade, rastreabilidade e integridade dos dados durante todo o processo de tratamento.

O projeto envolveu a coleta de várias tabelas de dados de diversos países, cada uma contendo informações únicas e valiosas. Estes dados foram então submetidos a um rigoroso processo de limpeza e tratamento, utilizando técnicas avançadas de análise de dados para garantir a precisão e a utilidade dos dados finais.

![netflix](https://github.com/devcaiada/etl-netflix/blob/main/images/Netflix_logo.svg.png?raw=true)

Após a conclusão do tratamento dos dados, os resultados foram consolidados em uma única tabela. Esta tabela final representa a síntese de todas as informações coletadas e tratadas durante o projeto. Ela foi cuidadosamente verificada para garantir sua precisão e foi exportada para a pasta ‘ready’ para uso futuro.

Este projeto demonstra um compromisso com a excelência em análise de dados e representa um passo significativo na melhoria da qualidade e utilidade dos dados do Netflix.

## Relatório - Power BI

Após o tratamento dos dados, elaborei um relatório detalhado utilizando a ferramenta Power BI. Este relatório proporciona uma visão abrangente e perspicaz dos dados tratados. Ele inclui análises sobre os tipos de planos vendidos, as vendas distribuídas por país e as vendas anuais.

![final_report](https://github.com/devcaiada/etl-netflix/blob/main/images/final_report.png?raw=true)

Além disso, o relatório destaca um dos aspectos mais importantes dos nossos dados: a relação entre a aquisição dos tipos de planos e a idade dos clientes. Esta análise nos permite entender melhor nosso público-alvo e adaptar nossos produtos e serviços de acordo.

Nossa análise revela tendências interessantes em relação à idade dos clientes e suas preferências de plano. Observamos que os clientes mais jovens têm uma inclinação para o plano básico. Isso pode ser atribuído a uma variedade de fatores, incluindo limitações orçamentárias ou simplesmente uma menor necessidade de recursos adicionais oferecidos em planos mais caros.

![age_report](https://github.com/devcaiada/etl-netflix/blob/main/images/age_report.png?raw=true)

Por outro lado, os clientes mais velhos mostram uma preferência pelo plano premium. Isso pode refletir uma maior disposição para investir em serviços de alta qualidade ou uma apreciação pelas características adicionais que o plano premium oferece, como o número de telas simultâneas.

Essas tendências nos fornecem insights valiosos sobre nossos diferentes segmentos de clientes e podem nos ajudar a personalizar nossas ofertas e estratégias de marketing para melhor atender às suas necessidades e preferências.

## O Código

Segue abaixo um exemplo da elegância e simplicidade do código Python que empregamos neste projeto. Utilizamos uma combinação de bibliotecas poderosas para realizar nossas tarefas. A biblioteca os foi usada para interagir com o Sistema Operacional, permitindo-nos manipular e navegar pelas estruturas de diretórios. A biblioteca glob foi empregada para lidar com caminhos de arquivos, proporcionando uma maneira flexível de especificar padrões de caminho.

Por último, mas certamente não menos importante, a biblioteca pandas desempenhou um papel crucial no tratamento de dados. Esta biblioteca, que se tornou um padrão de fato para a manipulação de dados em Python, nos permitiu limpar, transformar e analisar nossos dados de forma eficiente.

```python
import pandas as pd
import os
import glob


folder_path = r'data/raw'

excel_files = glob.glob(os.path.join(folder_path, '*xlsx'))


if not excel_files:
    print('Nenhum arquivo encontrado!')
else:
    dfs = []

    for excel_file in excel_files:
        try:
            df_temp = pd.read_excel(excel_file)

            file_name = os.path.basename(excel_file)

            df_temp['file_name'] = file_name

            if 'brasil' in file_name.lower():
                df_temp['country'] = 'Brasil'
            elif 'france' in file_name.lower():
                df_temp['country'] = 'França'
            elif 'italian' in file_name.lower():
                df_temp['country'] = 'Italia'

            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            dfs.append(df_temp)

        except Exception as e:
            print(f'Erro ao ler o arquivo {excel_file} : {e}')

    if dfs:

        result = pd.concat(dfs, ignore_index=True)

        output_file = os.path.join('data', 'ready', 'clean.xlsx')

        writer = pd.ExcelWriter(output_file)

        result.to_excel(writer, index=False)

        writer._save()
    else:
        print('Nenhum arquivo encontrado!')
```

Essas bibliotecas, quando usadas em conjunto, fornecem uma plataforma robusta e flexível para o tratamento de dados, demonstrando a força e versatilidade do Python para tarefas de análise de dados.
