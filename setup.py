from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'MyApp',
        'CFBundleDisplayName': 'MyApp',
        'CFBundleGetInfoString': 'Conversor de archivos Excel a JSON',
        'CFBundleIdentifier': 'com.miempresa.miaplicacion',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0',
        'CFBundleExecutable': 'MyApp',
        'LSUIElement': '1',
    },
    'packages': ['tkinter', 'jpype', 'convert'],
    'includes': ['tkinter', 'jpype', 'convert'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)