.DELETE_ON_ERROR:
GENICE=genice2
BASENAME=genice2_cif
PIPNAME=genice2-cif
GITNAME=genice-cif

test: RHO.zeo.gro.test RHO.cif.yap.test
%.zeo.gro: genice2_cif/lattices/zeolite.py Makefile
	( cd $(BASENAME) && $(GENICE) zeolite[$*] ) | grep -v Command > $@
%.cif.yap: $(BASENAME)/%.cif genice2_cif/lattices/zeolite.py Makefile
	( cd $(BASENAME) && $(GENICE) cif[$*.cif] -f yaplot ) | grep -v Command > $@
%.test:
	make $*
	diff $* ref/$*


%: temp_% replacer.py $(wildcard $(BASENAME)/lattices/*.py) $(wildcard $(BASENAME)/*.py) pyproject.toml
	python replacer.py $< > $@


test-deploy:
	poetry publish --build -r testpypi
test-install:
	pip install --index-url https://test.pypi.org/simple/ $(PIPNAME)
uninstall:
	-pip uninstall -y $(PIPNAME)
build: README.md $(wildcard genice2_cif/*.py)
	poetry build
deploy:
	poetry publish --build
check:
	poetry check


clean:
	-rm $(ALL) *~ */*~ *svg CS2.png
	-rm -rf build dist *.egg-info
	-find . -name __pycache__ | xargs rm -rf
