#rebuild
cd docs
sphinx-build -b html -W source _build/html

#load/view doc
sphinx-autobuild docs/source docs/_build/html