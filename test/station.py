#!/usr/bin/python
# -*- coding: UTF-8 -*-

import rpc

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
        #print rec['id'],rec['code'], rec['name']
    
    return records
    

def get_company():
    records = get_data()
    
    comps = [ rec for rec in records if len( rec['code'] ) <= 4]
    for rec in comps:
        pass
        #print rec['id'],rec['code'], rec['name']
    
    comps = [ {
        'cr_base_company_id': comp['code'],
        'cr_base_company_name': comp['name'],
    } for comp in comps ]
    
    return comps

def login():
    user = 'admin'
    psw = '123'
    result = rpc.login(user, psw)
    #print 'login:',result
    
    sid = result.get('session_id')
    print 'sid:',sid
    
    return sid


def set_company(sid):
    comps = get_company()
    model = 'cr.base.company'
    print model
    
    for comp in comps:
        rec = rpc.execute(sid, model,'search', [('cr_base_company_id','=', comp['cr_base_company_id'])] )
        if rec:
            print 'old:', rec[0]
            continue
            
        rid = rpc.execute(sid, model,'create', comp )
        print 'new:', rid


def get_part():
    records = get_data()
    
    recs = [ {
            'id': rec['id'],
            'code': rec['code'],
            'parent': rec['code'][0:4],
            'name': rec['name']
        } 
        for rec in records 
        if len( rec['code'] ) == 6 and rec['code'][-2:] == '01' ]
        
    for rec in recs:
        pass
        #print rec['id'], rec['parent'],  rec['code'], rec['name']
        
    return recs
    
def set_part(sid):
    records = get_part()
    model = 'cr.base.part'
    print model
    
    for rec in records:
        data = rpc.execute(sid, model,'search', [('cr_base_part_id','=', rec['code'])] )
        if data:
            print 'old:', data[0]
            continue
        
        parent_id = rpc.execute(sid, 'cr.base.company','search', 
            [('cr_base_company_id','=', rec['parent'])] )
        
        
        if not parent_id:
            continue
            
        parent_id = parent_id[0]
        
        vals = {
            'cr_base_part_name': rec['name'],
            'cr_base_part_id': rec['code'],
            'cr_base_company_id': parent_id,
        }
        
        rid = rpc.execute(sid, model,'create', vals )
        print 'new:', rid


def get_station():
    records = get_data()
    
    recs = [ {
            'id': rec['id'],
            'code': rec['code'],
            'parent': rec['code'][0:4] + '01',
            'name': rec['name']
        } 
        for rec in records 
        if len( rec['code'] ) == 6 ]
        
    for rec in recs:
        pass
        print rec['id'], rec['parent'],  rec['code'], rec['name']
        
    return recs

def set_station(sid):
    records = get_station()
    model = 'cr.base.station'
    print model

    for rec in records:
        data = rpc.execute(sid, model,'search', [('cr_base_station_id','=', rec['code'])] )
        if data:
            print 'old:', data[0]
            continue
        
        parent_id = rpc.execute(sid, 'cr.base.part','search', 
            [('cr_base_part_id','=', rec['parent'])] )
        
        
        if not parent_id:
            continue
            
        parent_id = parent_id[0]
        
        vals = {
            'cr_base_station_name': rec['name'],
            'cr_base_station_id': rec['code'],
            'cr_base_part_id': parent_id,
        }
        
        rid = rpc.execute(sid, model,'create', vals )
        print 'new:', rid
   


def get_location():
    return [
        {'code': 'second', 'name': '高架层'},
        {'code': 'second2', 'name': '高架夹层'},
        {'code': 'first', 'name': '平层'},
        {'code': 'below', 'name': '地下层'},
        {'code': 'east', 'name': '站前东广场'},
        {'code': 'west', 'name': '站前西广场'},
        {'code': 'south', 'name': '站前南广场'},
        {'code': 'north', 'name': '站前北广场'},
    ]
    


def set_location(sid):
    records = get_location()
    model = 'cr.base.position'
    print model

    station_ids = rpc.execute(sid, 'cr.base.station','search',  [] )
    
    def fn( station_id, rec ):
        data = rpc.execute(sid, model,'search', [
                ('cr_base_position_id','=', rec['code']),
                ('cr_base_station_id','=', station_id),
            ])
            
        if data:
            print 'old:', data[0]
            return
        
        vals = {
            'cr_base_position_name': rec['name'],
            'cr_base_position_id': rec['code'],
            'cr_base_station_id': station_id,
        }
        
        rid = rpc.execute(sid, model,'create', vals )
        print 'new:', rid
          
        
    
    for station_id in station_ids:
        for rec in records:
            fn(station_id, rec)
        
   

if __name__ == '__main__':

    sid = login()
    #set_company(sid)
    
    #set_station(sid)

    set_location(sid)
    
    
    #ptn = rpc.execute(sid, 'res.partner','search_read', [],['name'])
    #print ptn
    