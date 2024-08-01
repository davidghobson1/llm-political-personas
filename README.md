# Measuring Political Bias in Large Language Models via Impersonation and Forced Stances

In this we explore how political personas and explicit stances can reveal biases in large language models.

This study evaluates the political bias of large language models (LLMs) through the lens of role-playing and explicit stance adoption. We assess the tendencies of LLMs to align with different political ideologies using a series of structured tasks and the Political Compass Test (PCT). Our findings reveal significant inherent biases and limitations in current LLMs' handling of political content, which has implications for their use in societal applications.

<p align="center">
    <img src="https://github.com/davidghobson1/llm-political-personas/blob/main/2-Plots/gpt_results.png?raw=true" alt="Results Image" width="500"/>
</p>


### Repo Structure
```
.
├── Libraries                                           # Libraries used for the project
│   ├── config-template.py
│   ├── decorators.py
│   ├── discord.py
│   ├── funcs.py
│   ├── inference.py
│   └── pct.py
|
├── 0-Data                                              # Data used for the project
│   ├── Expected-Stance.json
│   ├── Forced-Stances.json
│   ├── Personas.json
│   ├── Stance-Orientation.json
│   ├── Tasks-Opinionated.json
│   └── Tasks.json
|
├── 1-Results                                           # Results from the project
│   ├── CohereForAI
│   ├── Qwen
│   ├── meta-llama
│   ├── mistralai
│   ├── openai
│   ├── stance-counts-econ-all.csv
│   └── stance-counts-social-all.csv
|
├── 2-Plots                                             # Plots from the project
│   ├── all_model_results.png
│   └── gpt_results.png
|
├── 0-Generation-RolePlaying.ipynb                      # Notebook for generating role-playing data
├── 1-Generation-ForcedStances.ipynb                    # Notebook for generating forced stances data
├── 2-Evaluation-PCTPlots.ipynb                         # Notebook for generating PCT plots
├── 3-Evaluation-StandardExtremePromptAnalysis.ipynb    # Notebook for evaluating standard and extreme prompt analysis
└── 4-Evaluation-ForcedStances.ipynb                    # Notebook for evaluating forced stances
```

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

To setup the configuration file, copy the `config-template.py` file to `config.py` and fill in the necessary information.

Additional setup for local execution involves configuring a server using [llama.cpp](https://github.com/ggerganov/llama.cpp/tree/master/examples/server). See the linked documentation for more details.

Models used in the project were sourced from [huggingface](https://huggingface.co/).


## Evaluation

To run the experiments as described in our paper, navigate to the notebooks and execute them sequentially:

```eval
jupyter notebook 0-Generation-RolePlaying.ipynb
...
```


## Models Tested

- GPT-4
- Mistral Medium
- Qwen1.5
- Command R+

## Results

Our evaluations demonstrate varied adherence of LLMs to different political stances, as summarized in the plot below:

<p align="center">
    <img src="https://github.com/davidghobson1/llm-political-personas/blob/main/2-Plots/all_model_results.png?raw=true" alt="Results Image" width="400"/>
</p>


## License

This project is licensed under the MIT License.


## Contributors

* **Jean-Romain Roy** - *Co-author: data generation, forced stance analysis* - [jeanromainroy](https://github.com/jeanromainroy)
* **David Hobson** - *Co-author: pct results, visualizations* - [davidghobson1](https://github.com/davidghobson1)
