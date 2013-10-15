ftp-db
=======

description:
------------
python script and php script for populating gftp database and searching it.

How this works:
---------------
1.  Run python script, (via cron would be best) to populate MySQL table of files in a certain directory.
2.  place search.html and search2.php in your web folder
3.  make sure you modify all the files to point to your MySQL database


Note:
-----
All thanks to nokocode, who saw this and noticed I wasn't sanitizing inputs to mysql and bad shit could have happened.
