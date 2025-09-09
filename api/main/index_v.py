# coding:utf-8
__author__ = "ila"

from flask import jsonify, send_from_directory, current_app, request, abort
from . import main_bp
from utils.codes import *
import os

# 获取正确的模板路径
def get_templates_path():
    return os.path.join(os.path.dirname(current_app.instance_path), 'api', 'templates', 'front')

@main_bp.route('/', methods=['GET'])
def index():
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    return send_from_directory(front_dist, "index.html")

@main_bp.route('/admin', methods=['GET'])
def admin():
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    return send_from_directory(admin_dist, "index.html")

@main_bp.route('/admin/', methods=['GET'])
def admin_slash():
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    return send_from_directory(admin_dist, "index.html")

@main_bp.route('/admin/<path:filename>', methods=['GET'])
def admin_static(filename):
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    return send_from_directory(admin_dist, filename)

@main_bp.route('/favicon.ico', methods=['GET'])
def favicon():
    # 检查请求来源，优先返回管理端favicon
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        favicon_path = os.path.join(admin_dist, "favicon.ico")
        if os.path.exists(favicon_path):
            return send_from_directory(admin_dist, "favicon.ico")
    
    # 默认返回前端favicon
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    return send_from_directory(front_dist, "favicon.ico")

@main_bp.route('/css/<path:filename>', methods=['GET'])
def static_css(filename):
    # 检查请求来源，返回对应端的CSS文件
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        css_path = os.path.join(admin_dist, "css", filename)
        if os.path.exists(css_path):
            return send_from_directory(os.path.join(admin_dist, "css"), filename)
    
    # 默认返回前端CSS
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    css_path = os.path.join(front_dist, "css", filename)
    if os.path.exists(css_path):
        return send_from_directory(os.path.join(front_dist, "css"), filename)
    
    # 如果都找不到，尝试在管理端查找
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    css_path = os.path.join(admin_dist, "css", filename)
    if os.path.exists(css_path):
        return send_from_directory(os.path.join(admin_dist, "css"), filename)
    
    return abort(404)

@main_bp.route('/js/<path:filename>', methods=['GET'])
def admin_js(filename):
    # 检查请求来源，返回对应端的JS文件
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        js_path = os.path.join(admin_dist, "js", filename)
        if os.path.exists(js_path):
            return send_from_directory(os.path.join(admin_dist, "js"), filename)
    
    # 默认返回前端JS
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    js_path = os.path.join(front_dist, "js", filename)
    if os.path.exists(js_path):
        return send_from_directory(os.path.join(front_dist, "js"), filename)
    
    # 如果都找不到，尝试在管理端查找
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    js_path = os.path.join(admin_dist, "js", filename)
    if os.path.exists(js_path):
        return send_from_directory(os.path.join(admin_dist, "js"), filename)
    
    return abort(404)

@main_bp.route('/fonts/<path:filename>', methods=['GET'])
def admin_fonts(filename):
    # 检查请求来源，返回对应端的字体文件
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        fonts_path = os.path.join(admin_dist, "fonts", filename)
        if os.path.exists(fonts_path):
            return send_from_directory(os.path.join(admin_dist, "fonts"), filename)
    
    # 默认返回前端字体
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    fonts_path = os.path.join(front_dist, "fonts", filename)
    if os.path.exists(fonts_path):
        return send_from_directory(os.path.join(front_dist, "fonts"), filename)
    
    # 如果都找不到，尝试在管理端查找
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    fonts_path = os.path.join(admin_dist, "fonts", filename)
    if os.path.exists(fonts_path):
        return send_from_directory(os.path.join(admin_dist, "fonts"), filename)
    
    return abort(404)

@main_bp.route('/img/<path:filename>', methods=['GET'])
def admin_img(filename):
    # 检查请求来源，返回对应端的图片文件
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        img_path = os.path.join(admin_dist, "img", filename)
        if os.path.exists(img_path):
            return send_from_directory(os.path.join(admin_dist, "img"), filename)
    
    # 默认返回前端图片
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    img_path = os.path.join(front_dist, "img", filename)
    if os.path.exists(img_path):
        return send_from_directory(os.path.join(front_dist, "img"), filename)
    
    # 如果都找不到，尝试在管理端查找
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    img_path = os.path.join(admin_dist, "img", filename)
    if os.path.exists(img_path):
        return send_from_directory(os.path.join(admin_dist, "img"), filename)
    
    return abort(404)

@main_bp.route('/lunar/<path:filename>', methods=['GET'])
def lunar_static(filename):
    # 检查请求来源，返回对应端的农历文件
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        lunar_path = os.path.join(admin_dist, "lunar", filename)
        if os.path.exists(lunar_path):
            return send_from_directory(os.path.join(admin_dist, "lunar"), filename)
    
    # 默认返回前端农历文件
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    lunar_path = os.path.join(front_dist, "lunar", filename)
    if os.path.exists(lunar_path):
        return send_from_directory(os.path.join(front_dist, "lunar"), filename)
    
    # 如果都找不到，尝试在管理端查找
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    lunar_path = os.path.join(admin_dist, "lunar", filename)
    if os.path.exists(lunar_path):
        return send_from_directory(os.path.join(admin_dist, "lunar"), filename)
    
    return abort(404)

@main_bp.route('/verifys/<path:filename>', methods=['GET'])
def verifys_static(filename):
    # 检查请求来源，返回对应端的验证文件
    referer = request.headers.get('Referer', '')
    if '/admin' in referer:
        admin_dist = os.path.join(get_templates_path(), "admin", "dist")
        verifys_path = os.path.join(admin_dist, "verifys", filename)
        if os.path.exists(verifys_path):
            return send_from_directory(os.path.join(admin_dist, "verifys"), filename)
    
    # 默认返回前端验证文件
    front_dist = os.path.join(get_templates_path(), "front", "dist")
    verifys_path = os.path.join(front_dist, "verifys", filename)
    if os.path.exists(verifys_path):
        return send_from_directory(os.path.join(front_dist, "verifys"), filename)
    
    # 如果都找不到，尝试在管理端查找
    admin_dist = os.path.join(get_templates_path(), "admin", "dist")
    verifys_path = os.path.join(admin_dist, "verifys", filename)
    if os.path.exists(verifys_path):
        return send_from_directory(os.path.join(admin_dist, "verifys"), filename)
    
    return abort(404)