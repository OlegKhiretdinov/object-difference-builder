import pytest


@pytest.fixture()
def diff_example():
    return [
        {'name': 'common',
         'status': 'changed',
         'values': [
             {
                 'name': 'follow',
                 'status': 'added',
                 'values': {'current': False}
             },
             {
                 'name': 'setting1',
                 'status': 'pristine',
                 'values': {'initial': 'Value 1'}
             },
             {
                 'name': 'setting2',
                 'status': 'deleted',
                 'values': {'initial': 200}
             },
             {
                 'name': 'setting3',
                 'status': 'changed',
                 'values': {'initial': True, 'current': None}},
             {
                 'name': 'setting4',
                 'status': 'added',
                 'values': {'current': 'blah blah'}
             },
             {
                 'name': 'setting5',
                 'status': 'added',
                 'values': [
                     {'name': 'key5',
                      'status': 'pristine',
                      'values': {'initial': 'value5'}
                      }
                 ]
             },
             {
                 'name': 'setting6',
                 'status': 'changed',
                 'values': [
                     {
                         'name': 'doge',
                         'status': 'changed',
                         'values': [
                             {'name': 'wow',
                              'status': 'changed',
                              'values': {'initial': '', 'current': 'so much'}
                              }
                         ]
                     },
                     {
                         'name': 'key',
                         'status': 'pristine',
                         'values': {'initial': 'value'}
                     },
                     {
                         'name': 'ops',
                         'status': 'added',
                         'values': {'current': 'vops'}}
                 ]
             }
         ]},
        {'name': 'group1',
         'status': 'changed',
         'values': [
             {
                 'name': 'baz',
                 'status': 'changed',
                 'values': {'initial': 'bas', 'current': 'bars'}
             },
             {
                 'name': 'foo',
                 'status': 'pristine',
                 'values': {'initial': 'bar'}
             },
             {
                 'name': 'nest',
                 'status': 'changed',
                 'values': {
                     'initial': [
                         {'name': 'key',
                          'status': 'pristine',
                          'values': {'initial': 'value'}
                          }
                     ],
                     'current': 'str'
                 }
             }
         ]},
        {
            'name': 'group2',
            'status': 'deleted',
            'values': [
                {
                    'name': 'abc',
                    'status': 'pristine',
                    'values': {'initial': 12345}
                },
                {
                    'name': 'deep',
                    'status': 'pristine',
                    'values': [
                        {'name': 'id',
                         'status': 'pristine',
                         'values': {'initial': 45}
                         }
                    ]
                }
            ]
        },
        {
            'name': 'group3',
            'status': 'added',
            'values': [
                {
                    'name': 'deep',
                    'status': 'pristine',
                    'values': [
                        {'name': 'id',
                         'status': 'pristine',
                         'values': [
                             {'name': 'number',
                              'status': 'pristine',
                              'values': {'initial': 45}
                              }
                         ]}
                    ]
                },
                {
                    'name': 'fee',
                    'status': 'pristine',
                    'values': {'initial': 100500}
                }
            ]
        }
    ]


@pytest.fixture()
def diff_example_2():
    return [
        {
            'name': 'follow',
            'status': 'deleted',
            'values': {'initial': False}
        },
        {
            'name': 'host',
            'status': 'pristine',
            'values': {'initial': 'hexlet.io'}
        },
        {
            'name': 'proxy',
            'status': 'deleted',
            'values': {'initial': '123.234.53.22'}
        },
        {
            'name': 'timeout',
            'status': 'changed',
            'values': {'initial': 50, 'current': 20}
        },
        {
            'name': 'verbose',
            'status': 'added',
            'values': {'current': True}
        }
    ]


@pytest.fixture()
def dict_1():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }


@pytest.fixture()
def dict_2():
    return {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
