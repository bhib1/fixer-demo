from setuptools import setup


# این کانفیگ ثابته و کپی کردم و اینجا قرار دادم
# name, version, package ==> necessary  -  Other ==> optional
setup(name='fixer-demo',
      version='0.1',
      description='Fixer service demo package',
      url='https://gitlab.com/bhi2017.b/fixer-demo',
      author='Behnam',
      author_email='me@example.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)
