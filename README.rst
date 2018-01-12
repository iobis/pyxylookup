# pyxylookup

Python client for the OBIS xylookup REST service

## Example usage

    import pyxylookup as xy
    xy.lookup([[0,0], [1,1]])

    ## Preparing a pandas DataFrame for calling 'lookup'
    import pandas as pd
    pointsdf = pd.DataFrame({'x': [0,1], 'y': [0,1]})
    points = pointsdf.to_records(index=False).tolist()
    ## retrieve results as a pandas DataFrame
    xy.lookup(points, asdataframe = True)

    ## Preparing a numpy ndarray for calling 'lookup'
    import numpy as np
    pointsarr = np.asarray([[0,0], [1,1]])
    points = pointsarr.tolist()
    xy.lookup(points)

## Development installation

    pipenv --three
    pipenv install vcrpy
    pipenv install tox
    pipenv install nose
    pipenv install requests
    pipenv install u-msgpack-python
    pipenv install pandas
    # enter virtual evironment
    pipenv shell