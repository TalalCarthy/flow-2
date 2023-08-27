

def save_binary_file(file, save_path):
    with open(save_path, "wb") as f:
        f.write(file.getbuffer())


def save_text_file(file, save_path, encoding="utf-8"):
    text_content = file.getvalue().decode(encoding)
    with open(save_path, "w", encoding=encoding, errors="replace") as f:
        f.write(text_content)


def save_file(file, save_path):
    if save_path.lower().endswith('.txt'):
        return save_text_file(file, save_path)
    else:
        return save_binary_file(file, save_path)


__all__ = ['save_file']
