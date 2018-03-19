#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
###description：脚本名不要命名mrjob.py会冲突

from mrjob.job import MRJob
class My_wordcount(MRJob):
    def mapper(self,key,line):
        for word in line.split():        
            yield word,1
    def reducer(self,word,occurrences):
        yield word,sum(occurrences)

if __name__=='__main__':
    My_wordcount.run()
