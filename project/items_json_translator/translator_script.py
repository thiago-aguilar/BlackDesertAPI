import json
from project.json_creator import scrapper
from time import sleep

def update_json(json_content, idx, list_size):
    print(f'Foram traduzidos {idx + 1} itens até agora, restam {list_size - (idx + 1)}')
    print(f'Foi traduzido {round((idx + 1)/list_size * 100, 2)}% dos itens')
    with open('data/translated_items.json', 'w', encoding='utf-8') as outfile:
        json.dump(json_content, outfile, indent=4, ensure_ascii=False)


def main():

    with open('data/items.json', 'rb') as json_file:
        data = json.load(json_file, encoding="utf8")

    list_size = len(data)
    output_list = []
    for idx, item in enumerate(data):
        print(f' ')
        id = item['id']
        grade = item['grade']
        name = scrapper.get_item_name(item_id=id)

        if name:

            current_item = {
                'id': id,
                'grade': grade,
                'name': name
            }
            output_list.append(current_item)
            update_json(json_content=output_list, idx=idx, list_size=list_size)

        else:
            print(f'ID {id} não encontrado no codex, será utilizado o nome em inglês')
            name = item['name']
            current_item = {
                'id': id,
                'grade': grade,
                'name': 'nome não mapeado'
            }
            output_list.append(current_item)
            update_json(json_content=output_list, idx=idx, list_size=list_size)


if __name__ == '__main__':
    main()
