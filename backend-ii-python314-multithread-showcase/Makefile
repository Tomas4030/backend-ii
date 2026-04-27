
setup:
	@uv python install 3.10 3.14.4 3.14t

run.314t:
	@uv python pin 3.14t
	@uv run --python 3.14t main.py


run.3.14:
	@uv python pin 3.14.4
	@uv run --python 3.14.4 main.py

run.3.10:
	@uv python pin 3.10
	@uv run --python 3.10 main.py


run.all: setup run.3.10 run.3.14 run.314t