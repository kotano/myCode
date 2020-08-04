

gunicorn:
	export FLASK_APP=application.py && \
	export FLASK_ENV=development && \
	gunicorn --workers=4 --bind=127.0.0.1:5000 application:app

hey:
	@echo 'HEY'


flaskdebug:
	export FLASK_APP=application.py && \
	export FLASK_ENV=development && \
	python3 -m flask run
