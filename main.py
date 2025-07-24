#!/usr/bin/env python3
"""
Script principal para extração de capítulos de PDFs.
DESAFIO: Implementar a lógica principal de processamento.
"""

import click
import logging
import os
from pathlib import Path
from src.pdf_processor import PDFProcessor

@click.command()
@click.option('--input', '-i', 'input_file', required=True,
              help='Caminho para o arquivo PDF de entrada')
@click.option('--output', '-o', 'output_dir', required=True,
              help='Diretório para salvar os capítulos extraídos')
@click.option('--font-size', '-f', 'font_size', default=16, show_default=True,
              help='Tamanho mínimo da fonte para considerar como título')
def main(input_file: str, output_dir: str, font_size: int):
    logging.basicConfig(level=logging.INFO)

    processor = PDFProcessor(font_size=font_size)
    stats = processor.process_pdf(input_file, output_dir)

    logging.info(f"✅ Processamento finalizado:")
    logging.info(f"📄 Páginas processadas: {stats.get('paginas_processadas', stats.get('pages', 'N/A'))}")
    logging.info(f"📚 Capítulos detectados: {stats.get('capitulos_detectados', stats.get('chapters', 'N/A'))}")


if __name__ == "__main__":
    main()
