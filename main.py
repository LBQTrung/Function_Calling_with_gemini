from handle_response import handle_with_function_calling

MAX_QUESTION = 5
index = 0

while (index < MAX_QUESTION):
    question = input("😎: ")
    print(f"🤖: {handle_with_function_calling(question)}")
    index += 1
