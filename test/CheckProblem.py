#!/usr/bin/python
# -*- coding: UTF-8 -*-

filename = 'CheckProblem.csv'

line_no = 0

records = []

with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
            pass
        
        if line_no:
            strs = lines.split('\t')
        
            #print len( strs )
        
            id,name0, name1, name2, card, order = strs
            #print id,name0, name1, name2, card, order
            #print [ line for line in lines ]
            
            if card == 'NULL':
                card = None
            if card == '红牌':
                card = 'red'
            if card == '白牌':
                card = 'white'
            if card == '黄牌':
                card = 'yellow'
            
            
            
            rec = {
                'id':    int(id),
                'name0': name0,
                'name1': name1,
                'name2': name2,
                'card':  card,
                'order': int(order),
            }
            
            records.append(rec)
        
        line_no += 1
        
        
    pass

for rec in  records:
    print rec['id'],rec['order'], rec['card'],rec['name0'],rec['name1'],rec['name2']