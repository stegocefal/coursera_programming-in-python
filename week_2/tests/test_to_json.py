import json
import pytest
from .context import coursera_tasks
from coursera_tasks.to_json import to_json


@pytest.mark.parametrize('expected_return',
                         [{"data": 42}, [1, 2, 3], (1, 2, 3)],
                         ids=['dict', 'list', 'tuple'])
def test_dictionary(expected_return):
    @to_json
    def get_data():
        return expected_return

    assert get_data() == json.dumps(expected_return)
    assert get_data.__name__ == 'get_data'
