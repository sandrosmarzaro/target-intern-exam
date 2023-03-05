import json


def load_json():
    with open('dados.json', 'r') as file:
        data = file.read()
        return json.loads(data)


def above_avarage_days(data):
    nonzero_data = [data for data in data if data['valor'] != 0]
    average = sum([data['valor'] for data in nonzero_data]) / len(nonzero_data)
    above_average_data = [data for data in data if data['valor'] > average]
    print(f'The days above average are: {[data["dia"] for data in above_average_data]}')


if __name__ == '__main__':
    data = load_json()
    smallest_day = min(data, key=lambda x: x['valor'])
    print(f'The smallest day was {smallest_day["dia"]} with value {smallest_day["valor"]}')
    biggest_day = max(data, key=lambda x: x['valor'])
    print(f'The biggest day was {biggest_day["dia"]} with value {biggest_day["valor"]}')
    above_avarage_days(data)
