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



```markdown
## [2025-07-18] - Implementação de Padrões Regex para Detecção

### Contexto
Precisávamos definir como identidficar títulos de capítulos nos PDFs.

### Decisão
Implementamos 4 padrões regex principais com flags IGNORECASE e MULTILINE


### Consequências
- **Positivas**: Flexibilidade para diferentes formatos
- **Negativas**: Pode capturar falsos positivos.
- **Riscos**: Precisão depende da qualidade dos padrôes

### Alternativas Consideradas
Implementar um Machine Learning para deteccão

### Implementação
Criamos uma lista de padrões no construtor do ChapterDetector

### Responsável
Roan Ferreira
Thiago Martins
Mariana Chiorboli
```
