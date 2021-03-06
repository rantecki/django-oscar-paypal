#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-oscar-paypal',
      version='0.1',
      url='https://github.com/tangentlabs/django-oscar-paypal',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="PayPal payment module for django-oscar",
      long_description=open('README.rst').read(),
      keywords="Payment, PayPal",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(),
      install_requires=['django-oscar>=0.2',
                        'requests',
                        'purl'],
      )
