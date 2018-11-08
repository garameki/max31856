from setuptools import setup, find_packages

setup(
	name='max31856',
	version='0.0',
	packages=find_packages("."),
	url='https://github.com/garameki/max31856',
	license='MIT',
	author='USAKU Takahashi',
	author_email='garameking@gmail.com',
	install_requires=[
	],
	description='Measure temperature using R-type Heat-Junction, Adafruit MAX31856 module & Raspberry Pi3 B+ via spi interface',
	platforms='OS : Raspbian strech in Raspberry Pi3 B+',
	classifiers = [
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
	],
)
