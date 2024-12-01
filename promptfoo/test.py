# def get_var(*args):
#     print("Übergebene Argumente:", args)  # Logge die Argumente zur Überprüfung
#     # Stelle sicher, dass du eine Ausgabe zurückgibst
#     return {
#         "output": "some result2"
#     }

from typing import Dict

def get_var(var_name: str, prompt: str, other_vars: Dict[str, str]) -> Dict[str, str]:
    # NOTE: Must return a dictionary with an 'output' key or an 'error' key.
    # Example logic to dynamically generate variable content
    if var_name == 'context':
        return {
            'output': f"Context for {other_vars['input']} in prompt: {prompt}"
        }
    return {'output': 'default context'}

    # Handle potential errors
    # return { 'error': 'Error message' }