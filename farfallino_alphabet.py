from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date

class MySettings(BaseModel):
    required_int: int
    optional_int: int = 69
    required_str: str
    optional_str: str = "meow"
    required_date: date
    optional_date: date = 1679616000

@plugin
def settings_model():
    return MySettings

@tool
def get_farfallino_message(tool_input, cat):
    """Cypher the specified input and the output using the farfallino
    alphabet. Input is quoted using a '%' character. Output is the
    tool output replacing the '%' character. """

    farfallino_input = ""
    for char in tool_input:
        if char in ["a", "e", "i", "o", "u"]:
            farfallino_input += "f" + char
        else:
            farfallino_input += char

    return farfallino_input


@hook
def agent_prompt_prefix(prefix, cat):
    prefix = """You are a secret agent and you're very mysterious. You 
    are an expert spy and you can help the user with their secrets 
    message. 
"""
    return prefix
