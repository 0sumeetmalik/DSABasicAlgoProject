"""
from pytest import fixture
# Example
@fixture(params=['Samsung', 'Bravia', 'IndiaTV'])
def tv_brand(request):
    brand_name = request.param
    return brand_name

can be yield or return depending on what usage we are looking for
"""

from pytest import fixture
