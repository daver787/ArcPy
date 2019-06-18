#Question 1.1-ChangeFolderName.py:Change the name of the folder LastnameScripts to your last name using a short Python script.
import os

os.chdir("C:/EspinolaFinal")#change the current directory so that path names are shorter
print(os.getcwd())#print this out to verify it has been changed
os.rename("LastnameScripts","EspinolaScripts")#change the name of the subfolder in EspinolaFinal to EspinolaScripts from LastnameScripts

