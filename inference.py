from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
def runModel(input_text):
    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.01},
    )
    template = """The following is a piece of automotive data text:
                {input_text}
            * Manufacturing Company (e.g., FORD)
            * Model (e.g., FORD FOCUS)
            * Part (e.g., ENGINE)
            * Failure Issue (e.g., amplification of the stress)
            * Repairing part (e.g.,  WILL INSPECT THE BATTERY CABLES)
            * Replaced Part (e.g., DAMAGED BATTERY CABLES REPLACED)
            Analyze the text and identify any entities belonging to these categories. If an entity is found, return the following information for each entity:
            Entity: The exact text representing the entity in the document.
            Label : The corresponding entity category from the predefined list.
            Example Output:
            {Entity: Spark Plugs, Label: Engine Components}
            If no entity is found return:
            {}
            """
    prompt = PromptTemplate(input_variables=["input_text"], template=template)
    response = llm(prompt.format(input_text=input_text))
    print(response)
    return response
