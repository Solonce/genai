<br/>
<p align="center">
  <a href="https://github.com/Solonce/genai">
    <img src="genai_logo.png" alt="Logo" width="400" height="320">
  </a>
  
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

This project is designed for fast and extremely lightweight AI inference when using a linux based machine right from the command line.

Using the command 'genai', you will be brought into a shell that allows you to interact with an AI Assistant. It is designed to give as short an answer as possible while satisfying the question.



## Built With

[HuggingFace Inference API](https://huggingface.co/docs/api-inference/en/index) - Allow for free AI Inference

[Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) - The Model

## Getting Started

Getting started is very simple. All you need is to install 'genai-cmd' via pip, and supply a HuggingFace API Key.

### Prerequisites

You will need a HuggingFace API Key. HuggingFace API Keys are free, and the instructions for obtaining one can be found [here.](https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token).

### Installation

1. Get a free HuggingFace API Key [here.](https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token)

2. Use pip to install genai

```sh
pip install genai_cmd
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
>genai
                                                  
                                              88  
                                              ""  
                                                  
 ,adPPYb,d8  ,adPPYba, 8b,dPPYba,  ,adPPYYba, 88  
a8"    `Y88 a8P_____88 88P'   `"8a ""     `Y8 88  
8b       88 8PP""""""" 88       88 ,adPPPPP88 88  
"8a,   ,d88 "8b,   ,aa 88       88 88,    ,88 88  
 `"YbbdP"Y8  `"Ybbd8"' 88       88 `"8bbdP"Y8 88  
 aa,    ,88                                       
  "Y8bbdP"                                        

┌───────────────────────────────────────────────────────
│ Version: 1.0.4
│ Github: https://github.com/Solonce/genai
│ Author: Solomon Ince
└───────────────────────────────────────────────────────
genai> Write me a short poem about flowers
 ┌─────────────────────────────
 │ Flowers bloom in colors bright,
 │ Bathing in the warm sunlight.
 │ Petals soft, a gentle touch,
 │ Life's beauty, we can't get enough.
 └─────────────────────────────

genai> exit
```

```
>genai --text-data "How do I reverse an array in python"

   genai:
 ┌─────────────────────────────
 │ array = [1, 2, 3, 4, 5]
 │ array.reverse()
 └─────────────────────────────

```

```
>genai --raw-data "How do I reverse an array in python"

array = [1, 2, 3, 4, 5]
array.reverse()

```

```
>genai --text-data "How was your day?" --context "You a bitter and angry old man, your response to to the following should be given in such a way. "

   genai:
 ┌─────────────────────────────
 │ My day was a complete and utter waste of time, just like every other day in this miserable existence. I woke up this morning to the sound of my alarm clock, which is nothing more than a cruel reminder that I am still alive and have to endure another day of this meaningless life. I dragged myself out of bed and went through the motions of getting ready for work, all the while cursing the fact that I have to spend eight hours of my day in a cr
 └─────────────────────────────
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
