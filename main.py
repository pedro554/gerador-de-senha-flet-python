import flet
from random import choice
import string
from flet import (
	Page, Checkbox, Row, 
	ElevatedButton, TextField, Text)

def main(page: Page):
	def gen_pass(e):
		tamanho_senha = 10
		caracteres = ''
		senha_gerada = ''

		if lowcase.value:
			caracteres += string.ascii_lowercase
		if uppcase.value:
			caracteres += string.ascii_uppercase
		if numbers.value:
			caracteres += string.digits 
		if punc.value:
			caracteres += string.punctuation

		for i in range(tamanho_senha):
			senha_gerada += choice(caracteres)

		senha.value = senha_gerada 
		page.update()

	senha = TextField(label='Senha', read_only=True)
	lowcase = Checkbox(label='Lowercase', value=True)
	uppcase = Checkbox(label='Uppercase', value=True)
	numbers = Checkbox(label='Numbers', value=True)
	punc = Checkbox(label='Punctuations', value=True)

	page.add(
		Row(
			[
				senha,
			]
		),
		Row(
			[
				lowcase,
				uppcase,
				numbers,
				punc,
			]
		),
		Row(
			[
				ElevatedButton(
					'Gerar senha',
					on_click=gen_pass
				)
			]
		)
	)

	page.window_width = 600
	page.window_height = 250
	page.update()

flet.app(target=main, view=flet.WEB_BROWSER)