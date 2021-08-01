# Задание 1
# Создайте класс Editor, который содержит методы view_document и
# edit_document. Пусть метод edit_document выводит на экран информацию о том,
# что редактирование документов недоступно для бесплатной версии. Создайте
# подкласс ProEditor, в котором данный метод будет переопределён. Введите с
# клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр
# класса ProEditor, иначе Editor. Вызовите методы просмотра и редактирования
# документов.

class Editor:

    def __init__(self):
        pass

    def view_document(self):
        print("The document is opening")

    def edit_document(self):
        print("Editing is not available for free version")


class ProEditor(Editor):

    def edit_document(self):
        print("The editing is available")


def main():
    license_key = str(input("Please enter your license key => "))
    if license_key == "hhh333":
        used_version = ProEditor()
        ProEditor.view_document(used_version)
        ProEditor.edit_document(used_version)
    else:
        used_version_2 = Editor()
        Editor.view_document(used_version_2)
        Editor.edit_document(used_version_2)


main()
