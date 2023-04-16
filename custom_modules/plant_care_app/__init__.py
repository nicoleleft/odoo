from . import models
from odoo import api

def _load_demo_data(cr, registry):
    env = api.Environment(cr, 1, {})
    demo_data_demo = env['users.demo']
    demo_data_demo.create_demo_data()

def post_init_hook(cr, registry):
    _load_demo_data(cr, registry)