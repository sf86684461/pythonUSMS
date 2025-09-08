# coding:utf-8
__author__ = "ila"

import logging, os, json, configparser
import time
from datetime import datetime
from werkzeug.utils import redirect

from flask import request, jsonify,session
from sqlalchemy.sql import func,and_,or_,case
from sqlalchemy import cast, Integer,Float
from api.models.brush_model import *
from . import main_bp
from utils.codes import *
from utils.jwt_auth import Auth
from configs import configs
from utils.helper import *
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from utils.baidubce_api import BaiDuBce
from api.models.config_model import config






# 注册接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/register", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_register():
    if request.method == 'POST':
        msg = {'code': normal_code, 'message': 'success', 'data': [{}]}
        req_dict = session.get("req_dict")


        error = chaoshishangpin.createbyreq(chaoshishangpin, chaoshishangpin, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = "注册用户已存在"
        return jsonify(msg)

# 登录接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/login", methods=['GET','POST'])
def pythoncb7g1i62_chaoshishangpin_login():
    if request.method == 'GET' or request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        req_model = session.get("req_dict")
        try:
            del req_model['role']
        except:
            pass


        datas = chaoshishangpin.getbyparams(chaoshishangpin, chaoshishangpin, req_model)
        if not datas:
            msg['code'] = password_error_code
            msg['msg']='密码错误或用户不存在'
            return jsonify(msg)


        req_dict['id'] = datas[0].get('id')
        try:
            del req_dict['mima']
        except:
            pass


        return Auth.authenticate(Auth, chaoshishangpin, req_dict)


# 登出接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/logout", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_logout():
    if request.method == 'POST':
        msg = {
            "msg": "退出成功",
            "code": 0
        }
        req_dict = session.get("req_dict")

        return jsonify(msg)

# 重置密码接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/resetPass", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_resetpass():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success"}

        req_dict = session.get("req_dict")

        if req_dict.get('mima') != None:
            req_dict['mima'] = '123456'

        error = chaoshishangpin.updatebyparams(chaoshishangpin, chaoshishangpin, req_dict)

        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['msg'] = '密码已重置为：123456'
        return jsonify(msg)

# 获取会话信息接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/session", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_session():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "data": {}}
        req_dict={"id":session.get('params').get("id")}
        msg['data']  = chaoshishangpin.getbyparams(chaoshishangpin, chaoshishangpin, req_dict)[0]

        return jsonify(msg)

# 分类接口（后端）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/page", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_page():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")
        userinfo = session.get("params")

        try:
            __hasMessage__=chaoshishangpin.__hasMessage__
        except:
            __hasMessage__=None
        if __hasMessage__ and __hasMessage__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None and chaoshishangpin!='chat':
                req_dict["userid"]=session.get("params").get("id")

        tablename=session.get("tablename")
        if tablename=="users" :
            try:
                pass
            except:
                pass
        else:
            mapping_str_to_object = {}
            for model in Base_model._decl_class_registry.values():
                if hasattr(model, '__tablename__'):
                    mapping_str_to_object[model.__tablename__] = model

            try:
                __isAdmin__=mapping_str_to_object[tablename].__isAdmin__
            except:
                __isAdmin__=None
            try:
                __authSeparate__ =mapping_str_to_object[tablename].__authSeparate__
            except:
                __authSeparate__ = None

            if __isAdmin__!="是" and __authSeparate__ == "是" and session.get("params")!=None:
                req_dict["userid"]=session.get("params").get("id")
            else:
                try:
                    del req_dict["userid"]
                except:
                    pass

            # 当前表也是有管理员权限的表
            if  __isAdmin__ == "是" and 'chaoshishangpin' != 'forum':
                if req_dict.get("userid") and 'chaoshishangpin' != 'chat':
                    del req_dict["userid"]
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if tablename!="users" and 'chaoshishangpin'[:7]!='discuss'and "userid" in chaoshishangpin.getallcolumn(chaoshishangpin,chaoshishangpin):
                    req_dict["userid"] = session.get("params").get("id")



        clause_args = []
        or_clauses = or_(*clause_args)

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = chaoshishangpin.page(chaoshishangpin, chaoshishangpin, req_dict, or_clauses)

        return jsonify(msg)

# 排序接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/autoSort", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_autosort():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")
        req_dict['sort']='clicktime'
        req_dict['order']='desc'

        try:
            __browseClick__= chaoshishangpin.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ =='是':
            req_dict['sort']='clicknum'
        elif __browseClick__ =='时长':
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = chaoshishangpin.page(chaoshishangpin, chaoshishangpin, req_dict)

        return jsonify(msg)

#查询单条数据
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/query", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_query():
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{}}
        req_dict = session.get("req_dict")
        query = db.session.query(chaoshishangpin)
        for key, value in req_dict.items():
            query = query.filter(getattr(chaoshishangpin, key) == value)
        query_result = query.first()
        query_result.__dict__.pop('_sa_instance_state', None)
        msg['data'] = query_result.__dict__
        return jsonify(msg)

