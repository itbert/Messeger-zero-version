import json

import flet as ft


def side_menu(page: ft.Page):

    with open('*/profile_info.json', 'r') as file:
        info = file.read()
        file.close()

    def navigation_side_menu(e):
        index = page.navigation_bar.selected_index
        page.clean()

        panel_profile = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Ваш профиль'),
                        ft.Text(f'Ваше имя: {info['name']}'),
                        ft.Text(f'Ваша фамилия: {info['surname']}'),
                        ft.Text(f'Ваш уникальный ник: {info['username']}')
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        if index == 0:
            page.add(panel_profile)

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Профиль",
                icon=ft.icons.MENU,
                selected_icon_content=ft.Icon(ft.icons.MENU_OPEN),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            )
        ], on_change=navigation_side_menu
    )

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Светлая тема" if page.theme_mode == ft.ThemeMode.LIGHT else "Тёмная тема"
        )
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    c = ft.Switch(label="Светлая тема", on_change=theme_changed)

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.add(ft.ElevatedButton('МЕНЮ', on_click=show_drawer, icon=ft.icons.MENU))
    page.add(ft.Container(width=10, height=10), c)


ft.app(side_menu)
