# Console chatbot with function calling

## Setup
1. Create virtual environment
```bash
virtualenv venv
```
2. Activate venv
```bash
venv/Scripts/acvivate
```

3. Install dependencies and model:
```bash
python setup.py
```

## Start LLM server
```bash
python -m llama_cpp.server --model models/functionary-7b-v2.q4_0.gguf --chat_format functionary-v2 --hf_pretrained_model_name_or_path ./models
```


Idea: 
- Get information from csv file. Ex: Get grades data of AI K2
- Add informatioon to csv file

Luồng xử lý:
1. Prompt -> trả về {has_function_calling: bool, function_name: str, question}
2. Exec(function_name) -> result
3. Prompt mới -> trả về kết quả