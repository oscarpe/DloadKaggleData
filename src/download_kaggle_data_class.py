#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from zipfile import ZipFile

class DownloadKaggleData:
    def __init__(self):
        
        # list competitions
        self._list_competitions = self.list_competitions()
        
    def download_files(self, competition = None, competition_files = [], all_files = True, save_path = None):
        
        """ Download Kaggle data from Python
        
        Input arguments:
            competition -- name of competition (str)
            all_files -- download all files from competition (bool)
            competition_files -- list of files to download from competition (list)
            save_path -- Destination path (str)
            
        Output:
            Print progress  
        
        """
        
        self._all_files = all_files
        self._competition_files = competition_files
        self._save_path = save_path
        
        if self._save_path is None:
            raise ValueError('invalid path destination value')
        
        
        if competition is not None and competition in self._list_competitions:
            self._competition = competition
        else:
            raise ValueError('invalid competition value')
        
        # list competition files
        self._files = self.list_competitions_files(competition = self._competition)
        
        if len(self._competition_files) > 0:
            self._all_files = False
            
            for tmp_save in self._competition_files:
                if tmp_save in self._files:
                    self.save_file(tmp_save)
                else:
                    raise ValueError("There is not file in competition called " + tmp_save)
                
            self._download_files = self._competition_files    
                
        elif self._all_files:
            for tmp_save in self._files:
                self.save_file(tmp_save)
                
            self._download_files = self._files
        else:
            raise ValueError('competitions_file is empty and all_files is not True')        
            
    
    def list_competitions(self):
        tmp = subprocess.getoutput("kaggle competitions list")        
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

    def list_competitions_files(self, competition = None):
        # Commmand line kaggle API list competition files
        tmp = subprocess.getoutput("kaggle competitions files -c " + competition)
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
    
    def unzip_files(self):
        for zipf in self._download_files:
            if zipf.split(".")[-1] == 'zip':
                tmp = ZipFile(self._save_path + "/" + zipf, 'r')
                tmp.extractall(self._save_path)
                tmp.close()
        print("all files unzipped success")





