migrate:
	- python blog/manage.py makemigrations blog users posts bitly
	- python blog/manage.py migrate
