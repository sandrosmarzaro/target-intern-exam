data = [
    {
        'estado': 'SP',
        'faturamento': 67836.43
    },
    {
        'estado': 'RJ',
        'faturamento': 36678.66
    },
    {
        'estado': 'MG',
        'faturamento': 29229.88
    },
    {
        'estado': 'ES',
        'faturamento': 27165.48
    },
    {
        'estado': 'Outros',
        'faturamento': 19849.53
    }
]

billing = sum([state['faturamento'] for state in data])
for data in data:
    percentual = data['faturamento'] / billing * 100
    print(f'{data["estado"]} - {percentual:.2f}%')
