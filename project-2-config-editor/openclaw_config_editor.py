import json
from pathlib import Path


CONFIG_FILE = Path(__file__).with_name("config.json")
DEFAULT_CONFIG = {
    "theme": "Dark",
    "language": "English",
    "font_size": 16,
    "default_model": "OpenClaw Lite",
    "response_style": "Balanced",
}
SETTING_OPTIONS = {
    "theme": ["Light", "Dark", "System"],
    "language": ["English", "Chinese", "Japanese"],
    "default_model": ["OpenClaw Lite", "OpenClaw Pro", "OpenClaw Max"],
    "response_style": ["Concise", "Balanced", "Detailed"],
}
SETTING_LABELS = {
    "theme": "Theme",
    "language": "Language",
    "font_size": "Font Size",
    "default_model": "Default Model",
    "response_style": "Response Style",
}


def validate_config(config: dict) -> dict:
    validated = DEFAULT_CONFIG.copy()
    for key, default_value in DEFAULT_CONFIG.items():
        value = config.get(key, default_value)
        if key == "font_size":
            if isinstance(value, int) and 8 <= value <= 32:
                validated[key] = value
        elif value in SETTING_OPTIONS.get(key, [default_value]):
            validated[key] = value
    return validated


def load_config(config_file: Path = CONFIG_FILE) -> dict:
    try:
        config = json.loads(config_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        config = DEFAULT_CONFIG.copy()
        save_config(config, config_file)
        return config

    validated = validate_config(config)
    if validated != config:
        save_config(validated, config_file)
    return validated


def save_config(config: dict, config_file: Path = CONFIG_FILE) -> None:
    config_file.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")


def show_settings(config: dict) -> None:
    print("Current OpenClaw settings:")
    for index, key in enumerate(DEFAULT_CONFIG, start=1):
        print(f"{index}. {SETTING_LABELS[key]}: {config[key]}")
    print("6. Reset to default settings")
    print("0. Finish editing")


def prompt_number(message: str, valid_numbers: set[int]) -> int:
    while True:
        selection = input(message).strip()
        if selection.isdigit() and int(selection) in valid_numbers:
            return int(selection)
        print("Please enter one of the listed numbers.")


def choose_setting() -> str:
    choice = prompt_number("Choose an option: ", {0, 1, 2, 3, 4, 5, 6})
    if choice == 0:
        return "finish"
    if choice == 6:
        return "reset"
    return list(DEFAULT_CONFIG)[choice - 1]


def prompt_list_value(setting: str) -> str:
    options = SETTING_OPTIONS[setting]
    print(f"Available {SETTING_LABELS[setting]} options:")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    choice = prompt_number("Choose an option: ", set(range(1, len(options) + 1)))
    return options[choice - 1]


def prompt_font_size() -> int:
    while True:
        raw_value = input("Enter Font Size (8-32): ").strip()
        if raw_value.isdigit() and 8 <= int(raw_value) <= 32:
            return int(raw_value)
        print("Font Size must be a whole number between 8 and 32.")


def get_new_value(setting: str):
    return prompt_font_size() if setting == "font_size" else prompt_list_value(setting)


def confirm_save() -> str:
    print("1. Save and quit")
    print("2. Quit without saving")
    print("3. Continue editing")
    choice = prompt_number("Choose an option: ", {1, 2, 3})
    return {1: "save", 2: "discard", 3: "continue"}[choice]


def main() -> None:
    config = load_config()
    working_config = config.copy()
    while True:
        show_settings(working_config)
        setting = choose_setting()
        if setting == "finish":
            action = confirm_save()
            if action == "save":
                save_config(working_config)
                print(f"Settings saved to {CONFIG_FILE}.")
                return
            if action == "discard":
                print("Changes discarded.")
                return
            continue
        if setting == "reset":
            working_config = DEFAULT_CONFIG.copy()
            print("Settings reset to defaults.")
            continue
        working_config[setting] = get_new_value(setting)
        print(f"Updated {SETTING_LABELS[setting]}.")


if __name__ == "__main__":
    main()
