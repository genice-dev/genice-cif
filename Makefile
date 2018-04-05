.DELETE_ON_ERROR:
OS=$(shell uname)
ifeq ($(OS), Darwin)
	DEST=~/Library/Application\ Support/GenIce
else
	DEST=~/.genice
endif

test: RHO.zeo.gro RHO.cif.gro
%.zeo.gro: lattices/zeolite.py Makefile
	genice zeolite[$*] > $@
%.cif.gro: %.cif lattices/zeolite.py Makefile
	genice cif[$<] > $@
install:
	install -d $(DEST)
	install -d $(DEST)/lattices
	install lattices/*py $(DEST)/lattices
clean:
	-rm *~ *gro *cif
	-rm -rf */__pycache__
