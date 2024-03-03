# PrediiLabs
Task : Fine tune a large language model (LLM) for performing named entity recognition (NER) task on an automotive dataset.
Hugging face link : https://huggingface.co/NotMuchOfAHugger/llama-predii__ner
So to begin with, I downloaded the data given and using python libraries used the relevant columns for processing and converting it into tabular representation.
While readind the data, figured out some relevant entities. The entitites were : 'Manufacturing Company','Model','Part','Failure Issue','Repairing part','Replaced Part'
Explored the Large language model (LLM). Went though LLaMA 2 7b, phi-2. Used LLaMA 2 7B
Prompting techniques : First shot :  training a model to recognize named entities related to automobiles without providing any labeled data explicitly related to automotive entities during training.
Few Shots : training a model using a small set of labeled examples from the automotive domain and leveraging a pre-trained language model's capabilities to generalize to new entities and contexts.
The model fouses on zero shot learning prompt technique. 
Got some satisfactory outputs and began with fine tuning the model. Got good results in five iteration. 

