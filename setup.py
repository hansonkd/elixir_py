#-*-Mode:python;coding:utf-8;tab-width:4;c-basic-offset:4;indent-tabs-mode:()-*-
# ex: set ft=python fenc=utf-8 sts=4 ts=4 sw=4 et:

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import tests.elixir_tests
        import unittest
        suite = unittest.TestSuite()
        suite.addTests(tests.elixir_tests.get_suite())
        unittest.TextTestRunner().run(suite)

long_description = open('README.markdown', 'r').read()
setup(
    name='elixir_py',
    py_modules=['elixir'],
    cmdclass={'test': PyTest},
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Erlang',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
    ],
    version='1.0.0',
    description='Elixir Flavored Erlang Binary Term Format for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Michael Truog',
    author_email='mjtruog@protonmail.com',
    url='https://github.com/hansonkd/elixir_py',
)
