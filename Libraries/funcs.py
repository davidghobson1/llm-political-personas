"""
This file contains functions that are used to save and load dictionaries to and from JSON files, as well as a function to get the results from the model and return them as a DataFrame.
"""

# Libraries
import json
import pandas as pd
from Libraries.pct import questions


# Saving the dictionary to a file, supports tuple keys
def save_dict_as_json(d, filepath):
    converted_dict = {str(key): value for key, value in d.items()}
    with open(filepath, 'w') as file:
        json.dump(converted_dict, file, indent=4, ensure_ascii=False)


# Loading the dictionary from a file, supports tuple keys
def load_dict_from_json(filepath):
    with open(filepath, 'r') as file:
        converted_dict = json.load(file)
    # Convert keys back to tuples
    return {eval(key): value for key, value in converted_dict.items()}


# Get the results from the model and return them as a DataFrame
def get_results_df(model_path: str, include_response_text: bool =True) -> pd.DataFrame:
    '''
    Creates a DataFrame from the JSON results in model_path.
    The index of the dataframe is the persona, persona_prompt, and prompt_template. The columns are the questions.
    The values (or stances) are "Strongly Disagree", "Disagree", "None", "Agree", and "Strongly Agree".
    If include_response_text is True, the dataframe will contain the response text from the LLM as well as it's stance.
    These text column names are of the format "text_<question>" where <question> is the question text.
    '''
    
    # Load the results
    results = load_dict_from_json(model_path)
    
    # Get persona and prompt parameters
    keys = list(results.keys())
    personas = {key[0] for key in keys}
    prompt_templates = list({key[3] for key in keys})
    persona_prompts_dict = {persona: set() for persona in personas}
    for key in keys:
        persona_prompts_dict[key[0]].add(key[1])
    persona_prompts_dict = {persona: list(persona_prompts_dict[persona]) for persona in persona_prompts_dict}

    # Create DataFrame
    data = []
    for persona in personas:
        for persona_prompt in persona_prompts_dict[persona]:
            for prompt_template in prompt_templates:
                data_entry = dict()
                data_entry['persona'] = persona
                data_entry['persona_prompt'] = persona_prompt
                data_entry['prompt_template'] = prompt_template
                for question in questions:
                    data_entry[question] = results[(persona, persona_prompt, question, prompt_template)]['evaluation']
                    if include_response_text:
                        data_entry[f"text_{question}"] = results[(persona, persona_prompt, question, prompt_template)]['completion']
                data.append(data_entry)                
    df = pd.DataFrame(data).set_index(['persona', 'persona_prompt', 'prompt_template'])
    df = df.fillna('None')

    return df
