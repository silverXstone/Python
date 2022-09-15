"""Write a Python program to display the examination schedule. (extract the date from 
exam_st_date).
exam_st_date = (11, 12, 2022)
Sample Output: The examination will start from : 11 / 12 / 2022"""

import datetime
ex = datetime.datetime(2022,11,12)
print(ex.strftime("%x"))
