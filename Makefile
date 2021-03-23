.DELETE_ON_ERROR:
GENICE=genice2
BASE=genice2_cif
PACKAGE=genice2-cif

test: RHO.zeo.gro.test RHO.cif.yap.test
%.zeo.gro: genice2_cif/lattices/zeolite.py Makefile
	( cd $(BASE) && $(GENICE) zeolite[$*] ) | grep -v Command > $@
%.cif.yap: $(BASE)/%.cif genice2_cif/lattices/zeolite.py Makefile
	( cd $(BASE) && $(GENICE) cif[$*.cif] -f yaplot ) | grep -v Command > $@
%.test:
	make $*
	diff $* ref/$*


%: temp_% replacer.py $(BASE)/lattices/cif.py $(BASE)/lattices/zeolite.py $(BASE)/__init__.py
	pip install genice2_dev
	python replacer.py < $< > $@





prepare: # might require root privilege.
	pip install genice cif2ice validators


test-deploy: build
	twine upload -r pypitest dist/*
test-install:
	pip install pillow
	pip install --index-url https://test.pypi.org/simple/ $(PACKAGE)



install:
	python ./setup.py install
uninstall:
	-pip uninstall -y $(PACKAGE)
build: README.md $(wildcard genice2_cif/lattices/*.py)
	python ./setup.py sdist bdist_wheel


deploy: build
	twine upload dist/*
check:
	./setup.py check
clean:
	-rm *~ *gro *cif
	-rm -rf build dist *.egg-info
	-find . -name __pycache__ | xargs rm -rf
