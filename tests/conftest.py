import pytest


@pytest.fixture
def time_example1() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date_example1() -> str:
    return "11.03.2024"


@pytest.fixture
def time_example2() -> str:
    return "2022-12-11T12:26:56.671407"


@pytest.fixture
def date_example2() -> str:
    return "11.12.2022"


@pytest.fixture
def operations_list_example() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428839, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def sorted_operations_list_example() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428839, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def reverse_sorted_operations_list_example() -> list:
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428839, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def executed_operations() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428839, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def canceled_operations() -> list:
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def unknown_operations() -> list:
    return []
