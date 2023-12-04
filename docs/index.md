# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

!!! warning "Warning"
    This is an example of a **warning** or **attention** message.

!!! info "Info"
    This is an example of an **information** message.

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

## Função de Extração de dados

### ::: app.pipeline.extract.extract_from_excel

## Função de Transformação de dados

### ::: app.pipeline.transform.concat_data_frames

## Função para Salvar os dados

### ::: app.pipeline.load.load_excel
