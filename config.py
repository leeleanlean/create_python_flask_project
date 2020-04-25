# coding=utf-8

"""配置信息"""
class Config(object):
 pass

"""开发环境配置信息"""
class DevelopConfig(Config):
  DEBUG = True

  # redis
  REDIS_HOST = ''
  REDIS_PORT = ''

"""生产环境配置信息"""
class ProductConfig(Config):
  # redis
  REDIS_HOST = ''
  REDIS_PORT = ''

config_map = {
  "develop": DevelopConfig,
  "product": ProductConfig
}