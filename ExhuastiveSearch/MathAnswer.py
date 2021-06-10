def solution(answers):

    student1 = list(range(1, 6)) * 2000
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000

    i, j, k = 0, 0, 0

    for q_index, answer in enumerate(answers):
        if student1[q_index] == answer:
            i += 1
        if student2[q_index] == answer:
            j += 1
        if student3[q_index] == answer:
            k += 1

    order = {1:i, 2:j, 3:k}
    max_answer = max(order.values())
    print(max_answer)

    return [k for k, v in order.items() if v == max_answer]
