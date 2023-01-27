BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text = text[start:]
    if len(text) > size:
        text = text[:size + 1]
        rev_text = text[::-1]
        for i in range(len(rev_text)):
            if rev_text[i] == ' ' or rev_text[i] == '\n':
                if rev_text[i + 1] in end_simbols:
                    rev_text = rev_text[i + 1:]
                    text = rev_text[::-1]
                    break

    page = [text, len(text)]
    return page


end_simbols = [',', '.', '!', ':', ';', '?']


def prepare_book(path: str) -> None:
    pass


prepare_book(BOOK_PATH)
