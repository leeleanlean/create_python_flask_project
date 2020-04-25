# coding=utf-8
from flask import Flask
import redis

from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

from config import config_map

from .api import *

# 数据库
# db = SQLAlchemy()

# 创建redis连接对象
redis_store = None

def create_app(env):
  """
  创建flask应用
  :param env[str] 配置环境变量(develop | product)
  :return:
  """
  app = Flask(__name__)

  # 配置参数
  config_class = config_map[env]
  app.config.from_object(config_class)

  # 初始化db
  # db.init_app(app)

  # 初始化redis工具
  global redis_store
  redis_store = redis.StrictRedis(host = config_class.REDIS_HOST, port = config_class.REDIS_PORT)

  # Session
  Session(app)

  # CSRF防护
  CSRFProtect(app)

  # 注册蓝图
  app.register_blueprint(api, url_prefix="/api")

  return app