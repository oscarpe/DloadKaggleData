# Download kaggle competitions data from python

This code uses Kaggle API behind the scenes.  

## Installation Kaggle API 

More information, please visit https://github.com/Kaggle/kaggle-api or execute `pip install kaggle`.

After install, sign up for a Kaggle account at https://www.kaggle.com > 'Account tab' > 'Create API Token' > 'save kaggle.json'.

After that, create .kaggle folder in the location ~ and place this file in the location `~/.kaggle/kaggle.json`.

## Use Class 

Keep in mind that you must have account at Kaggle and also be enrolled in the competition.

Copy download_kaggle_data_class.py from src folder and follow the next examples.

## Examples

### All files

```
Path = "Your_Save_Path"
comp = "home-credit-default-risk"       
 
DownloadKaggleData(competition = comp, all_files = True, save_path = Path, extract = True)        
```

### One file

```
Path = "Your_Save_Path"
comp = "home-credit-default-risk"       
file = "HomeCredit_columns_description.csv"
 
DownloadKaggleData(competition = comp, all_files = False, file = file, save_path = Path, extract = False)        
```


