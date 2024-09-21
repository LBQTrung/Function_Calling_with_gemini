# Coding samples
import inspect
import pandas as pd



df = pd.read_csv("./scores.csv")



# ========== Declare functions calling ==========
def get_student_info(student_name):
    """
    Reads input and returns the information of students in AI K2 class whose names contain the specified substring.
    """
    if df.empty:
        return []
    student_info = df[df['Name'].str.contains(student_name, case=False, na=False)]
    return student_info.to_dict(orient='records')


def get_top_student_info():
    """
    Reads input and returns the information of the student with the highest score.
    """
    if df.empty:
        return []
    max_score = df['Score'].max()
    print("có chạy")
    top_students = df[df['Score'] == max_score]
    return top_students.to_dict(orient='records')


def add_student(name, student_id, score):
    """Adds a new student to the CSV file."""
    new_student = pd.DataFrame([[name, student_id, score]], columns=['Name', 'ID', 'Score'])
    new_student.to_csv("./scores.csv", mode='a', header=False, index=False)
    return {"status": "success"}



# ========== Convert functions into strings ==========
function_calling_list = [get_top_student_info, get_student_info]
function_calling_string_list = [inspect.getsource(function_calling) for function_calling in function_calling_list]




# ========== Add strings into object in order to prepare prompt ==========



# ========== Prepare prompt ==========
CONTEXT_PROMPT = f"""
    Hãy nhớ những danh sách hàm dưới đây và thực hiện theo yêu cầu: {function_calling_string_list}
"""

def get_question_prompt(question):
    return f"""
    Câu hỏi: {question}
    Kiểm tra câu hỏi nó có liên quan đến thông tin điểm của lớp AI K2 không
và đưa ra đầu ra là một json có key và value như sau:
    - has_function_calling: True nếu có hàm được gọi, False nếu không.
    - function_calling: Một danh sách các chuỗi, mỗi chuỗi là lệnh gọi hàm tương ứng với yêu cầu của người dùng.
    - message: Trong trường hợp has_function_calling bằng False, trả về một string trả lời câu hỏi người dùng một cách bình thường
    """

def result_prompt(question, references):
    return f"""
    Câu hỏi: {question}
    Hãy trả lời câu hỏi dựa vào thông tin sau: {references}
    Đầu ra: là một string trả lời câu hỏi trên 
    """