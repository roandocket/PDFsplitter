"""
Utilitários para o projeto.
DESAFIO: Implementar funções auxiliares necessárias.
"""

import logging
import os
from pathlib import Path
from typing import Dict
import re


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configura o sistema de logging.
    
    DESAFIO: Implementar configuração de logs para arquivo e console.
    
    Args:
        level: Nível de logging
    """
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')


def create_book_output_directory(base_output_dir: str, book_name: str) -> Path:
    """
    Cria o diretório de saída específico para um livro.
    
    DESAFIO: Criar estrutura de pastas organizada.
    
    Args:
        base_output_dir: Diretório base de saída
        book_name: Nome do livro (sem extensão)
        
    Returns:
        Path do diretório criado
    """
    path = Path(base_output_dir) / book_name
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_chapter_pdf(content: str, output_path: str) -> bool:
    """
    Salva o conteúdo de um capítulo em um arquivo PDF.
    
    DESAFIO: Implementar salvamento de PDF.
    
    Args:
        content: Conteúdo do capítulo
        output_path: Caminho de saída
        
    Returns:
        True se salvo com sucesso
    """
    try:
        from reportlab.pdfgen import canvas
        c = canvas.Canvas(str(output_path))
        c.drawString(72, 800, content[:1000])  # Salva só início do conteúdo para evitar quebra
        c.save()
        return True
    except Exception as e:
        logging.error(f"Erro ao salvar PDF: {e}")
        return False


def generate_report(stats: Dict) -> str:
    """
    Gera um relatório de processamento.
    
    DESAFIO: Criar relatório detalhado com estatísticas.
    
    Args:
        stats: Estatísticas do processamento
        
    Returns:
        String com o relatório
    """
    report = ["Relatório de Processamento:"]
    for k, v in stats.items():
        report.append(f"{k}: {v}")
    return '\n'.join(report)


def save_processing_report(stats: Dict, book_output_dir: Path) -> None:
    """
    Salva o relatório de processamento no diretório do livro.
    
    DESAFIO: Salvar relatório em arquivo de texto.
    
    Args:
        stats: Estatísticas do processamento
        book_output_dir: Diretório do livro
    """
    report = generate_report(stats)
    report_path = Path(book_output_dir) / "relatorio.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)


def validate_pdf_file(file_path: str) -> bool:
    """
    Valida se o arquivo é um PDF válido.
    
    DESAFIO: Implementar validação de arquivo PDF.
    
    Args:
        file_path: Caminho para o arquivo
        
    Returns:
        True se for um PDF válido
    """
    try:
        from pypdf import PdfReader
        PdfReader(file_path)
        return True
    except Exception:
        return False

def sanitize_filename(name: str) -> str:
    return re.sub(r'[^\w\-_\. ]', '_', name)