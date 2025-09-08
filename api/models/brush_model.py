# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuzhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    nianling=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='年龄' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    yonghushouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户手机' )
    money=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='余额' )

class yuangong(Base_model):
    __doc__ = u'''yuangong'''
    __tablename__ = 'yuangong'

    __loginUser__='yuangonggonghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yuangonggonghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='员工工号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    yuangongxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='员工姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    yuangongshouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='员工手机' )
    nianling=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='年龄' )
    ruzhishijian=db.Column( db.Date,  nullable=True, unique=False,comment='入职时间' )
    money=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='余额' )

class shangpinfenlei(Base_model):
    __doc__ = u'''shangpinfenlei'''
    __tablename__ = 'shangpinfenlei'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinfenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品分类' )
    image=db.Column( db.Text, nullable=False, unique=False,comment='图片' )

class chaoshishangpin(Base_model):
    __doc__ = u'''chaoshishangpin'''
    __tablename__ = 'chaoshishangpin'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinbianhao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='商品编号' )
    shangpinfenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品分类' )
    shangpinmingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    gongyingshang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='供应商' )
    shangpintupian=db.Column( db.Text,  nullable=True, unique=False,comment='商品图片' )
    onelimittimes=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='单限' )
    alllimittimes=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='库存' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    price=db.Column( db.Float,default=0, nullable=False, unique=False,comment='价格' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class shangpinjinhuo(Base_model):
    __doc__ = u'''shangpinjinhuo'''
    __tablename__ = 'shangpinjinhuo'



    __authTables__={'yuangonggonghao':'yuangong',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    rukudanhao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='入库单号' )
    shangpinmingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    shangpinfenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品分类' )
    alllimittimes=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='进货数量' )
    rukujiage=db.Column( db.Integer,default=0, nullable=False, unique=False,comment='入库价格' )
    rukuzongjia=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='入库总价' )
    gongyingshang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='供应商' )
    rukushijian=db.Column( db.Date,  nullable=True, unique=False,comment='入库时间' )
    yuangonggonghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='员工工号' )
    yuangongxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='员工姓名' )
    beizhu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class gongyingshang(Base_model):
    __doc__ = u'''gongyingshang'''
    __tablename__ = 'gongyingshang'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    gongyingshangbianhao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='供应商编号' )
    gongyingshangmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='供应商名称' )
    dizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地址' )
    lianxidianhua=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='联系电话' )
    fuzerenxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='负责人姓名' )
    lianxifangshi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='联系方式' )

class syslog(Base_model):
    __doc__ = u'''syslog'''
    __tablename__ = 'syslog'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    username=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户名' )
    operation=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户操作' )
    method=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='请求方法' )
    params=db.Column( db.Text,  nullable=True, unique=False,comment='请求参数' )
    time=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='请求时长(毫秒)' )
    ip=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='IP地址' )

class cart(Base_model):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品表名' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    goodid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='商品id' )
    goodname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    buynumber=db.Column( db.Integer,default=0, nullable=False, unique=False,comment='购买数量' )
    price=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='单价' )
    goodtype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品类型' )

class orders(Base_model):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    orderid=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='订单编号' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品表名' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    goodid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='商品id' )
    goodname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='商品图片' )
    buynumber=db.Column( db.Integer,default=0, nullable=False, unique=False,comment='购买数量' )
    price=db.Column( db.Float,default=0, nullable=False, unique=False,comment='价格' )
    total=db.Column( db.Float,default=0, nullable=False, unique=False,comment='总价格' )
    type=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='支付类型' )
    status=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='状态' )
    address=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地址' )
    tel=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='电话' )
    consignee=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='收货人' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )
    goodtype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品类型' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )
    role=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户角色' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class friendlink(Base_model):
    __doc__ = u'''friendlink'''
    __tablename__ = 'friendlink'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    url=db.Column( db.Text,  nullable=True, unique=False,comment='链接' )

class discusschaoshishangpin(Base_model):
    __doc__ = u'''discusschaoshishangpin'''
    __tablename__ = 'discusschaoshishangpin'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

