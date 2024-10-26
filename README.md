# dunossauro

Curso

https://fastapidozero.dunossauro.com/

Capítulos concluídos:
	FastAPI do Zero!
	Configurando o ambiente de desenvolvimento
	Introdução ao desenvolvimento WEB
	Estruturando o Projeto e Criando Rotas CRUD
	Configurando o banco de dados e gerenciando migrações com Alembic
	Ingerando Banco de Dados a API
	Autenticação e Autorização com JWT
	Refatorando a Estrutura do Projeto
	Tornando o sistema de autenticação robusto

Install

- pipx

py -m pip install --user pipx

- Poetry

C:\Users\<user>\AppData\Roaming\Python\Python312\Scripts\pipx.exe install poetry

Create Project

C:\Users\<user>\pipx\venvs\poetry\Scripts\poetry.exe new fast_zero

Create venv

C:\Users\<user>\pipx\venvs\poetry\Scripts\poetry.exe install

Add FastAPI

C:\Users\<user>\pipx\venvs\poetry\Scripts\poetry.exe add 'fastapi[standard]'

Chamar a máquina virtual do poetry

C:\Users\<user>\pipx\venvs\poetry\Scripts\poetry.exe shell

Rodar o servidor

fastapi dev fast_zero/app.py
uvicorn fast_zero.app:app --reload

Ferramentas usadas

poetry add --group dev pytest pytest-cov taskipy ruff
poetry add sqlalchemy
poetry add pydantic-setting
poetry add alembic
poetry add pyjwt "pwdlib[argon2]"
poetry add pytz
poetry add --group dev factory-boy
poetry add --group dev freezegun

Migração da base de dados:
	alembic init migrations
	alembic revision --autogenerate -m "create users table"
	alembic upgrade head


Configuração do Ruff no pyproject.toml

[tool.ruff]
line-length = 79
extend-exclude = ['migrations']

Configuração do Linter no pyproject.toml

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

Configuração do Formatter no pyproject.toml

[tool.ruff.format]
preview = true
quote-style = 'single'

Configuração do pytest no pyproject.toml

[tool.pytest.ini_options]
pythonpath = "."
addopts = "-p no:warnings"

Configuração do Taskipy no pyproject.toml

[tool.taskipy.tasks]
lint = 'ruff check .; ruff check . --diff'
format = 'ruff check . --fix; ruff format .'
run = 'fastapi dev fast_zero/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'


