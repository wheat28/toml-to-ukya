import toml
import sys

def parse_toml(input_text):
    try:
        return toml.loads(input_text)
    except toml.TomlDecodeError as e:
        raise SyntaxError(f"Ошибка синтаксиса TOML: {e}")

def convert_to_ukya(value, indent_level=0):
    indent = "  " * indent_level
    if isinstance(value, dict):
        items = [f"{indent} {k} -> {convert_to_ukya(v, indent_level + 1)}." for k, v in value.items()]
        return "{\n" + "\n".join(items) + f"\n{indent}}}"
    elif isinstance(value, list):
        items = " ".join([convert_to_ukya(item, indent_level + 1) for item in value])
        return f"[ {items} ]"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return f'"{value}"'
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")

def convert_toml_to_ukya(toml_data):
    ukya_output = []
    for key, value in toml_data.items():
        ukya_output.append(f"let {key} = {convert_to_ukya(value)}")
    return "\n".join(ukya_output)

def main():
    print("Введите содержимое TOML. Для завершения введите пустую строку и нажмите Enter:")
    input_lines = []
    try:
        while True:
            line = input()
            if not line.strip():  # Если строка пустая, завершить ввод
                break
            input_lines.append(line)

        input_text = "\n".join(input_lines)

        # Парсинг и преобразование
        toml_data = parse_toml(input_text)
        ukya_output = convert_toml_to_ukya(toml_data)

        # Вывод результата
        print("\nРезультат в формате УКЯ:")
        print(ukya_output)
    except SyntaxError as e:
        print(f"Ошибка синтаксиса: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
