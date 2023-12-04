# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Workflow

mermaid

```mermaid
flowchart LR
    subgraph ETL(Pipeline)
        A(Multiplos Arquivos Excel) -> B[Extract: extract_from_excel]
        B[Extract: extract_from_excel] -> |Gera uma lista de Dataframes| C[Transformation: consolidate_dataframes]
        C[Transformation: consolidate_dataframes] -> |Gera um Dataframe Consolidado| D[Load: Converte para Excel]
        D(Load: Converte para Excel) -> |Salva o consolidado em Excel| E(Pasta Output: Um arquivo único Excel)

    end
```

## Função de Transformação de dados

### ::: app.pipeline.extract.extract_from_excel
