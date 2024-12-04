import argparse
import toml
import sys

def parse_toml(input_text):
    try:
        return toml.loads(input_text)
    except toml.TomlDecodeError as e:
        raise SyntaxError(f"Ошибка синтаксиса TOML: {e}")

def convert_to_ukya(value, indent_level=0):
    # Рекурсивная обработка всех типов данных с учетом отступов
    indent = "  " * indent_level  # Отступы для текущего уровня
    if isinstance(value, dict):
        # Словари
        items = [f"{indent} {k} -> {convert_to_ukya(v, indent_level + 1)}." for k, v in value.items()]
        return "{\n" + "\n".join(items) + f"\n{indent}}}"
    elif isinstance(value, list):
        # Массивы
        items = " ".join([convert_to_ukya(item, indent_level + 1) for item in value])
        return f"[ {items} ]"
    elif isinstance(value, (int, float)):
        # Числа
        return str(value)
    elif isinstance(value, str):
        # Строки
        return f'"{value}"'
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")

def convert_toml_to_ukya(toml_data):
    ukya_output = []
    for key, value in toml_data.items():
        ukya_output.append(f"let {key} = {convert_to_ukya(value)}")
    return "\n".join(ukya_output)

def main():
    parser = argparse.ArgumentParser(description="TOML to UKYA converter.")
    parser.add_argument("input_file", type=str, help=r"C:\Users\Vovawork\PycharmProjects\config3\input.toml")
    parser.add_argument("output_file", type=str, help=r"C:\Users\Vovawork\PycharmProjects\config3\output.txt")
    args = parser.parse_args()

    try:
        # Чтение из входного файла
        with open(args.input_file, "r", encoding="utf-8") as infile:
            input_text = infile.read()

        # Парсинг и преобразование
        toml_data = parse_toml(input_text)
        ukya_output = convert_toml_to_ukya(toml_data)

        # Запись в выходной файл
        with open(args.output_file, "w", encoding="utf-8") as outfile:
            outfile.write(ukya_output)

        print(f"Конвертация завершена. Результат сохранен в '{args.output_file}'.")
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
