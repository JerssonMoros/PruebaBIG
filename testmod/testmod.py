from openerp.osv import fields, osv

class testmod_test(osv.Model):
    _name = 'testmod.test'
    _columns = {
    'test1': fields.char('Test 1', size=32, required=True),
    'test2': fields.float('Test 2'),
    }

testmod_test()