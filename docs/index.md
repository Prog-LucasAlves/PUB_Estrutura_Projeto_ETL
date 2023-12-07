# Welcome to Projeto ETL

## Índice

- [Workflow](#workflow)
- [Função de Extração de dados](#função-de-extração-de-dados)

## Workflow

``` mermaid
---
title: Processo de ETL
---
flowchart TD
    A[Multiplos arquivos Excel] -.-> B([Extract: extract_from_excel])
    B([Extract: extract_from_excel]) ==> |Gera uma lista de Dataframes| C([Transformation: concat_data_frames])
    C([Transformation: concat_data_frames]) ==> |Gera um Dataframe Consilidado| D([Load: Converte para Excel])
    D([Load: Converte para Excel]) ==> |Salva o Consolidado em Excel| E([Pasta Output: Salva um arquivo único em Excel])
```

!!! info "Info"
    Categorização das funções de cada processo do ETL.

## Função de Extração de dados

### ::: app.pipeline.extract.extract_from_excel

## Função de Transformação de dados

### ::: app.pipeline.transform.concat_data_frames

## Função para Salvar os dados

### ::: app.pipeline.load.load_excel
