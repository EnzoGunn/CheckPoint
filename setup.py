from distutils.core import setup
from svc_utils import SvcUtils

setup(
    name='check_point',
    packages=['check_point'],
    version=SvcUtils.get_build_version('__init__.py'),
    description='CheckPoint',
    url='https://github.com/EnzoGunn/CheckPoint',
    author='Ahmad Saeed',
)
