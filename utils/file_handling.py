def open_text(file_directory):
    with open(file_directory, "r", encoding='utf-8') as f:
        text = f.read()
    f.close()
    
    return text