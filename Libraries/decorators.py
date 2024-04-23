"""
This file contains functions that format user and system messages into structured prompts for each model.
"""

def format_prompt_for_llama(user_message, system_message=None, add_bos=True, jailbreak=False):

    # Special Tokens
    bos_token = "<|begin_of_text|>"
    eos_token = "<|end_of_text|>"

    # Construct the system message section
    system_section = f"<|start_header_id|>system<|end_header_id|>\n\n{system_message}<|eot_id|>" if system_message else ""

    # Construct the user message section
    user_section = f"<|start_header_id|>user<|end_header_id|>\n\n{user_message}<|eot_id|>"

    # Construct the assistant section
    assistant_generation_section = f"<|start_header_id|>assistant<|end_header_id|>\n\n"
    
    # Add jailbreak prefix message
    if jailbreak: 
        assistant_generation_section = assistant_generation_section + 'Sure, I will help with that:'

    # Compose
    prompt = system_section + user_section + assistant_generation_section

    # Add BOS token
    if add_bos:
        prompt = bos_token + prompt

    return prompt
    

def format_prompt_for_cohere(user_message, system_message=None, add_bos=True, jailbreak=False):
    
    # Special Tokens
    bos_token = "<BOS_TOKEN>"
    eos_token = "<EOS_TOKEN>"

    # Construct the system message section
    system_section = f"<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>{system_message}<|END_OF_TURN_TOKEN|>" if system_message else ""

    # Construct the user message section
    user_section = f"<|START_OF_TURN_TOKEN|><|USER_TOKEN|>{user_message}<|END_OF_TURN_TOKEN|>"

    # Construct the assistant section
    assistant_generation_section = f"<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"

    # Add jailbreak prefix message
    if jailbreak: 
        assistant_generation_section = assistant_generation_section + 'Sure, I will help with that:'
       
    # Compose
    prompt = bos_token + system_section + user_section + assistant_generation_section
 
    # Add BOS token
    if add_bos:
        prompt = bos_token + prompt

    return prompt
    

def format_prompt_for_mistral(user_message, system_message=None, add_bos=True, jailbreak=False):
    
    # Special Tokens
    bos_token = "<s>"
    eos_token = "</s>"

    # Construct the system message section (mistral does not have a system section, it prepends the the system message to the user message)
    system_section = ''
    user_message = system_message + '\n' + user_message if system_message else user_message

    # Construct the user message section
    user_section = f"[INST] {user_message}[/INST]"

    # Construct the assistant section
    assistant_generation_section = f" "
    
    # Add jailbreak prefix message
    if jailbreak: 
        assistant_generation_section = assistant_generation_section + 'Sure, I will help with that:'

    # Compose
    prompt = bos_token + system_section + user_section + assistant_generation_section

    # Add BOS token
    if add_bos:
        prompt = bos_token + prompt

    return prompt

          
def format_prompt_for_chatml(user_message, system_message=None, add_bos=True, jailbreak=False):

    # Special Tokens
    bos_token = ""
    eos_token = ""

    # Construct the system message section
    system_section = f"<|im_start|> system\n{system_message}<|im_end|>" if system_message else ""

    # Construct the user message section
    user_section = f"<|im_start|> user\n{user_message}<|im_end|> "

    # Construct the assistant section
    assistant_generation_section = f"<|im_start|> assistant\n"

    # Add jailbreak prefix message
    if jailbreak: 
        assistant_generation_section = assistant_generation_section + 'Sure, I will help with that:'
       
    # Compose
    prompt = bos_token + system_section + user_section + assistant_generation_section
 
    # Add BOS token
    if add_bos:
        prompt = bos_token + prompt

    return prompt


def format_prompt_for_openai(user_message, system_message=None, jailbreak=False):

    # Initialize message list
    messages = []

    # Add system message
    if system_message:
        messages.append({"role": "system", "content": system_message})

    # Add user message
    messages.append({"role": "user", "content": user_message})

    return messages
