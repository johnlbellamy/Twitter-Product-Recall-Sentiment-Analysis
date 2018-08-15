#!/usr/bin/env python
import re
import pickle
import os

class TextCleaner:
    """Takes a string from array-like objects and performs:
    alpha_iterator(text) -- Text in list (or array-like) format. Returns lower-case letters stripped of punctuation and numbers.
    stop_word_iterator(text) --  Removes common "stop" words, like "and."
    word_iterator(text, stop_words) -- Text and custom stop_words in list format. stop_words are words to be removed.
    can use this in-lieu of stop_word_iterator, or in addition to.
	
	GENERAL USAGE:
	1) Download file to chosen directory.
	2) from  TextCleaner2000.TextCleaner import TextCleaner
	3) Pass the install directory to tell TextCleaner where to locate files and initialize a cleaner instance:
	   WINDOWS: cleaner = TextCleaner("PATH\\TO\\INSTALL\\DIRECTORY\\TextCleaner2000")
	   LINUX/UNIX/IOS: cleaner = TextCleaner("PATH/TO/INSTALL/DIRECTORY/TextCleaner2000")
	4) cleaner is static method so to use the functions call: cleaner.function_name
	
	EXAMPLE USAGE:
	For the following examples, text refers to an array-like object. For best results, pass text as a list() or a Pandas DataFrame column: (assuming data_frame is a pandas DataFrame) data_frame["column_name"].
    For custom stopword removal, pass as a list().	
	
	GENERAL NUMBER AND PUNCTUATION REMOVAL:
	alpha_words = cleaner.alpha_iterator(text)
	
	COMMON STOPWORD REMOVAL:
	cleaned_of_stops = cleaner.stop_word_iterator(text)
	
	CUSTOM STOPWORD REMOVAL:
	cleaned_of_custom_stops = cleaner.custom_stop_word_iterator(text, stop_words)
	Remember that stop_words is a comma-separated list()."""
    
    def __init__(self, tc_2000_home):
        self.tc_2000_home = tc_2000_home
        pickle_file_path = os.path.join(tc_2000_home, 'stops.pkl')
        pkl_file = open(pickle_file_path, 'rb')
        self.stop_words = pickle.load(pkl_file) 
        pkl_file.close() 
              

    def __alphaizer(self, text):
        """Given a string (text), removes all punctuation and numbers.
        Returns lower-case words. Called by the iterator method
        alpha_iterator to apply this to lists, or array-like (pandas dataframe)
        objects."""
        self.text = text
      
        x = re.sub("[0-9,'--!@#$%=&:;<>\?\(\)\.\{\}\]\[\\\/-]+", " " , text)
        x = x.lower() #Makes letters lower-case
        x = re.sub("^\s" , "" , x) #Removes leading spaces
        x = re.sub("\s+$" ,"" , x) # Removes trailing spaces
        x = re.sub("  "," ", x) #Removes extra spaces
        
        return x
                

    def __stop_word_remover(self, text, stop):
        """Removes common stop-words like: "and", "or","but", etc. Called by
        stop_word_iterator to apply this to lists, or array-like (pandas dataframe)
        objects. """

        self.text = text
        self.stop = stop
        
        i = 0
        while i < len(stop):
            text = re.sub("\s"+stop[i]+"\s|^"+stop[i]+"\s|\s"+stop[i]+"$", " ", text)
            i += 1
        
        return text
     
    def stop_word_iterator(self, text):
        """Calls __stop_word_remover to apply this method to array-like objects.
        Usage: TextCleaner.stop_word_iterator(text)."""

        self.text = text
        
        text2 = [self.__stop_word_remover(x,self.stop_words) for x in text]
        
        return text2
  
    def alpha_iterator(self,text):
        """Calls __alphaizer to apply this method to array-like objects. Usage:
        TextCleaner.alphaizer(text)."""

        self.text = text
        text2 = [self.__alphaizer(x) for x in text]
        
        return text2

    def __word_remover(self, text, stop):
        """Removes custom stop-words. For example, "patient", or "medicine", if
        one is dealing with medical text. Can use this method to pass any set of stop
        words, or in-lieu of common stop-word method stop_word_iterator. Called by
        word_iterator to apply this to lists, or array-like (pandas dataframe)
        objects. """

        self.text = text
        self.stop = stop
     
        i = 0
        while i < len(stop):
            text = re.sub("\s"+stop[i]+"\s|^"+stop[i]+"\s|\s"+stop[i]+"$", " ", text)
            text = re.sub("  "," ", text) #Removes extra spaces
            text = re.sub("^\s" , "" , text) #Removes leading spaces
            text = re.sub("\s+$" ,"" , text) # Removes trailing spaces
            i += 1
        
        return text

    def custom_stop_word_iterator(self, text, stop_words):
        """Removes custom stop-words. For example, "patient", or "medicine", if
        one is dealing with medical text and do not want to include those words in analysis. Can use this method to pass any set of stop
        words, or in-lieu of common stop-word method stop_word_iterator.Calls __word_remover to apply this method to array-like objects. Usage:
        TextCleaner.custom_stop_word_iterator(text, stop_words), where stop-words and text are in a comma-
        separated list, or iterable."""

        self.text = text
        
        text2 = [self.__word_remover(x,stop_words) for x in text]
        
        
        return text2


      


