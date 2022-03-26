# Step 1

Install the cython module first before running the setup.py file
```
pip install cython
```
# Step 2
Rename your .py file to D3M09.pyx for cythonize your file

```
mv (Your filename.py) D3M09.pyx
```


# Step 3
Run the setup.py file with the following command

```
python setup.py build_ext --inplace
```

# Step 4
Use D3M09.py file for run your cythonize file

# Note
You only need to use a file named cython-310.so Carry on

- Good luck
