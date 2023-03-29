# pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
# pip 20.0.2
echo -n "Current pip version: "
python3 -m pip --version | cut -d " " -f 1,2

echo -n "pip install: "
pip install --log install.log --target=./local_lib --force-reinstall git+https://github.com/jaraco/path.py.git

echo -n Execute Output:
./my_program.py
