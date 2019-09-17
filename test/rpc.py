# coding: utf-8 -*- coding: UTF-8 -*-


import requests
import json

HOST = 'http://192.168.56.101:8069'

SERVER = 'CR'

def ret(r):
    print 'status_code:', r.status_code
    print 'raw:', r.raw.read()
    print 'content:', r.content
    #print 'text:', r.text
    print 'headers:', r.headers

def t1(host=HOST):
    headers = {"content-type": "application/json" ,"credentials": "include"  }
    uri = host + '/json/test1'
    params = {}
    data = {}
    rspd = requests.post(uri,params=params,
                      data=json.dumps(data),
                      headers=headers)
                      
    ret(rspd)

print('t1')
#t1()

def jsonrpc(uri, data=None, params=None, sid=None, client=None):
        headers = {"content-type": "application/json"  }
        data1 = {"jsonrpc":"2.0",
                "method":"call",
                "id":123,
                "params":data and data or {}
                }
        
        params1 = params and params.copy() or {}
        if sid:                      
            params1.update( {'session_id':sid} )

        
        if not client:
            client=requests
        
        rspd = client.post(uri,params=params1,
                          data=json.dumps(data1),
                          headers=headers)
        #print rspd
        #ret(rspd)
        
        content = json.loads(rspd.content)
        res = content.get('result',{})
        
        error = content.get('error',{})

        if error:
            print uri, data, sid
            print error
            
            
            return None

        return json.loads(rspd.content).get('result',{})

def login(user,psw):
    url = HOST + '/json/user/login'
    return jsonrpc(url, {'db': SERVER,'login':user, 'password':psw } )
        
def execute0(sid, model, method, *args, **kwargs ):
    URI_API       = HOST + '/json/api0'
    return jsonrpc(URI_API,{'model':model, 'method': method, 
        'args': args, 'kwargs': kwargs },sid=sid )

def execute(sid, model, method, *args, **kwargs ):
    URI_API       = HOST + '/json/api'
    return jsonrpc(URI_API,{'model':model, 'method': method, 
        'args': args, 'kwargs': kwargs },sid=sid )

if __name__ == '__main__':
    user = 'admin'
    psw = '123'
    result = login(user, psw)
    print 'login:',result
    
    sid = result.get('session_id')
    print 'sid:',sid
    
    #ptn = execute(sid, 'res.partner','search_read2', [('id','=',3)],
    #    { 'category_id': None, 'property_product_pricelist': None,  'industry_id': None } )
    #print ptn

    #ptn = execute(sid, 'res.partner','read2', 3,
    #    { 'category_id': None, 'property_product_pricelist': None,  'industry_id': None }  )
    #print ptn

    #ptn = execute(sid, 'res.partner','search_read2', [('id','=',3)],['name',['company_id',['name']],['category_id',['name']] ])
    #print ptn

    print '14234234234232'

    ptn = execute(sid, 'res.partner','search_count', [], 
      context={'sdaa':12312} )
    print 'product', ptn

    ptn = execute(sid, 'account.invoice','search_read2', 
      [], {}  )
    print 'data', ptn



"""
    ptn = execute(sid, 'ir.logging','fields_get2', [] )
    print 'product', ptn
    
    ptn = execute(sid, 'account.invoice','fields_get2', [] )
    print 'product', ptn

    ptn = execute(sid, 'account.invoice','search_read2', [], #{'invoice_line_ids':{}} 
    )
    print 'data', ptn


    
    ptn = execute(sid, 'account.move','fields_get2', [] )
    print 'product', ptn

    ptn = execute(sid, 'account.move','search_read2', [], {'line_ids':{}} )
    print 'data', ptn


    

    ptn = execute(sid, 'res.groups','fields_get2', [] )
    print 'product', ptn

    ptn = execute(sid, 'res.groups','search_read2', [], [] )
    print 'data', ptn
    

    #ptn = execute(sid, 'res.partner','fields_get2', {'category_id': None, 'property_product_pricelist': None,  'industry_id': None} )
    #print 123123123, ptn

    #ptn = execute(sid, 'res.company','fields_get2' )
    #print 'company', ptn

    ptn = execute(sid, 'res.users','fields_get2', [] )
    print 'product', ptn

    ptn = execute(sid, 'res.users','search_read2', [], [] )
    print 'data', ptn

    ptn = execute(sid, 'res.users','fields_get2', [] )
    print 'product', ptn

    ptn = execute(sid, 'res.users','search_read2', [], [] )
    print 'data', ptn
    
    res.groups

    
    #url = HOST + '/web/session/modules'
    #ptn = jsonrpc(url,{},sid=sid )
    #print 'modules:',ptn
    
"""


    
