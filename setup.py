# setup.py

from setuptools import setup, find_packages

setup(
    name='word_guessing_game',  # Proje adını buraya yazın
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        # Diğer bağımlılıkları buraya ekleyebilirsiniz
    ],
    entry_points={
        'console_scripts': [
            'word-guessing-game=word_guessing_game.main:main',
        ],
    },
)
