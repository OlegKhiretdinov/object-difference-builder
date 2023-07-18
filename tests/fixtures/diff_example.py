diff_example = [
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
