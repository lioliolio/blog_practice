migrate:
	- python blog/manage.py makemigrations blog users posts bitly
	- python blog/manage.py migrate

test:
	- pep8 .
	- python blog/manage.py test blog users posts bitly
