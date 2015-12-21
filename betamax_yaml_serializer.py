import os

import yaml
from betamax.serializers import BaseSerializer


class YAMLSerializer(BaseSerializer):
    name = 'yaml'

    @staticmethod
    def generate_cassette_name(cassette_library_dir, cassette_name):
        return os.path.join(cassette_library_dir,
                            '{0}.{1}'.format(cassette_name, 'yml'))

    def serialize(self, cassette_data):
        return yaml.dumps(cassette_data)

    def deserialize(self, cassette_data):
        try:
            deserialized_data = yaml.loads(cassette_data)
        except ValueError:
            deserialized_data = {}

        return deserialized_data
