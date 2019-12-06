from setuptools import setup

setup(
    name='allsnek',
    entry_points={
        'console_scripts': [
            'snek = snek:main',
            'fancy = fancy:main',
            'fancysnek = fancysnek:fancysnek'
            
        ],
    
        
    }
)