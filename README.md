# Tutorial 1
First, tidy up the files that you want to compile with Cython, for example, such as strings and spaces as shown below
![IMG_20220313_121546](https://user-images.githubusercontent.com/101085369/158046243-97fa5714-ade5-4506-a4f7-4a257c7bb718.jpg)
If you've trimmed the file, then the 2nd tutorial

# Tutorial 2
Rename Your File.py To File.pyx Like The Image Below
![IMG_20220313_121606](https://user-images.githubusercontent.com/101085369/158046265-28c27b3f-3c45-442f-92ed-0fee19c06a70.jpg)
If It Has Been Changed Continue Tutorial 3
# Tutorial 3
In the setup.py file there is a reading for example.pyx Change the reading to be your file name Example

![IMG_20220313_121533](https://user-images.githubusercontent.com/101085369/158046285-d7144f4a-15c4-4de7-a7cf-d06625cca70b.jpg)

- file.pyx

If you have continued to Tutorial 4

# Tutorial 4
Install the cython module first before running the setup.py file
```
pip install cython
```

Run the setup.py file with the following command

```
python setup.py build_ext --inplace
```
![IMG_20220313_121719](https://user-images.githubusercontent.com/101085369/158046222-76265b3c-7f82-4ec9-8bd9-dd73bc606ce2.jpg)
If the setup.py file path is like in the picture above then the cython compilation is successful Continue to tutorial 5
# Tutorial 5
Go to your folder where you put the file and delete the file as shown below
![IMG_20220313_121702](https://user-images.githubusercontent.com/101085369/158046308-ace0e980-f60f-4a31-b165-51875cff6113.jpg)


If you have deleted files and folders as above You only need to use a file named cython-310.so Carry on

# Tutorial 6
And the results will be like this
![IMG_20220313_121645](https://user-images.githubusercontent.com/101085369/158046336-3bc81901-43c4-40af-864b-3d0df4dc4475.jpg)

- Good luck
