import flet as ft

from MainScreen.SideMenu import side_menu


def bottom_menu(page: ft.Page):

    # page.add(
    #     ft.CupertinoSlidingSegmentedButton(
    #         selected_index=1,
    #         thumb_color=ft.colors.BLUE_400,
    #         on_change=lambda e: print(f"selected_index: {e.data}"),
    #         padding=ft.padding.symmetric(0, 10),
    #         controls=[
    #             ft.Text("call"),
    #             ft.Text("chats"),
    #             ft.Text("notes"),
    #         ],
    #     ),
    # )

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Какую задачу добавить?", width=500)

    panel_contacts = ft.Row()
    panel_chats = ft.Row()
    panel_notes = ft.Row([new_task, ft.ElevatedButton("+", on_click=add_clicked)])

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0:
            page.add(panel_contacts)
        elif index == 1:
            page.add(panel_chats)
        elif index == 2:
            page.add(panel_notes)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.PHONE_SHARP, label="Контакты"),
            ft.NavigationDestination(icon=ft.icons.CHAT, label="Чаты"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Заметки"
            ),
        ], on_change=navigate
    )
    page.add()


ft.app(target=bottom_menu)
