.PHONY: run reset

run:
	uvicorn main:app --reload

reset:
	mysql -u root < sql/reset.sql

app: reset run

.PHONY: clean
clean:
	rm -rf *.pyc __pycache__