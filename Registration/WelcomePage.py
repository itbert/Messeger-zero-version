import json
import flet as ft

# Register


def welcome_reg(page: ft.Page):
    def button_clicked(e):
        profile_base_set = {'name': tb1.value,
                            'surname': tb2.value,
                            'username': tb3.value,
                            'password': tb4.value}

        profile_json = json.dumps(profile_base_set)

        with open("profile_info.json", "w") as file:
            file.write(profile_json)

        page.update()

    tb1 = ft.TextField(label="Имя", hint_text="Введите текст")
    tb2 = ft.TextField(label="Фамилия", hint_text="Введите текст")
    tb3 = ft.TextField(label="Пользователь", hint_text="Введите текст")
    tb4 = ft.TextField(label="Пароль", password=True, can_reveal_password=True)
    but_sub = ft.ElevatedButton(text="Зарегистрироваться", on_click=button_clicked, autofocus=True, bottom=True)
    page.add(tb1, tb2, tb3, tb4, but_sub)


ft.app(target=welcome_reg)
