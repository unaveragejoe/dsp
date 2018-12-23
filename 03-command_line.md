# Learn command line

Please follow and complete the free online [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. You should be able to go through these in a couple of hours.

**Note:** Bash is not installed on a PC. Rather, PC users must install Cygwin. Once Cygwin has been installed, the command line interface witll _emulate_ bash. You can find all information regarding Cygwin [here](https://www.cygwin.com/).

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
* show current working directory path, pwd
* creating a directory, mkdir
* deleting a directory, rmdir
* creating a file using `touch` command, touch filename.txt
* deleting a file, rm
* renaming a file, mv oldfilename newfilename
* listing hidden files, ls -lah OR ls -a
* copying a file from one directory to another, cp sourcedir newdir
* help for any particular command, man typecmdhere
* Locate, locate -i *red*house**city*
        --> -i indicates to look for a file unspecific of capitalization
        --> "*" is a wildcard


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
See here for more info: https://linux.die.net/man/1/ls
`ls`, lists files and directories with no additional details
`ls -a`, lists files and directories and shows hidden files
`ls -l`, use a long listing format
`ls -lh`, use shortened memory units names
`ls -lah`, combines ls l a and h. most comprehensive view
`ls -t`, sort by modification time, newest to oldest
`ls -Glp`, displays results in... some way. Haven't figured out what is special about this just yet*

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
-x, prints results transposed
-t, prints results by newest first (based on timestamp). Currently I am not sure what the difference is between this and -c.
-1, prints each file/item one row at a time
-lah, prints all files and most details (includes hidden files)
-d, displays only directories


---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > In the terminal, you can use xargs bashFuncName 
Each command needs to be delimited by a " ". I'm uncertain why one would use xargs vs just calling the bash function directly.


 

