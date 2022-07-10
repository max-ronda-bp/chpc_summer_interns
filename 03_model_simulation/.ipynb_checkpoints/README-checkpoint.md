# Model Runner/Sampling Workflow

## Learning Objectives:
- Build a sampling/simulation workflow
- Learn how to interact with `.hjson` files
- Learn how to interact with `OrderedDicts`
- Learn about `Python classes/objects` 
- Learn how to read code base and implement new features
- Learn how to write data to disk
- Learn how to read data and visualize it
- Learn how to optimize code 

## Prompt:
A reservoir engineer (RE) has asked you to design software that can run their reservoir models through their in-house physics simulator. The RE will provide you with a template file that will contain the description of the inputs they are trying to pass through the `simulator` and they will like those inputs to be sampled according to the described distribution. The input file, `model_input_description.hjson`, contains the inputs that you will read in, create models, and lastly run them through the simulator. 


## Model Simulation Diagram

<img src="images/model_sim_diagram.PNG" align="center" max-width="200px">

At the end of this assignment, you should have a directory structure that will look something like this:


```python
/username/your_local_directory/models
├── models
│   ├── model_0
│   │   ├── model_inputs.csv
│   │   ├── mq.value
│   ├── model_1
│   │   ├── model_inputs.csv
│   │   ├── mq.value
│   ├── model_2
│   │   ├── model_inputs.csv
│   │   ├── mq.value
│   ├── model_n
│   │   ├── model_inputs.csv
│   │   ├── mq.value
```

## Next:

Navigate to notebooks folder and start with notebook `00-intro.ipynb` to begin working on this project. Each notebook will have a `controls` tab at the bottom that will help you move around between each step of the project.

## Bonus:

The last notebook, 07-read-inputs-outputs_bonus.ipynb, is extra credit. Please reach out to one of the TAs if you get to that part. 