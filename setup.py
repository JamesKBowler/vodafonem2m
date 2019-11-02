from distutils.core import setup
setup(
  name = 'vodafonem2m',
  packages = ['vodafonem2m'],
  version = '0.1',
  license='GNU GENERAL PUBLIC LICENSE',
  description = 'Provides access to Vodafone M2M endpoints via the REST API.',
  author = 'James K Bowler',
  author_email = 'james.bowler@datacentauri.com',
  url = 'https://github.com/JamesKBowler/vodafonem2m',
  download_url = 'https://github.com/JamesKBowler/vodafonem2m/archive/0.1.tar.gz',
  keywords = ['Vodafone M2M Python API', 'Vodafone M2M', 'Python M2M'],
  install_requires=[
        requests
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
    'Programming Language :: Python :: 3.6',
  ],
)
