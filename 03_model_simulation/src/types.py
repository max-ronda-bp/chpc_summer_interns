import numpy as np

class Uniform:
    """Represents a uniform distribution variable. 
    
    Attributes
    ----------
    min_value: float
        The minimum value 
    max_value: float
        The maximum value
    """
    def __init__(self, variable_name, min_value, max_value):
        self.variable_name = variable_name
        self.min_value = min_value
        self.max_value = max_value
        self.value = self.generate()
    
    def __repr__(self):
        return f"{self.variable_name}:{self.value}"
    
    def __str__(self):
        return f"{self.variable_name}:{self.value}"
    
    def generate(self):
        return np.random.uniform(self.min_value, self.max_value)

class Discrete:
    """
    Represents a discrete input
    
    Attributes
    ----------
    choices: list
        List of any type 
    """
    def __init__(self, variable_name, choices):
        self.variable_name = variable_name
        self.choices = choices
        self.value = self.generate()
        
    def __repr__(self):
        return f"{self.variable_name}:{self.value}"
    
    def __str__(self):
        return f"{self.variable_name}:{self.value}"
    
    def generate(self):
        return np.random.choice(self.choices)
    
# TODO: perhaps add another type here