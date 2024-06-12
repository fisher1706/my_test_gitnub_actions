class Generator:
    def __init__(self):
        self.result = {}

    def generate_some_data(self, data):
        data_out = {
            "Transaction":
                {
                     "CashbackAmount": 0.0,
                     "OriginalAmount": data,
                     "Scheme": "VISA",
                }
            }
        self.result.update(data_out)
        return self.result


if __name__ == '__main__':
    g = Generator()

    print(g.generate_some_data(123))
