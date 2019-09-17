#!/usr/bin/python
# -*- coding: UTF-8 -*-

import rpc

def login():
    user = 'admin'
    psw = '123'
    result = rpc.login(user, psw)
    #print 'login:',result
    
    sid = result.get('session_id')
    print 'sid:',sid
    
    return sid

def get_data():

    filename = 'CheckProblem.csv'

    line_no = 0

    records = []
    
    def fn( lines, records ):
        strs = lines.split('\t')
        #print len( strs )
        id,name0, name1, name2, card, order = strs
        #print id,name0, name1, name2, card, order
        #print [ line for line in lines ]
            
        if card == 'NULL':
            card = 'none'
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

    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                pass
                break

            if line_no:
                fn( lines, records )
                    
            line_no += 1
            

    for rec in  records:  
        print rec['id'],rec['order'], rec['card'],rec['name0'],rec['name1'],rec['name2']            
        pass


    return records




if __name__ == '__main__':

    sid = login()
    #set_company(sid)
    
    #set_station(sid)

    get_data()
    
 


