.DELETE_ON_ERROR:

test: RHO.zeo.gro RHO.cif.yap
%.zeo.gro: genice_cif/lattices/zeolite.py Makefile
	genice zeolite[$*] > $@
%.cif.yap: %.cif genice_cif/lattices/zeolite.py Makefile
	genice cif[$<] -f yaplot > $@

%: temp_% replacer.py genice_cif/lattices/zeolite.py genice_cif/__init__.py
	python replacer.py < $< > $@
	-fgrep '%%' $@





prepare: # might require root privilege.
	pip install genice cif2ice


test-deploy: build
	twine upload -r pypitest dist/*
test-install:
	pip install pillow
	pip install --index-url https://test.pypi.org/simple/ genice_cif



install:
	./setup.py install
uninstall:
	-pip uninstall -y genice-cif
build: README.md $(wildcard genice_cif/lattices/*.py)
	./setup.py sdist bdist_wheel


deploy: build
	twine upload dist/*
check:
	./setup.py check
clean:
	-rm *~ *gro *cif
	-rm -rf build dist *.egg-info
	-find . -name __pycache__ | xargs rm -rf