# 分页接口（前端）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/list", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_list():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']
            
        userinfo = session.get("params")

        try:
            __foreEndList__=chaoshishangpin.__foreEndList__
        except:
            __foreEndList__=None

        if __foreEndList__ and __foreEndList__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None:
                req_dict['userid']=session.get("params").get("id")

        try:
            __foreEndListAuth__=chaoshishangpin.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None:
                req_dict['userid']=session.get("params").get("id")

        tablename=session.get("tablename")
        if tablename=="users" :
            try:
                del req_dict["userid"]
            except:
                pass
        else:
            mapping_str_to_object = {}
            for model in Base_model._decl_class_registry.values():
                if hasattr(model, '__tablename__'):
                    mapping_str_to_object[model.__tablename__] = model

            try:
                __isAdmin__=mapping_str_to_object[tablename].__isAdmin__
            except:
                __isAdmin__=None

            if __isAdmin__!="是" and session.get("params")!=None:
                req_dict["userid"]=session.get("params").get("id")

        if 'luntan' in 'chaoshishangpin':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]


        if 'discuss' in 'chaoshishangpin':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = chaoshishangpin.page(chaoshishangpin, chaoshishangpin, req_dict)

        return jsonify(msg)

# 保存接口（后端）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/save", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_save():
    '''
    '''
    request.operation = "新增超市商品"
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        for key in req_dict:
            if req_dict[key] == '':
                req_dict[key] = None

        error= chaoshishangpin.createbyreq(chaoshishangpin, chaoshishangpin, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 添加接口（前端）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/add", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_add():
    '''
    '''
    request.operation = "新增超市商品"
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        try:
            __foreEndListAuth__=chaoshishangpin.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users":
                req_dict['userid']=session.get("params").get("id")

        error= chaoshishangpin.createbyreq(chaoshishangpin, chaoshishangpin, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 踩、赞接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/thumbsup/<id_>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_thumbsup(id_):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=chaoshishangpin.getbyid(chaoshishangpin, chaoshishangpin,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = chaoshishangpin.updatebyparams(chaoshishangpin, chaoshishangpin, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 获取详情信息（后端）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/info/<id_>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_info(id_):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data = chaoshishangpin.getbyid(chaoshishangpin, chaoshishangpin, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        #浏览点击次数
        try:
            __browseClick__= chaoshishangpin.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__  and  "clicknum"  in chaoshishangpin.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}
            ret=chaoshishangpin.updatebyparams(chaoshishangpin,chaoshishangpin,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 获取详情信息（前端）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/detail/<id_>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_detail(id_):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data = chaoshishangpin.getbyid(chaoshishangpin, chaoshishangpin, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        #浏览点击次数
        try:
            __browseClick__= chaoshishangpin.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ and "clicknum" in chaoshishangpin.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}
            ret=chaoshishangpin.updatebyparams(chaoshishangpin,chaoshishangpin,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 更新接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/update", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_update():
    '''
    '''
    request.operation = "更新超市商品"
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        if req_dict.get("mima") and "mima" not in chaoshishangpin.__table__.columns :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in chaoshishangpin.__table__.columns :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = chaoshishangpin.updatebyparams(chaoshishangpin, chaoshishangpin, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error


        return jsonify(msg)

# 删除接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/delete", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_delete():
    '''
    '''
    request.operation = "删除超市商品"
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")

        error=chaoshishangpin.delete(
            chaoshishangpin,
            req_dict
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 投票接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/vote/<int:id_>", methods=['POST'])
def pythoncb7g1i62_chaoshishangpin_vote(id_):
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success"}


        data= chaoshishangpin.getbyid(chaoshishangpin, chaoshishangpin, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=chaoshishangpin.updatebyparams(chaoshishangpin,chaoshishangpin,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return jsonify(msg)




# 分组统计接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/group/<columnName>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_group(columnName):
    '''
    分组统计接口
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        userinfo = session.get("params")


        msg['data'] = chaoshishangpin.groupbycolumnname(chaoshishangpin,chaoshishangpin,columnName,req_dict)
        msg['data'] = msg['data'][:10]
        msg['data'] = [ {**i,columnName:str(i[columnName])} if columnName in i else i for i in msg['data']]
        json_filename='chaoshishangpin'+f'_group_{columnName}.json'

        where = ' where 1 = 1 '
        sql = "SELECT COUNT(*) AS total, " + columnName + " FROM chaoshishangpin " + where + " GROUP BY " + columnName
        return jsonify(msg)

# 按值统计接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/value/<xColumnName>/<yColumnName>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_value(xColumnName, yColumnName):
    '''
    按值统计接口,
    {
        "code": 0,
        "data": [
            {
                "total": 10.0,
                "shangpinleibie": "aa"
            },
            {
                "total": 20.0,
                "shangpinleibie": "bb"
            },
            {
                "total": 15.0,
                "shangpinleibie": "cc"
            }
        ]
    }
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        userinfo = session.get("params")


        msg['data'] = chaoshishangpin.getvaluebyxycolumnname(chaoshishangpin,chaoshishangpin,xColumnName,yColumnName,req_dict)
        msg['data'] = msg['data'][:10]
        return jsonify(msg)

# 按日期统计接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/value/<xColumnName>/<yColumnName>/<timeStatType>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_value_riqi(xColumnName, yColumnName, timeStatType):
    '''
    按日期统计接口
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        userinfo = session.get("params")
        where = ' where 1 = 1 '
        sql = ''
        if timeStatType == '日':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM chaoshishangpin {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, yColumnName, where, '%Y-%m-%d')

        if timeStatType == '月':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM chaoshishangpin {2} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, yColumnName, where, '%Y-%m')

        if timeStatType == '年':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM chaoshishangpin {2} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, yColumnName, where, '%Y')

        data = db.session.execute(sql)
        data = data.fetchall()
        results = []
        for i in range(len(data)):
            result = {
                xColumnName: decimalEncoder(data[i][0]),
                'total': decimalEncoder(data[i][1])
            }
            results.append(result)
            
        msg['data'] = results
        json_filename='chaoshishangpin'+f'_value_{xColumnName}_{yColumnName}.json'

        return jsonify(msg)

# 按值统计（多）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/valueMul/<xColumnName>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_valueMul(xColumnName):

    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": []}

        req_dict = session.get("req_dict")
        userinfo = session.get("params")

        where = ' where 1 = 1 '

        for item in req_dict['yColumnNameMul'].split(','):
            sql = "SELECT {0}, sum({1}) AS total FROM chaoshishangpin {2} GROUP BY {0} LIMIT 10".format(xColumnName, item, where)
            L = []
            data = db.session.execute(sql)
            data = data.fetchall() 
            for i in range(len(data)):
                result = {
                    xColumnName: decimalEncoder(data[i][0]),
                    'total': decimalEncoder(data[i][1])
                }
                L.append(result)
            msg['data'].append(L)

        return jsonify(msg)

# 按值统计（多）
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/valueMul/<xColumnName>/<timeStatType>", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_valueMul_time(xColumnName,timeStatType):

    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": []}

        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        where = ' where 1 = 1 '

        for item in req_dict['yColumnNameMul'].split(','):
            sql = ''
            if timeStatType == '日':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM chaoshishangpin {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d') LIMIT 10".format(xColumnName, item, where, '%Y-%m-%d')

            if timeStatType == '月':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM chaoshishangpin {2} GROUP BY DATE_FORMAT({0}, '%Y-%m') LIMIT 10".format(xColumnName, item, where, '%Y-%m')

            if timeStatType == '年':
                sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM chaoshishangpin {2} GROUP BY DATE_FORMAT({0}, '%Y') LIMIT 10".format(xColumnName, item, where, '%Y')
            L = []
            data = db.session.execute(sql)
            data = data.fetchall() 
            for i in range(len(data)):
                result = {
                    xColumnName: decimalEncoder(data[i][0]),
                    'total': decimalEncoder(data[i][1])
                }
                L.append(result)
            msg['data'].append(L)

        return jsonify(msg)

# 推荐算法接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/autoSort2", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_autoSort2():
    if request.method == 'GET':

        leixing = set()
        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        sql = "select goodtype from orders where userid = "+str(userinfo.get("id"))+" and tablename = 'chaoshishangpin' order by addtime desc"
        try:
            data = db.session.execute(sql)
            rows = data.fetchall()
            for row in rows:
                for item in row:
                    if item != None:
                        leixing.add(item)
        except:
            leixing = set()

        L = []
        where = " AND ".join([f"{key} = '{value}'" for key, value in req_dict.items() if key!="page" and key!="limit" and key!="order"and key!="sort"])
        if where:
            sql = f'''SELECT * FROM (SELECT * FROM chaoshishangpin WHERE {where}) AS table1 WHERE shangpinfenlei IN ('{"','".join(leixing)}') union all SELECT * FROM (SELECT * FROM chaoshishangpin WHERE {where}) AS table1 WHERE shangpinfenlei NOT IN ('{"','".join(leixing)}')'''
        else:
            sql ="select * from chaoshishangpin where shangpinfenlei in ('%s"%("','").join(leixing)+"') union all select * from chaoshishangpin where shangpinfenlei not in('%s"%("','").join(leixing)+"')"
        data = db.session.execute(sql)
        data_dict = [dict(zip(result.keys(), result)) for result in data.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                elif 'datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)

        return jsonify({"code": 0, "msg": '',  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":5,"list": L[0:int(req_dict['limit'])]}})







# 统计接口
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/remind/<columnName>/<type>", methods=['GET'])  #
def pythoncb7g1i62_chaoshishangpin_remind(columnName,type):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, 'count': 0}
        # 组合查询参数
        params = session.get("req_dict")
        remindstart = 0
        remindend =9999990
        if int(type)==1:#数字
            if params.get('remindstart') == None and params.get('remindend') != None:
                remindstart = 0
                remindend = int(params['remindend'])
            elif params.get('remindstart') != None and params.get('remindend') == None:
                remindstart = int(params['remindstart'])
                remindend = 999999
            elif params.get('remindstart') == None and params.get('remindend') == None:
                remindstart = 0
                remindend = 999999
            else:
                remindstart = params.get('remindstart')
                remindend =  params.get('remindend')
        elif int(type)==2:#日期
            current_time=int(time.time())
            if params.get('remindstart') == None and params.get('remindend') != None:
                starttime=current_time-60*60*24*365*2
                params['remindstart'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
                endtime=current_time+60*60*24*params.get('remindend')
                params['remindend'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endtime))

            elif params.get('remindstart') != None and params.get('remindend') == None:
                starttime= current_time - 60 * 60 * 24 * params.get('remindstart')
                params['remindstart']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
                endtime=current_time+60*60*24*365*2
                params['remindend'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endtime))
            elif params.get('remindstart') == None and params.get('remindend') == None:
                starttime = current_time - 60 * 60 * 24 * 365 * 2
                params['remindstart'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * 365 * 2
                params['remindend'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endtime))

        data = chaoshishangpin.getbetweenparams(
            chaoshishangpin,
            chaoshishangpin,
            columnName,
            {
                "remindStart": remindstart,
                "remindEnd": remindend
            }
        )

        msg['count'] = len(data)
        return jsonify(msg)






#分类列表
@main_bp.route("/pythoncb7g1i62/chaoshishangpin/lists", methods=['GET'])
def pythoncb7g1i62_chaoshishangpin_lists():
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": []}
        list,_,_,_,_ = chaoshishangpin.page(chaoshishangpin,chaoshishangpin,{})
        msg['data'] = list
        return jsonify(msg)


