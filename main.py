# Стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO
# (англ. last in — first out, «последним пришёл — первым вышел»). Чаще всего принцип работы стека сравнивают
# со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии
# (стрельба начнётся с патрона, заряженного последним).

# Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок.
# Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,
# и пары скобок правильно вложены друг в друга.

# Пример сбалансированных последовательностей скобок:
#
# (((([{}]))))
# [([])((([[[]]])))]{()}
# {{[()]}}
# Несбалансированные последовательности:
#
# }{}
# {{[(])]}}
# [[{())}]
# Программа ожидает на вход строку со скобками. На выход сообщение: "Сбалансированно", если строка корректная,
# и "Несбалансированно", если строка составлена неверно.


class StackLIFO:

    def __init__(self, stack):
        self.stack = stack

    # is_empty - проверка стека на пустоту. Метод возвращает True или False.
    def is_empty(self):
        if self.stack == []:
            result = 'False'
        else:
            result = 'True'
        return result

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, element):
        self.stack.append(element)
        print(self.stack)

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        self.stack.pop()
        result = self.stack[-1]
        return result

    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        result = self.stack[-1]
        return result

    # size - возвращает количество элементов в стеке.
    def size(self):
        result = len(self.stack)
        return result

    def is_balanced(self):
        text = "".join(el for el in self.stack if el in "〈({[]})〉")
        print(text)
        result = 'Сбалансированно'
        while text:
            flag = True
            for el in "〈〉", "()", "{}", "[]":
                if el in text:
                    text = text.replace(el, "")
                    flag = False
            if flag:
                result = 'Несбалансированно'
                return result
        return result

if __name__ == '__main__':
    list1 = []
    Stack1 = StackLIFO(list1)
    print(Stack1.is_empty())
    element1 = 1
    element2 = 2
    element3 = 3
    Stack1.push(element1)
    Stack1.push(element2)
    Stack1.push(element3)
    print(Stack1.pop())
    print(Stack1.peek())
    print(Stack1.size())

    list2 = '# [([])((([[[]]])))]{()}' #balanced
    Stack2 = StackLIFO(list2)
    print(Stack2.is_balanced())

    list3 = '{{[(])]}}'#not balanced
    Stack3 = StackLIFO(list3)
    print(Stack3.is_balanced())



