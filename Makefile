push:
	git add .
	git commit -m"$(m)"
	git push

active:
	mv index.html t.html
	mv tmp.html index.html
	mv t.html tmp.html
