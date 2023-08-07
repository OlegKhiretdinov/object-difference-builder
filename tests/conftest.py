import pytest


@pytest.fixture()
def diff_example():
    return [
        {'key': 'common',
         'status': 'changed',
         'values': [
             {
                 'key': 'follow',
                 'status': 'added',
                 'values': {'current': False}
             },
             {
                 'key': 'setting1',
                 'status': 'pristine',
                 'values': {'initial': 'Value 1'}
             },
             {
                 'key': 'setting2',
                 'status': 'deleted',
                 'values': {'initial': 200}
             },
             {
                 'key': 'setting3',
                 'status': 'changed',
                 'values': {'initial': True, 'current': None}},
             {
                 'key': 'setting4',
                 'status': 'added',
                 'values': {'current': 'blah blah'}
             },
             {
                 'key': 'setting5',
                 'status': 'added',
                 'values': [
                     {'key': 'key5',
                      'status': 'pristine',
                      'values': {'initial': 'value5'}
                      }
                 ]
             },
             {
                 'key': 'setting6',
                 'status': 'changed',
                 'values': [
                     {
                         'key': 'doge',
                         'status': 'changed',
                         'values': [
                             {'key': 'wow',
                              'status': 'changed',
                              'values': {'initial': '', 'current': 'so much'}
                              }
                         ]
                     },
                     {
                         'key': 'key',
                         'status': 'pristine',
                         'values': {'initial': 'value'}
                     },
                     {
                         'key': 'ops',
                         'status': 'added',
                         'values': {'current': 'vops'}}
                 ]
             }
         ]},
        {'key': 'group1',
         'status': 'changed',
         'values': [
             {
                 'key': 'baz',
                 'status': 'changed',
                 'values': {'initial': 'bas', 'current': 'bars'}
             },
             {
                 'key': 'foo',
                 'status': 'pristine',
                 'values': {'initial': 'bar'}
             },
             {
                 'key': 'nest',
                 'status': 'changed',
                 'values': {
                     'initial': [
                         {'key': 'key',
                          'status': 'pristine',
                          'values': {'initial': 'value'}
                          }
                     ],
                     'current': 'str'
                 }
             }
         ]},
        {
            'key': 'group2',
            'status': 'deleted',
            'values': [
                {
                    'key': 'abc',
                    'status': 'pristine',
                    'values': {'initial': 12345}
                },
                {
                    'key': 'deep',
                    'status': 'pristine',
                    'values': [
                        {'key': 'id',
                         'status': 'pristine',
                         'values': {'initial': 45}
                         }
                    ]
                }
            ]
        },
        {
            'key': 'group3',
            'status': 'added',
            'values': [
                {
                    'key': 'deep',
                    'status': 'pristine',
                    'values': [
                        {'key': 'id',
                         'status': 'pristine',
                         'values': [
                             {'key': 'number',
                              'status': 'pristine',
                              'values': {'initial': 45}
                              }
                         ]}
                    ]
                },
                {
                    'key': 'fee',
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
            'key': 'follow',
            'status': 'deleted',
            'values': {'initial': False}
        },
        {
            'key': 'host',
            'status': 'pristine',
            'values': {'initial': 'hexlet.io'}
        },
        {
            'key': 'proxy',
            'status': 'deleted',
            'values': {'initial': '123.234.53.22'}
        },
        {
            'key': 'timeout',
            'status': 'changed',
            'values': {'initial': 50, 'current': 20}
        },
        {
            'key': 'verbose',
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
