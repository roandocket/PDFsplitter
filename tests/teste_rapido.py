from src.chapter_detector import ChapterDetector

detector = ChapterDetector()
test_text = ["Capítulo 1", "cap.6", "cap.  6", "chapter 3", "Capítulo X", "Capitulo 1", "1. Introdução", "No Capítulo anterior..."]

for text in test_text:
    result = detector._is_chapter_title(text)
    print(f"Texto: {text} - Resultado: {result}")