import pandas as pd
import time
from .types import Uniform, Discrete
import random
import sys
sys.path.append("..") # to import one directory up
from src.types import Uniform, Discrete
class Model:
    """Represents a model class
    
    Attributes
    ---------
        input_template : Dict
            Input template dictionary
        inputs : List
            List holding Model inputs 
    """
    inputs = []
    def __init__(self, inputs_template):
        self.inputs_template = inputs_template
        
    def __repr__(self):
        return f"{self.inputs}"
    
    def __str__(self):
        return f"{self.inputs}"
    
    def get_inputs_as_df(self):
        """Function returns inputs as a Dataframe
        """
        model_inputs_dict = {}
        for i in self.inputs:
            model_inputs_dict[i.variable_name] = i.value
            
        return pd.DataFrame([model_inputs_dict]).reset_index(drop=True)
    
    def generate(self):
        """For 03-create-model.ipynb 
        
        TODO: Implement generate function. 
        
        This function needs to iterate through the `inputs_template` dictionary
        that you pass in the constructor and needs to create a list containing
        inputs for the model. For example if inputs_template looks like this:
        
        
        OrderedDict([('PERM',
              OrderedDict([('generator', 'uniform'),
                           ('min_value', 500),
                           ('max_value', 2500)])),
             ('PORO',
              OrderedDict([('generator', 'uniform'),
                           ('min_value', 0.1),
                           ('max_value', 0.25)])),
             ('AQ_SIZE',
              OrderedDict([('generator', 'uniform'),
                           ('min_value', 0.5),
                           ('max_value', 50)])),
             ('CHAN',
              OrderedDict([('generator', 'discrete'),
                           ('choices', ['few', 'some', 'many'])]))])
        
        You want to generate a model_inputs list that looks like this 
        
        model_inputs=
        [PERM:2189.8833075395087,PORO:0.17159581263029622,AQ_FIZE:36.21321636919663,CHAN:many]
        """

        model_inputs = []


        for key, val in self.inputs_template.items():

            generator = val["generator"]

            if generator == "uniform":
                min_value = val["min_value"]
                max_value = val["max_value"]

                model_input = Uniform(variable_name=key, min_value=min_value, max_value=max_value)
                model_inputs.append(model_input)

            elif val["generator"] == "discrete":
                # TODO: Add Discrete to model_inputs
                choices=val["choices"]
                model_input = Discrete(variable_name=key, choices=choices)
                model_inputs.append(model_input)
                
                self.inputs = model_inputs
        
class Simulator:
    """Represents a simulator class 
    """
    def simulate(self, model):
        """Simulates a Model
        
        Parameters
        ----------
            model : Model
                A single Model() object
        
        Returns
        -------
            simulator_output : Uniform 
        """
        print(f"[LOG] Simulating Model: {model}")
        time.sleep(random.randint(1,5))
        simulator_output = Uniform("mq", 0,1)
        print("[LOG] Done")
        return simulator_output.value