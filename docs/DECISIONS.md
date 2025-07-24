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

### Contexto
estava buscando uma solução para melhorar a detecção dos capítulos

### Decisão
com buscas descobri o pdf plumber que extrai informações extras dos pdfs, como tamanho da fonte, assim então setei uma variavel para definir um tamanho minimo para um capitulo ser um capitulo, ja que geralmente em livros os capitulos são mais destacados(com fontes maiores que a do corpo do texto)

### Consequências
- **Positivas**: redução e praticamente extinção de falsos positivos se regex de detecção for bem implementado
- **Negativas**: [Desvantagens]
- **Riscos**: o txt do titulo do livro pode ser extraido e se o chapter detector estiver no fallback de detecção por numeros pode puxar o numero do livro como por exemplo: "Star Wars - Volume 3". Todo o livro pode estar em fonte pequena e nenhum texto é extraido, sera explicado como tratar isso na implementação

### Alternativas Consideradas
[Liste outras opções avaliadas]

### Implementação

o pdf é processado extraindo apenas os textos grandes, e o chapter detector itera sobre esses txts gerados puxando o capítulo, se os textos não forem encontrados o valor minimo de tamanho da fonte cai pra 1 (é removida essa validação por tamanho de fonte)


### Responsável
Thiago martins
```

## Decisões Registradas

