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

### Instance DownloadKaggleData class

```
comp = DownloadKaggleData()       

# competitions list    
list_competitions = comp._list_competitions

# competitions files list        
list_competitions_files = comp.list_competitions_files(competition="home-credit-default-risk")
```
### All files

```
destination_path ="/your/destination/path/" 

comp.download_files(competition="home-credit-default-risk", 
                    save_path=destination_path)

```

### Multiple files

```
destination_path ="/your/destination/path/" 

files = ['sample_submission.csv.zip', 'HomeCredit_columns_description.csv']

comp.download_files(competition="home-credit-default-risk", 
                    competition_files=files,
                    save_path=destination_path)


```

### Extract Zip Files

```
comp.unzip_files()

```






