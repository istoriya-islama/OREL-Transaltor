import flet as ft
from mtranslate import translate

# Словарь языков
languages = {
    'ألعربية': 'ar',
    'Русский': 'ru',
    'Türkçe': 'tr',
    'English': 'en',
    'Azərbaycan': 'az',
    'Український': 'uk',
     'ئۇيغۇر': 'ug'}

def main(page: ft.Page):
    page.title = "OREL Translator 2.0"
    page.theme_mode = "dark"
    page.window_width = 500
    page.window_height = 390
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    lang_names = list(languages.keys())

    # Элементы интерфейса
    combo_from = ft.Dropdown(
        options=[ft.dropdown.Option(lang) for lang in lang_names],
        value=lang_names[0],
        width=140
    )

    combo_to = ft.Dropdown(
        options=[ft.dropdown.Option(lang) for lang in lang_names],
        value=lang_names[1],
        width=140
    )

    arrow = ft.Text("→", size=30, color="white", weight="bold")

    text_input = ft.TextField(
        multiline=True,
        label="Enter text",
        width=450,
        height=120,
        text_style=ft.TextStyle(size=14, weight="bold")
    )

    text_output = ft.TextField(
        multiline=True,
        label="Translation",
        width=450,
        height=120,
        text_style=ft.TextStyle(size=14, weight="bold"),
        read_only=True
    )

    def translate_click(e):
        src_lang = combo_from.value
        dest_lang = languages.get(combo_to.value)
        if dest_lang:
            result = translate(text_input.value, dest_lang)
            text_output.value = result
            page.update()

    translate_btn = ft.ElevatedButton(
        text="Translate",
        width=450,
        on_click=translate_click
    )

    def theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    # Размещение на странице
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=theme),
                ft.Text("OREL Translator 2.0")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([combo_from, arrow, combo_to], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([text_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([translate_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([text_output], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
