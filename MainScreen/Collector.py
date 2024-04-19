import flet as ft
from SideMenu import side_menu
from SelectelBottomMenu import bottom_menu


def collector_main_screen(page: ft.Page):
    side_menu(page)
    bottom_menu(page)


ft.app(target=collector_main_screen)
