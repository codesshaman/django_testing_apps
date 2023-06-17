# Create your views here.
def config(file_path, section_name):
    """Метод парсинга конфигурационного файла"""
    section_lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        section_found = False

        for line in lines:
            line = line.strip()

            if line.startswith(';'):
                continue  # Пропускаем строки с комментариями

            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                if current_section == section_name:
                    section_found = True
                else:
                    section_found = False
            elif section_found:
                section_lines.append(line)

    return section_lines

