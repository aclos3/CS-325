Written by Junhyeok Jeong
This is README.txt for explaining how to compile binpack.py and binpack_random.py

###if you have binpack.py and binpack_random.py file on your ssh directory

1. Make the files be excutable on ssh
chmod +x binpack.py
chmod +x binpack_random.py

2. Before compile binpack.py or binpack_random.py, make sure the input data file(bin.txt) is existed on your directory 
and make sure your python3 is above version 3.5 + because of print(f"output") function (new function of .format).

3. if your python3 version is lower than 3.5, then update it with this command
sudo apt-get update
sudo apt-get install python3.6 or python3.7  

4. As the file is written as python 3, compile with this command on ssh
python3 binpack.py
or
python3 binpack_random.py

5. if the file contents are statisfied, then result will be printed on the terminal after compile !


###The HW8 2-a.ltx and HW8 2-b.ltx files are for problem 2, so the files can open with LINDO software.

Thank you !
