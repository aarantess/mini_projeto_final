# Mini-Projeto: Visualização de Dados e Business Intelligence

**Aluno:** Aline Daiani Arantes Leonardo  
**Turma:** QA VDBI 2026/1 2  
**Data:** 01/06/2026

---

## 1. Descrição do Projeto

Este projeto consiste em uma **Análise Exploratória de Dados (AED)** aplicada a uma base de varejo contendo aproximadamente **830.000 registros**.

O principal objetivo foi transformar dados brutos em informações estratégicas para o negócio, por meio de processos de:

* limpeza e tratamento de dados;
* correção de inconsistências;
* extração de estatísticas descritivas;
* geração de agrupamentos e indicadores para apoio à tomada de decisão em **Business Intelligence (BI)**.

---

## 2. Reflexão Teórica: Processo de ETL e Qualidade dos Dados

O processo de **ETL (Extração, Transformação e Limpeza)** é uma etapa fundamental em qualquer projeto de Business Intelligence. Durante o desenvolvimento deste projeto, ficou evidente que bases de dados inconsistentes podem gerar interpretações equivocadas e impactar diretamente as decisões estratégicas da empresa.

Um exemplo importante foi a identificação e remoção de **96.553 registros duplicados**, que representavam aproximadamente **11,63% da base original**. Caso esses dados fossem mantidos, os indicadores de vendas e faturamento apresentariam valores artificialmente inflados, comprometendo a confiabilidade da análise.

Além disso, foram realizadas ações de:

* tratamento de valores nulos;
* padronização de categorias;
* correção de registros inconsistentes;
* normalização de informações textuais.

A conversão de valores como `#N/D` para a categoria **"Sem Categoria"** garantiu maior integridade analítica e permitiu representar a realidade operacional da empresa com mais precisão.

Dessa forma, o projeto demonstra como a qualidade dos dados é essencial para a construção de análises confiáveis e para o suporte à tomada de decisões baseada em evidências.

---

## 3. Insights Obtidos na Análise

A análise exploratória revelou informações relevantes sobre a operação do varejo:

### Liderança de Categoria

A categoria **ALIMENTOS** apresentou o maior volume de vendas, com **384.197 itens**, representando aproximadamente **52,38% da base tratada**.

### Perfil Familiar dos Clientes

A maior parte dos clientes não possui filhos, considerando que a **moda** e a **mediana** da variável são iguais a **0**. Ainda assim, a média geral foi de **1,15 filhos por cliente**.

### Participação por Gênero

O público feminino apresentou participação ligeiramente superior nas compras:

* **Feminino (F):** 52,14%
* **Masculino (M):** 47,86%

### Eficiência do Processo de ETL

A etapa de limpeza foi determinante para a qualidade da análise, removendo mais de **96 mil duplicidades** e evitando distorções nos indicadores do negócio.

### Integridade das Categorias

O tratamento de inconsistências permitiu recuperar e padronizar **3.228 registros** sob a categoria **"Sem Categoria"**.

### Qualidade da Base de Produtos

A exclusão de registros sem nome de produto garantiu maior confiabilidade na análise do mix de produtos comercializados.

---

## 4. Instruções de Execução

### Pré-requisitos

Certifique-se de possuir instalado:

* Python 3.x
* Biblioteca Pandas

Instalação do Pandas:

```bash
pip install pandas
```

### Execução

1. Coloque o arquivo `Base Varejo.csv` na mesma pasta do script.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python script.py
```

Após a execução:

* o relatório técnico será exibido no terminal;
* o arquivo `df_limpo.csv` será gerado automaticamente.

---

## 5. Estrutura de Pastas do Repositório

```text
MiniProjeto_Final/
└── [Nome_do_Aluno]/
    ├── script.py          # Código-fonte Python
    ├── README.md          # Documentação do projeto
    └── df_limpo.csv       # Base de dados limpa e padronizada
```

---

## 6. Fonte dos Dados

A base de dados utilizada neste projeto foi obtida por meio da plataforma Kaggle:

**Base Varejo**
https://www.kaggle.com/datasets/namespaiva/base-varejo/data

O conjunto de dados foi utilizado exclusivamente para fins acadêmicos e educacionais, permitindo a aplicação prática de conceitos de ETL, Análise Exploratória de Dados (AED) e Business Intelligence (BI).

---

## Considerações Finais

Este projeto permitiu aplicar, na prática, conceitos fundamentais de:

* Análise Exploratória de Dados (AED);
* ETL (Extração, Transformação e Limpeza de Dados);
* tratamento e padronização de informações;
* estatística descritiva;
* geração de indicadores de negócio;
* Business Intelligence (BI).

Além de desenvolver habilidades técnicas em manipulação e análise de dados, o projeto evidenciou a importância da qualidade das informações para a geração de insights confiáveis e para o suporte à tomada de decisões orientadas por dados.

A experiência reforçou como etapas de limpeza, validação e padronização são fundamentais para transformar grandes volumes de dados em conhecimento útil para organizações.

---

> **Nota:** Este projeto foi desenvolvido conforme as diretrizes da Semana 07 do módulo de Visualização de Dados e Business Intelligence.
