"""
Processador principal para extração de capítulos de PDFs.
DESAFIO: Implementar toda a lógica de processamento.
"""

import logging
from pathlib import Path
from typing import Dict, List, Tuple

from pypdf import PdfReader, PdfWriter
from .chapter_detector import ChapterDetector
from .utils import sanitize_filename


class PDFProcessor:
    """
    Classe principal responsável por processar PDFs e extrair capítulos.
    
    DESAFIO: Implementar todos os métodos desta classe.
    """
    
    def __init__(self, font_size: int = 16):
        # TODO: Inicializar componentes necessários
        self.font_size = font_size
        self.detector = ChapterDetector()
        
    def process_pdf(self, input_file: str, output_dir: str) -> Dict:
        logging.info(f"Iniciando processamento do arquivo: {input_file}")

        # 1. Extrair texto das páginas com font_size padrão
        pages = self._extract_text_from_pdf(input_file, font_size=self.font_size)
        logging.info(f"{len(pages)} páginas processadas com texto extraído.")

        # 2. Detectar capítulos com padrão principal
        chapter_dicts = self.detector.detect_chapters(pages)

        # 3. Fallback: tentar padrões de número/romano se não encontrar capítulos
        if not chapter_dicts:
            logging.warning("Nenhum capítulo detectado com padrão principal. Tentando fallback de números...")
            # Temporariamente troca os padrões do detector para fallback
            original_patterns = self.detector.chapter_patterns
            self.detector.chapter_patterns = self.detector.fallback_patterns
            chapter_dicts = self.detector.detect_chapters(pages)
            self.detector.chapter_patterns = original_patterns

        # 4. Fallback final: se ainda não encontrar, extrair texto com font_size=1
        if not chapter_dicts:
            logging.warning("Nenhum capítulo detectado com fallback. Tentando extrair texto com font_size=1...")
            pages = self._extract_text_from_pdf(input_file, font_size=1)
            chapter_dicts = self.detector.detect_chapters(pages)

        if not chapter_dicts:
            logging.warning("Nenhum capítulo detectado após todos os fallbacks.")
            return {
                "paginas_processadas": len(pages),
                "capitulos_detectados": 0,
                "chapters": 0,
                "pages": len(pages)
            }

        logging.info(f"{len(chapter_dicts)} capítulos detectados.")

        # Converter para lista de tuplas (start_page, title) para _save_chapters
        chapter_starts = [(ch.get("page", 0), ch.get("title", f"Capitulo_{i+1}")) for i, ch in enumerate(chapter_dicts)]

        # 5. Criar subpasta com nome do livro
        book_name = Path(input_file).stem
        book_output_dir = Path(output_dir) / book_name
        book_output_dir.mkdir(parents=True, exist_ok=True)

        # Salvar os capítulos como PDFs na subpasta
        num_saved = self._save_chapters(input_file, chapter_starts, str(book_output_dir))

        return {
            "input": input_file,
            "output_dir": str(book_output_dir),
            "paginas_processadas": len(pages),
            "capitulos_detectados": len(chapter_dicts),
            "chapters": num_saved,
            "pages": len(pages)
        }

    
    def _extract_text_from_pdf(self, pdf_path: str, font_size: int = 16) -> List[Tuple[int, str]]:
        import pdfplumber
        extracted_pages = []

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                filtered = page.filter(lambda obj: obj.get("size", 0) >= font_size)
                text = filtered.extract_text() or ""
                extracted_pages.append((i, text))

        return extracted_pages

    
    def _save_chapters(self, pdf_path: str, chapters: List[Tuple[int, str]], output_dir: str) -> int:
        reader = PdfReader(pdf_path)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        count = 0

        for idx, (start, title) in enumerate(chapters):
            end = chapters[idx + 1][0] if idx + 1 < len(chapters) else len(reader.pages)
            writer = PdfWriter()

            for i in range(start, end):
                writer.add_page(reader.pages[i])

            chapter_name = f"capitulo_{idx+1:02d}.pdf"
            out_path = Path(output_dir) / chapter_name
            with open(out_path, "wb") as f:
                writer.write(f)
            logging.info(f"Gerado: {out_path} (páginas {start+1}-{end})")
            count += 1

        return count
