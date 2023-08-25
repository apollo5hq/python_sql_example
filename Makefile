.PHONY: run reset

run:
	flask run

reset:
	mysql -u root -p < sql/resetdb.sql

app: reset run

.PHONY: clean
clean:
	rm -rf *.pyc __pycache__