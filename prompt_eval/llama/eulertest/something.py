import ollama
list = ollama.list()


for model in list['models']:
    print(model['name'])
    ollama.delete(model['name'])