#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from zipfile import ZipFile

class DownloadKaggleData:
    def __init__(self, competition = None, all_files = True, file = None, save_path = None, extract = True):
        
        self._all_files = all_files
        self._file = file
        self._competition = competition
        self._extract = extract
        
        if competition is None:
            raise ValueError("competition name is None")
        else:
            self._competition = competition
            
        if file is None and not all_files:
            raise ValueError("You must provide a file name or set all_files to True")
        elif not file is None:
            self._all_files = False
            self._file = file
        
        if save_path is None:
            raise ValueError("You must provide a data save path")
        else:
            self._save_path = save_path
        
        # get list competition files names 
        self._files = self.file_names()
        
        # download one or all files
        if not self._all_files and self._file in self._files:
            self.save_file(file = self._file)
            self._download_files = [self._file]
        elif not self._all_files:
            raise ValueError("There is not file called " + self._file)
        
        if self._all_files:
            self._download_files = self._files
            for tmp in self._files:
                self.save_file(tmp)
        
        # extract zip files        
        if self._extract:
            self.unzip_files()
        
    def file_names(self):
        # Commmand line kaggle API list competition files
        tmp = subprocess.getoutput("kaggle competitions files -c " + self._competition)
        tmp = tmp.split(sep = "\n")
        
        flag = True
        ind = 0
        while(flag):
            if "------" in tmp[ind]:
                ind += 1
                flag = False
            else:
                ind += 1
        
        tmp = tmp[ind:]
        
        return [a.split(" ")[0] for a in tmp]
        
    def save_file(self, file = None):
        # Commmand line kaggle API download competition file
        tmp = subprocess.getoutput("kaggle competitions download -c " + self._competition + " -f " + file + " -p " + self._save_path)
        print(tmp)
        pass
    
    def unzip_files(self):
        for zipf in self._download_files:
            if zipf.split(".")[-1] == 'zip':
                tmp = ZipFile(self._save_path + "/" + zipf, 'r')
                tmp.extractall(self._save_path)
                tmp.close()
    




        
