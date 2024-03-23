<br/>
<p align="center">
  <h3 align="center">genai</h3>

  <p align="center">
    A Command Line AI Assistant powered by Mixtral-8x7B-Instruct-v0.1 using the HuggingFace Inference API.
    <br/>
    <br/>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/Solonce/genai?color=dark-green) ![Stargazers](https://img.shields.io/github/stars/Solonce/genai?style=social) ![Issues](https://img.shields.io/github/issues/Solonce/genai) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)

## About The Project

![Screen Shot](images/screenshot.png)

This project is designed for fast and extremely lightweight AI inference when using a linux based machine right from the command line.

Using the command 'genai', you will be brought into a shell that allows you to interact with an AI Assistant. It is designed to give as short an answer as possible while satisfying the question.



## Built With

HuggingFace Inference API - Allow for free AI Inference

Mixtral-8x7B-Instruct-v0.1 - The Model

## Getting Started

Getting started is very simple. All you need is to install 'genai-cmd' via pip, and supply a HuggingFace API Key.

### Prerequisites

You will need a HuggingFace API Key. HuggingFace API Keys are free, and the instructions for obtaining one can be found here.

### Installation

1. Get a free HuggingFace API Key [here.](https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token)

2. Use pip to install genai

```sh
pip install genai-cmd
```

3. Set the HuggingFace API Key

```sh
genai -S 'HF_API_KEY'
```

4. Have Fun!
Use the following command to enter a shell!

```sh
genai
```

## Usage

Here is some basic usage:

```
GENAI SHELL - CTRL+C FOR EXIT
genai> How do I reverse a string in python?

s = input()
print(s[::-1])

genai> What does KeyboardInterrupt mean in python?

KeyboardInterrupt is an exception that is raised when the user presses the interrupt key (normally Control-C or Delete).

genai> Write me a script to get the live OHLC of BTC on Kraken using Kraken public API

import requests
import json

def get_btc_ohlc():
    url = "https://api.kraken.com/0/public/OHLC?pair=XBTUSD"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['result']['XXBTZUSD']

print(get_btc_ohlc())

```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/Solonce/genai/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/Solonce/genai/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/Solonce/genai/blob/main/LICENSE.md) for more information.

## Authors

* **Solomon Ince** - *AI/ML Programmer* - [Solomon Ince](https://github.com/Solonce/) - *genai*
