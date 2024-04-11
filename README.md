## Solid Abstract Factory

This repository demonstrates the implementation of an Abstract Factory in Python.  

Under [project/models](https://github.com/evertonsavio/python-factory-serializer/tree/master/project/models) we have a class called `Song.py` that inherits Serializable.py
This allows an instance of `Song.py` being able to serialize itself choosing a FormatType like JSON or XML. You can check this on [main.py](https://github.com/evertonsavio/python-factory-serializer/blob/master/main.py).

For implementing a new format using this code we only need to add our new format implementation file under [serializers](https://github.com/evertonsavio/python-factory-serializer/tree/master/serializer/serializers/impl) and register it on [registers.py](https://github.com/evertonsavio/python-factory-serializer/blob/master/serializer/constants/registers.py). That's it, all your model classes that inherits [Serializable.py](https://github.com/evertonsavio/python-factory-serializer/blob/master/serializer/Serializable.py) now can serialize itself to the new format.
We don't need to change anything on the class factories or on the core implementation. Check this PR for more information on how this can be done: [PR](https://github.com/evertonsavio/python-factory-serializer/pull/1)

## Python

1. Create your environment:
```commandline
python -m venv .venv
```
2. Activate your environment
```commandline
 . ./.venv/Scripts/activate 
.\venv\Scripts> . activate
```
3. install your dependencies
```commandline
pip install -r ./requirements.txt
```
4. Run project
```commandline
python main.py
```
5. Deactivate Environment
```commandline
deactivate
```
### Development
```
pip install PyYAML
pip freeze > requirements.txt
```