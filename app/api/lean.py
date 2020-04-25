# coding=utf-8
from . import api

@api.route("/")
def home():
  return "/api"

@api.route("/lean")
def lean():
  return "/lean"