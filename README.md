# PDF Chapter Extractor

## 📋 Sobre o Projeto

Este projeto visa desenvolver uma solução automatizada para extrair capítulos de livros em PDF, separando-os em arquivos individuais. O sistema deve ser robusto o suficiente para lidar com diferentes formatos de livros e padrões de títulos de capítulos.

## 🎯 Objetivos

### Funcionalidades Principais
- **Detecção Automática**: Identificar capítulos usando expressões regulares
- **Separação Inteligente**: Dividir PDFs em arquivos individuais por capítulo
- **Flexibilidade**: Suportar diferentes formatos de títulos
- **Organização**: Estruturar saída por livro processado

### Casos de Uso
- Processamento de livros acadêmicos
- Organização de bibliotecas digitais
- Preparação de material didático
- Análise de estrutura de livros

## 🏗️ Arquitetura do Projeto

```
src/
├── pdf_processor.py    # Orquestrador principal
├── chapter_detector.py # Detecção de capítulos
├── page_builder.py     # Construção de páginas
└── utils.py           # Utilitários gerais
```

## 🚀 Como Começar

### Pré-requisitos
- Python 3.8+
- Git
- Conhecimento básico de regex e processamento de texto

### Instalação
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd PdfManipulator

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt
```

### Uso Básico
```bash
python main.py --input LivrosPDF/Dom_Casmurro.pdf
```

## 📚 Documentação

- **`docs/DECISIONS.md`**: Registro de decisões técnicas
- **`docs/ARCHITECTURE.md`**: Documentação da arquitetura
- **`docs/API.md`**: Documentação das APIs internas

## 👥 Trabalho em Equipe

### Estrutura de Colaboração
- **Branch principal**: `main`
- **Branches de desenvolvimento**: `feature/nome-da-feature`
- **Revisão de código**: Pull Requests obrigatórios

### Convenções
- **Commits**: Mensagens em português, descritivas
- **Código**: Documentação em português
- **Testes**: Cobertura mínima de 70%

## 📝 Registro de Decisões

### Como Documentar Decisões

Cada decisão técnica importante deve ser registrada em `docs/DECISIONS.md` seguindo este formato:

```markdown
## [Data] - [Título da Decisão]

### Contexto
Descreva o problema ou situação que levou à decisão.

### Decisão
Explique qual foi a decisão tomada.

### Consequências
- **Positivas**: Benefícios da decisão
- **Negativas**: Possíveis desvantagens
- **Riscos**: Riscos associados

### Alternativas Consideradas
Liste outras opções que foram avaliadas.

### Implementação
Como a decisão será implementada.

### Responsável
Nome do(s) estagiário(s) responsável(is).
```

### Exemplo de Decisão
```markdown
## 2024-01-15 - Padrão de Detecção de Capítulos

### Contexto
Precisamos definir como identificar títulos de capítulos em diferentes formatos de PDF.

### Decisão
Usar regex com múltiplos padrões: "Capítulo X", "CAPÍTULO X", "Cap. X", "Chapter X".

### Consequências
- **Positivas**: Flexibilidade para diferentes formatos
- **Negativas**: Complexidade na manutenção dos padrões
- **Riscos**: Possíveis falsos positivos

### Alternativas Consideradas
- Usar apenas um padrão fixo
- Implementar ML para detecção

### Implementação
Criar lista de padrões regex em `ChapterDetector`.

### Responsável
João Silva
```

## 🧪 Testes

### Executar Testes
```bash
# Todos os testes
python -m pytest

# Testes específicos
python -m pytest tests/test_chapter_detector.py

# Com cobertura
python -m pytest --cov=src
```

### Estrutura de Testes
- **Testes unitários**: Para cada classe/função
- **Testes de integração**: Para fluxos completos
- **Testes de regressão**: Para casos conhecidos

## 📊 Critérios de Aceite

### Funcionalidade
- [ ] Processar 5+ livros diferentes
- [ ] 70%+ de precisão na separação
- [ ] Suporte a múltiplos formatos
- [ ] Tratamento de casos especiais

### Qualidade
- [ ] Código documentado
- [ ] Testes unitários
- [ ] Logs informativos
- [ ] Tratamento de erros

### Colaboração
- [ ] Decisões documentadas
- [ ] Code review realizado
- [ ] Padrões seguidos

## 🔧 Desenvolvimento

### Fluxo de Trabalho
1. **Planejar**: Definir tarefa e documentar decisões
2. **Desenvolver**: Implementar em branch separada
3. **Testar**: Criar testes e validar funcionalidade
4. **Revisar**: Pull Request com code review
5. **Integrar**: Merge após aprovação

### Ferramentas Recomendadas
- **IDE**: VS Code ou PyCharm
- **Debug**: pdb ou debugger da IDE
- **Análise**: pylint, flake8
- **Formatação**: black, isort

## 💬 Comunicação

### Canais
- **Issues**: Para bugs e melhorias
- **Pull Requests**: Para discussões de código
- **DECISIONS.md**: Para decisões técnicas

### Reuniões
- **Daily**: 15 min para alinhamento
- **Review**: Semanal para revisão de progresso
- **Retrospectiva**: Quinzenal para melhorias

## 🎓 Aprendizado

### Recursos Úteis
- [Documentação pypdf](https://pypdf.readthedocs.io/)
- [Regex Tutorial](https://regexone.com/)
- [Python Testing](https://docs.pytest.org/)

### Próximos Passos
1. Familiarizar-se com a estrutura
2. Ler documentação das bibliotecas
3. Analisar os PDFs de exemplo
4. Começar com implementação básica

---

**Boa sorte no desenvolvimento! 🚀** # PDFsplitter
