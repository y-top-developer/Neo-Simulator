from src.DataProvider import DataProvider

class Simulator(DataProvider):
    def __init__(self, initial, final, level, pivot):
        DataProvider.__init__(self, initial, final, level)
        self.pivot = pivot

    def get_initial(self, data):
        return f'{self.pivot}'.join([i for i in data['initial']])

    def get_final(self, data):
        return f'{self.pivot}'.join([i for i in data['final']])

    def split_input(self, response):
        return response.strip(self.pivot).split(self.pivot)

    def validate_input(self, input_data, data):
        result = {
            'status': 'SUCCESS',
            'messages': []
        }

        final = data['final']
        input_data = self.split_input(input_data)
        for i, (a, b) in enumerate(zip(input_data, final)):
            if a != b:
                result['status'] = 'ERROR'
                result['messages'].append(('incompatible', i, a, b))
        if i != len(final):
            result['status'] = 'ERROR'
            result['messages'].append(('incommensurate', i, a, b))
        return result
