SHELL := /bin/bash 

dir_en := $(shell basename `pwd`)_en
dir_pl := $(shell basename `pwd`)_pl

# single depth of a tree is assumed
notebooks := $(wildcard */*.ipynb)

notebooks_en := $(foreach d,$(notebooks), ../$(dir_en)/$(d) )
notebooks_pl := $(foreach d,$(notebooks), ../$(dir_pl)/$(d) )

.PHONY: clean pdf notebooks dirs clean_output test

test: 
	@echo $(notebooks_pl)
#	@echo $(notebooks)


to_en: $(notebooks_en)
	@echo Converted to english!

to_pl: $(notebooks_pl)
	@echo Converted to polish!



../$(dir_en)/%.ipynb: %.ipynb

	@echo Making dir in ../$(dir_en)
	@mkdir -p $(shell dirname $@)

	@echo CLEANING OUTPUT of $< 
	@jupyter nbconvert --ClearOutputPreprocessor.enabled=True --clear-output $< 

	@echo Converting notebook  $< to english $@
	@jupyter nbconvert --to selectLanguage --NotebookLangExporter.language=en  $< --stdout > $@ 

../$(dir_pl)/%.ipynb: %.ipynb

	@echo Making dir in ../$(dir_pl)
	@mkdir -p $(shell dirname $@)

	@echo CLEANING OUTPUT of $< 
	@jupyter nbconvert --ClearOutputPreprocessor.enabled=True --clear-output $< 

	@echo Converting notebook  $< to polish $@
	@jupyter nbconvert --to selectLanguage --NotebookLangExporter.language=pl  $< --stdout > $@ 



log1 := $(shell test -d ../$(dir_en) || mkdir -v ../$(dir_en))
log2 := $(shell test -d ../$(dir_pl) || mkdir -v ../$(dir_pl))
