"""
Sample response: 
```json
{
 "has_function_calling": true,
 "function_calling": [
  "get_student_info(student_name='Trung')"
 ],
 "message": ""
}
```
"""
import json
from set_up import chat
from function_calling import (
    get_student_info,
    get_top_student_info,
    get_question_prompt,
    result_prompt
)

def extract_response_json(text):
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        return "{" + text[start+1:end] + "}"
    return None


def handle_with_function_calling(question):
    try:
        response = chat.send_message(get_question_prompt(question))
        response_json = extract_response_json(response.text)
        response_object = json.loads(response_json)
        if not response_object["has_function_calling"]:
            return response_object["message"]
        else:
            extra_information_list = []
            for function_calling in response_object["function_calling"]:
                extra_information = eval(function_calling)
                extra_information_list.append(extra_information)
            final_response = chat.send_message(result_prompt(question, extra_information_list))
            return final_response.text
    except:
        return "Xin lỗi, tôi không thể trả lời câu hỏi này lúc này"