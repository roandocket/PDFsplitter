# Registro de Decisões Técnicas

Este documento registra as decisões técnicas importantes tomadas durante o desenvolvimento do projeto.

## Formato das Decisões

Cada decisão deve seguir este template:

```markdown
## [YYYY-MM-DD] - [Título da Decisão]

### Contexto
[Descreva o problema ou situação]

### Decisão
[Explique a decisão tomada]

### Consequências
- **Positivas**: [Benefícios]
- **Negativas**: [Desvantagens]
- **Riscos**: [Riscos associados]

### Alternativas Consideradas
[Liste outras opções avaliadas]

### Implementação
[Como será implementada]

### Responsável
[Nome do(s) responsável(is)]
```

## Decisões Registradas

### [Aguardando primeira decisão]

---

**Nota**: Este arquivo deve ser atualizado sempre que uma decisão técnica importante for tomada. 

[2025-07-21] - Uso de pdfplumber para Extração de Títulos por Tamanho de Fonte

### Contexto
Durante a tentativa de detecção de capítulos em PDFs, observamos que os títulos geralmente aparecem com fontes maiores. No entanto, o texto extraído diretamente do PDF não contém essa informação por padrão, dificultando a diferenciação entre títulos e corpo do texto.

### Decisão

Foi adotado o uso da biblioteca pdfplumber, que permite acessar metadados visuais dos textos, como tamanho de fonte. Definimos um limiar (threshold) para filtrar apenas textos com fontes maiores, aumentando a precisão na detecção dos capítulos.

### Consequências
- **Positivas**: Redução significativa de falsos positivos na detecção de capítulos.
                Maior precisão ao distinguir entre títulos e conteúdo normal.

- **Negativas**: Dependência da qualidade e padronização dos metadados do PDF.


- **Riscos**: Caso o título do livro ou subtítulos sigam a mesma lógica de fontes grandes, podem ser        confundidos como capítulos.
            Caso nenhum texto esteja com fonte grande, nada será detectado.

### Alternativas Consideradas
Análise apenas via regex textual.

### Implementação

O PDF é processado usando pdfplumber, filtrando apenas textos com fonte acima de um determinado threshold. Esses trechos são salvos em arquivos .txt, que serão usados posteriormente para detectar os capítulos via regex.

Caso nenhum texto relevante seja encontrado, o threshold é reduzido para 1, permitindo que todo o texto seja considerado como fallback.

### Responsável
Thiago martins
```


[2025-07-22] - Estratégia de Detecção Hierárquica de Capítulos

### Contexto

    Alguns livros PDF não seguem uma formatação consistente: alguns usam títulos com fontes grandes, outros com fontes normais, e alguns sequer têm padrões claros. Foi necessário implementar uma estratégia mais robusta que cobrisse diferentes cenários.

### Decisão

    Foi implementada uma estratégia hierárquica de detecção:

    Primeira tentativa: Detectar capítulos em textos com fonte maior que o threshold.

    Fallback: Caso nada seja detectado, aplicar padrões alternativos de regex (ex: números isolados).

    Fallback final: Reduzir o threshold para 1 e aplicar os mesmos padrões em todos os textos, sem filtragem por fonte.

### Consequências

- **Positivas**:

    Alta taxa de detecção de capítulos mesmo em PDFs mal formatados.
    Adaptação automática ao nível de estrutura disponível no documento.

- **Negativas**:

  - Pode aumentar o tempo de processamento por passar por múltiplas tentativas.

- **Riscos**:

    Fallbacks podem detectar títulos errados (ex: número de volume ou paginação) se os padrões forem genéricos demais.
    O uso de textos com `threshold = 1` pode introduzir ruído textual e causar falsos positivos.

### Alternativas Consideradas

    Utilizar apenas uma camada de regex sem fallback.
    Marcação manual de capítulos.

### Implementação
A lógica de fallback foi implementada na classe `ChapterDetector`. O código tenta detectar capítulos usando os textos com fonte grande. Se a detecção falhar, aplica os padrões secundários e reduz o limite mínimo de fonte no pdf_processor.

### Responsável
Thiago Martins


## Decisões Registradas

