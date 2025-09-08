# coding:utf-8
__author__ = "ila"

from flask import jsonify,send_from_directory
from . import main_bp
from utils.codes import *
from flask import send_from_directory
from . import main_bp

@main_bp.route('/', methods=['GET'])
def index():
    return send_from_directory("templates/front","index.html")

@main_bp.route('/admin', methods=['GET'])
def admin():
    return send_from_directory("templates/front/admin/dist","index.html")

# 新增：支持访问 /admin/（结尾斜杠），避免 404
@main_bp.route('/admin/', methods=['GET'])
def admin_slash():
    return send_from_directory("templates/front/admin/dist","index.html")

# 新增：补 favicon 路由，避免浏览器请求 /favicon.ico 时 404（不影响功能，但更干净）
@main_bp.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory("templates/front/admin/dist","favicon.ico")

@main_bp.route('/css/<css>', methods=['GET'])
def css(css):
    return send_from_directory("templates/front/admin/dist/css",css)

@main_bp.route('/js/<js>', methods=['GET'])
def admin_js(js):
    msg = {'code': normal_code, 'message': 'python项目运行成功，请运行前台和后台页面程序'}
    return send_from_directory("templates/front/admin/dist/js/",js)

@main_bp.route('/fonts/<fonts>', methods=['GET'])
def admin_fonts(fonts):
    msg = {'code': normal_code, 'message': 'python项目运行成功，请运行前台和后台页面程序'}
    return send_from_directory("templates/front/admin/dist/fonts/",fonts)

@main_bp.route('/img/<img>', methods=['GET'])
def admin_img(img):
    msg = {'code': normal_code, 'message': 'python项目运行成功，请运行前台和后台页面程序'}
    return send_from_directory("templates/front/admin/dist/img/",img)
