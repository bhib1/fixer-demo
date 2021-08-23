from setuptools import setup


# این کانفیگ ثابته و کپی کردم و اینجا قرار دادم
# name, version, package ==> necessary  -  Other ==> optional
setup(name='fixer-demo',
      version='0.2',
      description='Fixer service demo package',
      url='https://github.com/bhib1/fixer-demopython setup.py sdist',
      author='Behnam',
      author_email='me@example.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)
