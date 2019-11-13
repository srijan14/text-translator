# Text Translator
This project provide a
[python package](https://pypi.org/project/text-translator/) along with
[pre-trained](https://github.com/srijan14/Machine-Translation-Models-And-Data)
models to perform machine translation on text

## Getting Started
Below instructions will get you a copy of the project up and running
your local machine for development and testing purposes.
### Prerequisites

```
python>=3.6
```

## Installing

```
pip install text-translator
```

## Usage

1. Loading Library
    ```
    from translator import Translator
    translator = Translator()
    ```
    
2. Model Loading(Pretrained models for multiple language conversion can
   be found
   [here](https://github.com/srijan14/Machine-Translation-Models-And-Data))
    ```
    translator.load_model(MODEL_PATH)
    ```
    
3. Prediction

    ```
    translator.translate("What is your name?")  
    आपका नाम क्या है?
    ```
    
    ```
    translator.translate(["What is your name?","What is your age?"])
    आपका नाम क्या है?
    आपकी उम्र क्या है?
    ```

## [Pretrained Models](https://github.com/srijan14/Machine-Translation-Models-And-Data)

## Authors

* [**Srijan Sharma**](https://github.com/srijan14)

## License

This project is licensed under the Apache License - see the
[LICENSE.md](./LICENSE) file for details

## Acknowledgments

* [Open-NMT](https://github.com/OpenNMT/OpenNMT-py)
