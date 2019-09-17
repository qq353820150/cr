#!/usr/bin/python
# -*- coding: UTF-8 -*-



def get_data():
    filename = 'station.csv'

    line_no = 0

    records = []

    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            if not line_no:
                print lines
        
        
            if line_no:
                strs = lines.split('\t')
                #ID	SpeciesNo	SpeciesName	Remark	Purviews	HokerID	address	address_longitude	address_latitude
                id,code, name, Remark,Purviews, HokerID,address, address_longitude, address_latitude = strs
                #print id,code, name,address_longitude, address_latitude
                #print [ line for line in lines ]
            
                rec = {
                    'id':    int(id),
                    'type': '',
                    'parent': '',
                    'code': code,
                    'name': name,
                    'address_longitude': address_longitude,
                    'address_latitude':  address_latitude,
                }
                records.append(rec)

            line_no += 1

    for rec in  records:
        pass
        print rec['id'],rec['code'], rec['name'] 
    


get_data()

