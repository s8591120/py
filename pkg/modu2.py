import json


def read_json(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def print_json(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=4))


def process_data(data: dict, discount: float) -> None:
    for category in data['categories']:
        for item in category['items']:
            item['price'] = round(item['price'] * discount)


def write_json(data: dict, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
