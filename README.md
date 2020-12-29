# MyShellScripts

## Cloning Repo

```git clone https://github.com/espin086/MyShellScripts.git & cd MyShellScripts/```

## Decription and Usage of Files
---
Useful shell scripts for my personal use, at times they may be python scripts that run bash/linux commands. These are the shell scripts in this repository. 


* [delete_my_files.py](https://github.com/espin086/MyShellScripts/blob/main/delete_files.py) - can be used with a cronjob to delete files from my computer on an hourly basis. 

  * * In a linux terminal type:
```crontab -e```

  * * To run hourly on cron type the following, but modify based on your file path:
```0 * * * * * python /Users/jjespin/Documents/mygithub/MyShellScripts/delete_files.py```
