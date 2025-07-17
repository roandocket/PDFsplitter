# Arquitetura do Projeto

## Visão Geral

O projeto PDF Chapter Extractor é estruturado em camadas bem definidas, seguindo princípios de responsabilidade única e baixo acoplamento.

## Estrutura de Módulos

```
src/
├── pdf_processor.py    # Orquestrador principal
├── chapter_detector.py # Detecção de capítulos
├── page_builder.py     # Construção de páginas
└── utils.py           # Utilitários gerais
```

## Responsabilidades dos Módulos

### PDFProcessor
- **Responsabilidade**: Orquestrar todo o processo de extração
- **Dependências**: ChapterDetector, PageBuilder
- **Métodos principais**:
  - `process_pdf()`: Fluxo principal
  - `_extract_text_from_pdf()`: Extração de texto
  - `_save_chapters()`: Salvamento de capítulos

### ChapterDetector
- **Responsabilidade**: Detectar e identificar capítulos
- **Dependências**: regex, logging
- **Métodos principais**:
  - `detect_chapters()`: Detecção principal
  - `_is_chapter_title()`: Verificação de títulos
  - `_extract_chapter_number()`: Extração de números
  - `_is_false_positive()`: Detecção de falsos positivos

### PageBuilder
- **Responsabilidade**: Construir e manipular páginas
- **Dependências**: reportlab
- **Métodos principais**:
  - `create_chapter_pdf()`: Criação de PDFs
  - `split_page_content()`: Divisão de conteúdo
  - `_format_text_for_pdf()`: Formatação de texto

### Utils
- **Responsabilidade**: Funções auxiliares
- **Dependências**: pathlib, logging
- **Funções principais**:
  - `setup_logging()`: Configuração de logs
  - `create_book_output_directory()`: Criação de diretórios
  - `validate_pdf_file()`: Validação de arquivos
  - `generate_report()`: Geração de relatórios

## Fluxo de Dados

```
Input PDF → PDFProcessor → ChapterDetector → PageBuilder → Output Files
     ↓              ↓              ↓              ↓
  Utils         Utils         Utils         Utils
```

## Padrões de Design

### 1. Single Responsibility Principle
Cada classe tem uma responsabilidade específica e bem definida.

### 2. Dependency Injection
As dependências são injetadas via construtor, facilitando testes.

### 3. Strategy Pattern
Diferentes estratégias de detecção podem ser implementadas.

### 4. Factory Pattern
Criação de objetos PDF pode ser abstraída.

## Considerações de Performance

### 1. Processamento de Arquivos Grandes
- Leitura em chunks para PDFs grandes
- Processamento lazy quando possível

### 2. Memória
- Liberação de recursos após uso
- Uso de generators para grandes volumes

### 3. I/O
- Operações assíncronas para I/O intensivo
- Buffer de escrita para múltiplos arquivos

## Extensibilidade

### 1. Novos Formatos de Títulos
- Sistema de plugins para padrões regex
- Configuração via arquivo JSON

### 2. Novos Formatos de Saída
- Interface para diferentes formatos
- Suporte a EPUB, DOCX, etc.

### 3. Integração com APIs
- Webhooks para notificações
- API REST para processamento remoto

## Segurança

### 1. Validação de Entrada
- Verificação de tipos de arquivo
- Sanitização de nomes de arquivo

### 2. Tratamento de Erros
- Logs detalhados para debug
- Recuperação graciosa de falhas

## Testes

### 1. Estrutura de Testes
```
tests/
├── test_pdf_processor.py
├── test_chapter_detector.py
├── test_page_builder.py
└── test_utils.py
```

### 2. Tipos de Testes
- **Unitários**: Testes isolados de cada componente
- **Integração**: Testes de fluxo completo
- **Performance**: Testes de carga e tempo

## Logs e Monitoramento

### 1. Estrutura de Logs
- Logs estruturados em JSON
- Diferentes níveis por ambiente
- Rotação automática de arquivos

### 2. Métricas
- Tempo de processamento
- Taxa de sucesso
- Uso de recursos

## Configuração

### 1. Variáveis de Ambiente
- `LOG_LEVEL`: Nível de logging
- `OUTPUT_DIR`: Diretório de saída
- `MAX_FILE_SIZE`: Tamanho máximo de arquivo

### 2. Arquivo de Configuração
- Padrões regex customizáveis
- Configurações de performance
- Configurações de saída 