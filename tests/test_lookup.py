import vcr
import pyxylookup


#@vcr.use_cassette('tests/vcr_cassettes/lookup_points_array.yaml')
def test_lookup_points_array():
    "lookup - points array"
    res = pyxylookup.lookup([[0,0], [1,1]])
    assert res is not None
