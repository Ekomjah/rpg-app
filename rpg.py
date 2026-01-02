full_dot = '●'
empty_dot = '○'
def create_character(name,strength, intelligence, charisma):
    if not isinstance(name, str): 
        return "The character name should be a string."
    if not(name):
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"

