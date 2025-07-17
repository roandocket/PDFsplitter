# Documentação da API

## PDFProcessor

### Classe Principal

```python
class PDFProcessor:
    def __init__(self)
    def process_pdf(input_file: str, output_dir: str) -> Dict
    def _extract_text_from_pdf(pdf_path: str) -> List[Tuple[int, str]]
    def _save_chapters(chapters: List[Dict], book_output_dir: str) -> int
```

### Métodos

#### `process_pdf(input_file: str, output_dir: str) -> Dict`
Processa um arquivo PDF e extrai seus capítulos.

**Parâmetros:**
- `input_file`: Caminho para o arquivo PDF
- `output_dir`: Diretório de saída base

**Retorna:**
```python
{
    'book_name': str,
    'output_directory': str,
    'chapters_detected': int,
    'files_generated': int,
    'problematic_pages': List[int]
}
```

#### `_extract_text_from_pdf(pdf_path: str) -> List[Tuple[int, str]]`
Extrai texto de todas as páginas do PDF.

**Parâmetros:**
- `pdf_path`: Caminho para o PDF

**Retorna:**
- Lista de tuplas (número_da_página, texto)

#### `_save_chapters(chapters: List[Dict], book_output_dir: str) -> int`
Salva os capítulos em arquivos PDF separados.

**Parâmetros:**
- `chapters`: Lista de capítulos com conteúdo
- `book_output_dir`: Diretório específico do livro

**Retorna:**
- Número de arquivos gerados

## ChapterDetector

### Classe Principal

```python
class ChapterDetector:
    def __init__(self)
    def detect_chapters(pages: List[Tuple[int, str]]) -> List[Dict]
    def _is_chapter_title(text: str) -> bool
    def _extract_chapter_number(text: str) -> str
    def _is_false_positive(text: str) -> bool
```

### Métodos

#### `detect_chapters(pages: List[Tuple[int, str]]) -> List[Dict]`
Detecta capítulos nas páginas fornecidas.

**Parâmetros:**
- `pages`: Lista de tuplas (número_da_página, texto)

**Retorna:**
```python
[
    {
        'number': str,
        'title': str,
        'start_page': int,
        'end_page': int,
        'content': str
    }
]
```

#### `_is_chapter_title(text: str) -> bool`
Verifica se um texto é um título de capítulo.

**Parâmetros:**
- `text`: Texto a ser verificado

**Retorna:**
- True se for um título de capítulo

#### `_extract_chapter_number(text: str) -> str`
Extrai o número do capítulo do texto.

**Parâmetros:**
- `text`: Texto do título do capítulo

**Retorna:**
- Número do capítulo como string

#### `_is_false_positive(text: str) -> bool`
Verifica se é uma menção a capítulo anterior.

**Parâmetros:**
- `text`: Texto a ser verificado

**Retorna:**
- True se for uma menção (falso positivo)

## PageBuilder

### Classe Principal

```python
class PageBuilder:
    def __init__(self)
    def split_page_content(page_text: str, chapter_boundaries: List[int]) -> List[str]
    def create_chapter_pdf(content: str, output_path: str) -> bool
    def _format_text_for_pdf(text: str) -> str
```

### Métodos

#### `split_page_content(page_text: str, chapter_boundaries: List[int]) -> List[str]`
Divide o conteúdo de uma página em múltiplos capítulos.

**Parâmetros:**
- `page_text`: Texto da página
- `chapter_boundaries`: Posições dos limites dos capítulos

**Retorna:**
- Lista de textos separados por capítulo

#### `create_chapter_pdf(content: str, output_path: str) -> bool`
Cria um arquivo PDF para um capítulo.

**Parâmetros:**
- `content`: Conteúdo do capítulo
- `output_path`: Caminho de saída

**Retorna:**
- True se criado com sucesso

#### `_format_text_for_pdf(text: str) -> str`
Formata texto para criação de PDF.

**Parâmetros:**
- `text`: Texto original

**Retorna:**
- Texto formatado

## Utils

### Funções Principais

#### `setup_logging(level: int = logging.INFO) -> None`
Configura o sistema de logging.

**Parâmetros:**
- `level`: Nível de logging

#### `create_book_output_directory(base_output_dir: str, book_name: str) -> Path`
Cria o diretório de saída específico para um livro.

**Parâmetros:**
- `base_output_dir`: Diretório base de saída
- `book_name`: Nome do livro (sem extensão)

**Retorna:**
- Path do diretório criado

#### `save_chapter_pdf(content: str, output_path: str) -> bool`
Salva o conteúdo de um capítulo em um arquivo PDF.

**Parâmetros:**
- `content`: Conteúdo do capítulo
- `output_path`: Caminho de saída

**Retorna:**
- True se salvo com sucesso

#### `generate_report(stats: Dict) -> str`
Gera um relatório de processamento.

**Parâmetros:**
- `stats`: Estatísticas do processamento

**Retorna:**
- String com o relatório

#### `save_processing_report(stats: Dict, book_output_dir: Path) -> None`
Salva o relatório de processamento no diretório do livro.

**Parâmetros:**
- `stats`: Estatísticas do processamento
- `book_output_dir`: Diretório do livro

#### `validate_pdf_file(file_path: str) -> bool`
Valida se o arquivo é um PDF válido.

**Parâmetros:**
- `file_path`: Caminho para o arquivo

**Retorna:**
- True se for um PDF válido

## Estruturas de Dados

### Chapter
```python
{
    'number': str,        # Número do capítulo
    'title': str,         # Título completo
    'start_page': int,    # Página de início
    'end_page': int,      # Página de fim
    'content': str        # Conteúdo do capítulo
}
```

### ProcessingStats
```python
{
    'book_name': str,           # Nome do livro
    'output_directory': str,    # Diretório de saída
    'chapters_detected': int,   # Capítulos detectados
    'files_generated': int,     # Arquivos gerados
    'problematic_pages': List[int]  # Páginas problemáticas
}
```

### Page
```python
Tuple[int, str]  # (número_da_página, texto)
```

## Exemplos de Uso

### Processamento Básico
```python
from src.pdf_processor import PDFProcessor

processor = PDFProcessor()
result = processor.process_pdf("livro.pdf", "output/")
print(f"Capítulos detectados: {result['chapters_detected']}")
```

### Detecção de Capítulos
```python
from src.chapter_detector import ChapterDetector

detector = ChapterDetector()
pages = [(1, "Capítulo 1\nConteúdo..."), (2, "Capítulo 2\nConteúdo...")]
chapters = detector.detect_chapters(pages)
```

### Criação de PDF
```python
from src.page_builder import PageBuilder

builder = PageBuilder()
success = builder.create_chapter_pdf("Conteúdo do capítulo", "capitulo_01.pdf")
```

### Configuração de Logs
```python
from src.utils import setup_logging
import logging

setup_logging(logging.DEBUG)
``` 