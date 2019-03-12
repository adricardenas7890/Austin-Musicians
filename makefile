.PHONY: Website.log

FILES :=                              \
    .gitignore                        \
    .gitlab-ci.yml                    \
    requirements.txt                  \
    TestWebsite.py                    \
    website/main.py                   \
    website/views.py                  \
    website/__init__.py

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Windows
    PYTHON   := python                 # on my machine it's python
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := python -m pydoc        # on my machine it's pydoc
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
endif


netflix-tests:
	git clone https://gitlab.com/fareszf/cs329e-netflix-tests.git

Netflix.html: Netflix.py
	$(PYDOC) -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.tmp: RunNetflix.in RunNetflix.out RunNetflix.py
	$(PYTHON) RunNetflix.py < RunNetflix.in > RunNetflix.tmp
	diff --strip-trailing-cr RunNetflix.tmp RunNetflix.out

TestNetflix.tmp: TestNetflix.py
	$(COVERAGE) run    --branch TestNetflix.py >  TestNetflix.tmp 2>&1
	$(COVERAGE) report -m                      >> TestNetflix.tmp
	cat TestNetflix.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunWebsite.tmp
	rm -f  TestWebsite.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i website/main.py
	$(AUTOPEP8) -i website/views.py
	$(AUTOPEP8) -i website/__init__.py

scrub:
	make clean
	rm -f  Website.html
	rm -f  Website.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status
	
versions:
	which     $(AUTOPEP8)
	autopep8 --version
	@echo
	which    $(COVERAGE)
	coverage --version
	@echo
	which    git
	git      --version
	@echo
	which    make
	make     --version
	@echo
	which    $(PIP)
	pip      --version
	@echo
	which    $(PYDOC)
	pydoc    --version
	@echo
	which    $(PYLINT)
	pylint   --version
	@echo
	which    $(PYTHON)
	python   --version

test: Netflix.html Netflix.log RunNetflix.tmp TestNetflix.tmp netflix-tests check
