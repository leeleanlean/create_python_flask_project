# coding=utf-8
from app import create_app

# 创建flask应用
app = create_app('develop')

if __name__ == '__main__':
  app.run()