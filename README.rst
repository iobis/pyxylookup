# pyxylookup

Python client for the OBIS xylookup REST service

## Example usage

    import pyxylookup
    pyxylookup.lookup([[0,0], [1,1]])


## Development installation

    pipenv --three
    pipenv install vcrpy
    pipenv install tox
    pipenv install requests
    pipenv install u-msgpack-python
    # enter virtual evironment
    pipenv shell