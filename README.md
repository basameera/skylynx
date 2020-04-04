# skylynx

**Status**

[![Build Status](https://travis-ci.org/basameera/skylynx.svg?branch=master)](https://travis-ci.org/basameera/skylynx)

Python support functions module

**Only Python 3**

---

## Version 0.0.3

### `skylynx` 

``` python
import skylynx
print('skylynx', skylynx.__version__)

>> skylynx 0.0.2
```

### `skylynx.utils` 

#### JSON

##### Write

``` python
import skylynx.utils as su

data_dict = dict(
    a=123,
    b='skylynx'
)
su.json_write('example.json', data_dict)
```

``` json
{
  "a": 123,
  "b": "skylynx"
}
```

##### Read

``` python
data = su.json_read('example.json')
print(data)

>> {'a': 123, 'b': 'skylynx'}
```

#### YAML

##### Write

``` python
su.yaml_write('example.yaml', data_dict)
```

``` yaml
a: 123
b: skylynx
```

##### Read

``` python
data = su.yaml_read('example.yaml')
print(data)

>> {'a': 123, 'b': 'skylynx'}
```

#### Pretty Print

``` python
data_dict = dict(
    a='This print a python dict object in a human readable form.',
    b=456,
    c=dict(
        d=123,
        e='skylynx'
    ),
    f = ['abc', 123]
)
su.pprint(data_dict, '> Header <')
```

``` bash
======================== > Header < ========================
a: This print a python dict object in a human readable form.
b: 456
c:
  d: 123
  e: skylynx
f: ['abc', 123]
------------------------------------------------------------
```

#### Make Directories

``` python
path = 'path/to/the/folder/'
su.makedirs(path)
print(os.path.exists(path))

>> True
```

