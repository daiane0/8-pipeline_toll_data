## Análise de tráfego rodoviário
Este projeto tem como objetivo analisar dados de tráfego rodoviário de diferentes praças de pedágio, visando contribuir para a descongestionamento das rodovias nacionais. O projeto consiste em realizar a extração, transformação e carga de dados (ETL), criar um pipeline de dados e carregar os dados em um banco de dados. O projeto utiliza as tecnologias Apache Airflow e Kafka.

## Descrição
### Parte 1: Airflow
Consolidar dados de diferentes formatos de arquivos provenientes de diferentes praças de pedágio em um único arquivo. Cada rodovia é operada por um operador de pedágio com uma configuração de TI distinta, resultando no uso de diferentes formatos de arquivo.

Foi desenvolvido um DAG (Directed Acyclic Graph) no Apache Airflow para:
  - Extrair dados de arquivos CSV, TSV e de largura fixa.
  - Realizar transformações nos dados.
  - Carregar os dados transformados na área de estágio.

### Parte 2: Kafka

criar um pipeline de dados em tempo real para coletar dados de tráfego rodoviário de diferentes praças de pedágio conforme os veículos passam pelas praças. Os dados dos veículos, como ID do veículo, tipo de veículo, ID da praça de pedágio e timestamp, são transmitidos para o Kafka em tempo real.

Foram realizadas as seguintes etapas para criar um pipeline de dados em tempo real:
  - Iniciar um servidor de banco de dados MySQL.
  - Criar uma tabela para armazenar os dados de pedágio.
  - Iniciar o servidor Kafka.
  - Instalar o driver Python do Kafka.
  - Instalar o driver Python do MySQL.
  - Criar um tópico "toll" no Kafka.
  - Baixar um programa gerador de dados de streaming.
  - Personalizar o programa gerador para transmitir para o tópico "toll" no Kafka.
  - Baixar e personalizar um consumidor de dados de streaming.
  - Personalizar o consumidor para escrever os dados em uma tabela do banco de dados MySQL.
  - Verificar se os dados transmitidos estão sendo coletados na tabela do banco de dados.

---
Este projeto foi desenvolvido como parte da Formação de Engenheiro de Dados da IBM na plataforma Coursera. Créditos ao curso e aos seus instrutores por fornecerem a base para este exercício.
