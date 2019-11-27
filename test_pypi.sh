rm -r *.egg-info/
rm -r dist/

python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pip install -i https://test.pypi.org/simple/ bvr