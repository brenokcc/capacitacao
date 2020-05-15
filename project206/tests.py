from project206.goal01 import pipeline, parse_data


def test_pipeline():
    with pipeline('out.csv', ('Chevrolet', 'Landau', 'Carlo')) as p:
        for row in parse_data('cars.csv'):
            p.send(row)

    with open('out.csv') as f:
        for row in f:
            print(row, end='')


test_pipeline()
