rm -r *.egg-info/
rm -r dist/

python setup.py sdist
twine upload dist/*

# pip install --upgrade pip
#pip install -i https://test.pypi.org/simple/ bvr