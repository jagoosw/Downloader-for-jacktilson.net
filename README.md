# Downloader for jacktilson.net
Simple script to download papers for WJEC A Level Maths from jacktilson.net
Set start_year (usually 2006), end_year (usually current year), the papers you want in the start of the script in the list names and the directory you want to put them in in the variable store.

For example for all C1, C2 and M1 papers from the years 2006 to 2017 stored in the directory /Users/John/Maths/Papers it would look like this

start_year = 2006
end_year = 2017
names = ["c1", "c2", "m1"] #Put the paper names you want here
store = "/Users/John/Maths/Papers/"#Put the directory you want the papers in here, remember the trailing /

After modifying the file run python paper_get.py 

Note: this is for the legacy specifcation and currently can not download winter papers becuase I'm not sitting any this year that were ever in the winter, although it could easily be modified to do so 
