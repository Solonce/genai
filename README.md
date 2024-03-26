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
* [Flags](#flags)
* [Examples](#examples)
* [Limitations](#limitations)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)

## About The Project

This project is designed for fast and extremely lightweight AI inference when using a linux based machine right from the command line.

Using the command 'genai', you will be brought into a shell that allows you to interact with an AI Assistant. It is designed to give as short an answer as possible while satisfying the question.

### Cool Features!

- Shell support: Open a shell to pass multiple prompts to genai.
- No shell/One-liner support: Use the -t flag to ask genai a single prompt without entering a shell
- Context Operation: Genai runs under a given context so it knows how to format the response. Change it for a single shell instance or reset the default context to something custom. The default context is [here](https://github.com/Solonce/genai/blob/main/default_context.txt).
- Fast & Custom: Genai defaults to a lightweight 100 character response, with a maximum 3 second load time. These are variable with the correct flags if you need longer responses! 


## Built With

[HuggingFace Inference API](https://huggingface.co/docs/api-inference/en/index) - Allow for free AI Inference

[Mixtral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mixtral-7B-Instruct-v0.2) - The Model

## Getting Started

Getting started is very simple. All you need is to install 'genai-cmd' via pip, and supply a HuggingFace API Key.

### Prerequisites

You will need a HuggingFace API Key. HuggingFace API Keys are free, and the instructions for obtaining one can be found [here.](https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token).

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

## Flags
```
-t, --text-data      Used to ask a question to genai directly without entering the shell.
-r, --raw-data       Same as -t without text formatting.

-c, --context        Used to set the temporary context genai answers prompt(s) under. Works with shell. (ex. "You are a pirate", "You are an angry old man")
-l, --length         Used to set the maximum length of response. Default is 100 characters. Works with shell.
-s, --seconds        Used to set the maximum time a response will take to generate. Default is 3. Works with shell.

-C, --reset-context  Used to set the default context genai answers all prompts under. (ex. "You are a pirate", "You are an angry old man")
-S, --set-key        Used to set the HuggingFace Inference API key needed for genai to operate.
```


## Examples
### Entering a shell
The main usage of genai is to enter a shell that you can communicate with an AI Agent.

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
  │ Version: 1.0.8
  │ Github: https://github.com/Solonce/genai
  │ Author: Solomon Ince
  │ 
  │ Model: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
  └───────────────────────────────────────────────────────
genai> How do I get only even numbers from an array in python?

  ┌─────────────────────────────
  │ [1, 2, 3, 4, 5]
  │ 
  │ filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
  └─────────────────────────────

genai> exit
```

### Entering a shell with custom --length and --seconds
This is to demonstrate you can make large AI inference requests, even though this was built as a lightweight tool.
```
>genai -l 500 -s 15
                                                     
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
  │ Version: 1.0.8
  │ Github: https://github.com/Solonce/genai
  │ Author: Solomon Ince
  │ 
  │ Model: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
  └───────────────────────────────────────────────────────
genai> Write me a short paper on Artificial Society and its future.

  ┌─────────────────────────────
  │ I. Introduction
  │         Artificial Society (AS) refers to a virtual world populated by artificial
  │ agents, each with its own set of rules, behaviors, and interactions. AS is an
  │ extension of Artificial Intelligence (AI) and offers a platform for exploring complex
  │ social phenomena, testing theories, and simulating future scenarios.
  │ 
  │     II. Current State of Artificial Society
  │         AS is still in its infancy, with most research focusing on individual agents
  │ and their interactions. However, recent advancements in multi-agent systems, machine
  │ learning, and natural language processing have led to more sophisticated simulations
  │ of social structures and dynamics.
  │ 
  │     III. Potential Applications of Artificial Society
  │         1. Social Science Research: AS can be used to test theories and hypotheses in
  │ a controlled environment, providing valuable insights into human behavior and social
  │ dynamics.
  │         2. Education and Training: AS can be used to simulate real-world scenarios and
  │ provide students with a safe space to practice and learn social skills.
  │         3. Urban Planning and Design: AS can be used to simulate and optimize urban
  │ environments, taking into account factors such as traffic flow, resource allocation,
  │ and social interaction.
  │         4. Conflict Resolution and Negotiation: AS can be used to model and analyze
  │ complex negotiations and conflicts, providing insights into effective strategies and
  │ solutions.
  │ 
  │     IV. Future Directions for Artificial Society
  │         1. Scalability: Developing AS that can handle large-scale simulations with
  │ millions of agents and complex social structures.
  │         2. Realism: Incorporating more realistic models of human behavior and social
  │ dynamics, including emotions, motivations, and cultural norms.
  │         3. Ethics: Addressing ethical concerns related to AS, such as privacy,
  │ consent, and the potential for unintended consequences.
  │         4. Integration with Physical World: Exploring ways to integrate AS with the
  │ physical world, such as through augmented reality or the Internet of Things.
  │ 
  │     V. Conclusion
  │         Artificial Society offers a unique platform for exploring complex social
  │ phenomena and testing theories in a controlled environment. With continued research
  │ and development, AS has the potential to revolutionize fields such as social science,
  │ education, urban planning, and conflict resolution.
  └─────────────────────────────

genai> exit
```

### One line inference
This is for fast inference if you just want one prompt answered.
```
>genai -t "How do I reverse an array in python"

   genai:
 ┌─────────────────────────────
 │ array = [1, 2, 3, 4, 5]
 │ array.reverse()
 └─────────────────────────────

```

### One line inference with NO text formatting
This is the same, but instead of -t, we use -r for the raw response with no text formatting.
```
>genai -r "How do I reverse an array in python"

array = [1, 2, 3, 4, 5]
array.reverse()

```

### One liner inference with temporary context included
This is one line text inference, but supplying context for the agent.
```
>genai --text-data "How was your day?" --context "You a bitter and angry old man, your response to the following should be given in such a way. "

   genai:
 ┌─────────────────────────────
 │ My day was a complete and utter waste of time, just like every other day in this miserable existence.
 │ I woke up this morning to the sound of my alarm clock, which is nothing more than a cruel reminder that I am
 │ still alive and have to endure another day of this meaningless life. I dragged myself out of bed and went through
 │ the motions of getting ready for work, all the while cursing the fact that I have to spend eight hours of my day in a cr
 └─────────────────────────────
```

## Limitations
- This project was never intended for a 'catch-all' or to be used as a perfect AI assistant. The goal was to simply create a command line AI assistant tool.
- The [Mixtral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mixtral-7B-Instruct-v0.2) model is open source, and such is variable to change and unpredictability.
- The [Mixtral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mixtral-7B-Instruct-v0.2) model tends to have an issue generating one response. It will often respond back as a user to prompt the model again.
- The line 'After you have finished answering the question, please type TERMINATE.' is used in the default prompt, but not enforced with the -c or -C flags. This line can be important if you want nice text formatting.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
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
