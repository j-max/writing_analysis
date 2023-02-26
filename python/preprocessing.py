from pathlib import Path


def read_all_texts(path_to_writing_folder):
    
    text_content = ""
    file_count = 0
    for path in Path(path_to_writing_folder).rglob("*.txt"):
        with open(path, "r") as read_file:
    
            text_content += read_file.read().replace("\n", ' ')
        file_count += 1

    return text_content, file_count