import json
import os


class Utils:
    PATH = 'templates/'

    def writer(self, data, filename):
        json_object = json.dumps(data)

        with open(self.PATH + filename, "w") as outfile:
            try:
                outfile.write(json_object)
            except Exception:
                raise Exception(f'json data: {filename} is not created')

    def cleaner(self):
        for file in os.listdir(self.PATH):
            os.remove(self.PATH + file)
