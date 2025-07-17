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
from src.utils import setup_logging


@click.command()
@click.option('--input', '-i', 'input_file', required=True,
              help='Caminho para o arquivo PDF de entrada')
@click.option('--output', '-o', 'output_dir', default='output',
              help='Diretório de saída para os capítulos')
@click.option('--verbose', '-v', is_flag=True,
              help='Modo verboso para mais detalhes')
def main(input_file, output_dir, verbose):
    """
    Extrai capítulos de um arquivo PDF e salva em arquivos separados.
    """
    # TODO: Implementar validação do arquivo de entrada
    
    # TODO: Configurar logging adequadamente
    
    # TODO: Processar o PDF usando a classe PDFProcessor
    
    # TODO: Exibir resultados do processamento
    
    pass


if __name__ == '__main__':
    main() 