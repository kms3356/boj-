def solution(todo_list, finished):
    answer = [todo for todo, fin in zip(todo_list, finished) if fin == 0]
    return answer