import pyxylookup as xy
import pandas as pd
import numpy as np
import vcr
from nose.tools import raises

test_points = [[0,0], [1,1]]


@vcr.use_cassette('tests/vcr_cassettes/lookup_points_array.yaml')
def test_lookup_points_array():
    """lookup - points array"""
    r = xy.lookup(test_points)
    assert len(r) == 2


@vcr.use_cassette('tests/vcr_cassettes/lookup_asdataframe.yaml')
def test_lookup_asdataframe():
    """lookup - asdataframe"""
    r = xy.lookup(test_points, asdataframe=True)
    assert r.shape[0] == 2
    assert r.shape[1] >= 4
    assert 'DataFrame' in str(type(r))
    assert isinstance(r, pd.DataFrame)
    r = xy.lookup(test_points, shoredistance=True, grids=False, areas=False, asdataframe=True)
    assert r.shape[0] == 2
    assert r.shape[1] == 1
    r = xy.lookup(test_points, shoredistance=False, grids=True, areas=False, asdataframe=True)
    assert r.shape[0] == 2
    assert r.shape[1] >= 3
    r = xy.lookup(test_points, shoredistance=False, grids=False, areas=True, asdataframe=True)
    assert r.shape[0] == 2
    assert r.shape[1] == 1
    r = xy.lookup(test_points, shoredistance=True, grids=True, areas=True, asdataframe=True)
    assert r.shape[0] == 2
    assert r.shape[1] >= 5


def test_lookup_all_false():
    """Expect error when all parameters are False"""
    @raises(TypeError)
    def check_lookup_all_false_error(asdataframe):
        xy.lookup(test_points, shoredistance=False, grids=False, areas=False, asdataframe=asdataframe)
    for asdf in [True, False]:
        check_lookup_all_false_error(asdf)


def test_lookup_wrong_points():
    """Expect error when all parameters are False"""
    @raises(ValueError)
    def test_lookup_wrong_points_error(points):
        xy.lookup(points)
    test_lookup_wrong_points_error(None)
    test_lookup_wrong_points_error([])
    test_lookup_wrong_points_error([[]])
    test_lookup_wrong_points_error("[[0,0]]")
    test_lookup_wrong_points_error(pd.DataFrame({'x': [0, 1], 'y': [0, 1]}))
    test_lookup_wrong_points_error(np.asarray([[0, 1], [0, 1]]))
