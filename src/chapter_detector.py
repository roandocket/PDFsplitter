import re
import os
import logging
from typing import List, Dict, Tuple
from .config import CHAPTER_PATTERNS, FALLBACK_PATTERNS


class ChapterDetector:
    def __init__(self):
        self.chapter_patterns = CHAPTER_PATTERNS
        self.fallback_patterns = FALLBACK_PATTERNS

    def detect_chapters_from_dir(self, txt_dir: str) -> List[Tuple[int, str]]:
        """
        Detecta capítulos a partir dos arquivos .txt com texto extraído.
        """
        chapter_starts = []
        txt_files = sorted([f for f in os.listdir(txt_dir) if f.endswith('.txt')])

        for idx, fname in enumerate(txt_files):
            with open(os.path.join(txt_dir, fname), encoding="utf-8") as f:
                text = f.read()
                for pattern in self.chapter_patterns:
                    for match in pattern.finditer(text):
                        chapter_starts.append((idx, match.group(0)))

        if not chapter_starts:
            logging.warning("Nenhum capítulo detectado com padrão principal. Tentando fallback...")
            for idx, fname in enumerate(txt_files):
                with open(os.path.join(txt_dir, fname), encoding="utf-8") as f:
                    text = f.read()
                    for pattern in self.fallback_patterns:
                        for match in pattern.finditer(text):
                            chapter_starts.append((idx, match.group(0)))
            if chapter_starts:
                logging.info(f"Fallback detectou {len(chapter_starts)} possíveis capítulos.")

        return chapter_starts

    def detect_chapters(self, pages: List[Tuple[int, str]]) -> List[Dict]:
        """
        Detecta capítulos em uma lista de (número_da_página, texto).
        """
        detected = []
        for idx, text in pages:
            if self._is_false_positive(text):
                continue
            if self._is_chapter_title(text):
                chapter_number = self._extract_chapter_number(text)
                detected.append({
                    "page": idx,
                    "title": text.strip(),
                    "number": chapter_number
                })
        return detected

    def _is_chapter_title(self, text: str) -> bool:
        return any(pat.search(text) for pat in self.chapter_patterns)

    def _extract_chapter_number(self, text: str) -> str:
        match = re.search(r'\d+|[IVXLC]+', text, re.IGNORECASE)
        return match.group(0) if match else ""

    def _is_false_positive(self, text: str) -> bool:
        return bool(re.search(r'cap[íi]tulo anterior', text, re.IGNORECASE))
    
    