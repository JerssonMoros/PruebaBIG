from openerp.osv import fields, osv

class maintenance_asset_type(osv.Model):

	_name = 'maintenance.asset.type'
	_columns = {
		'name': fields.char('Name', required = True)
	}

maintenance_asset_type()

class maintenance_asset(osv.Model):

    _name = 'maintenance.asset'
    _columns = {
        'asset_name' : fields.char('name', size=40, required=True, help='Name of asset'),
        'asset_type_id': fields.many2one('maintenance.asset.type', 'Type'),
        'serial_number': fields.char('Serial Number', size=32, required=True, help='Serial Number of this asset'),
        'employee_id': fields.many2one('hr.employee', 'Employee', help='Employee who has this machine'),
        'acquisition_date': fields.date('Acquisition Date', help='Date when the asset has been bought'),
        'location': fields.char('Location', size=128, help='Location of the asset'),
        'value': fields.float('asset Value', help='Value of the bought asset'),
        'order_ids': fields.one2many('maintenance.order', 'asset_id', 'Order'),
    }
    _rec_name = 'asset_name'

maintenance_asset()

class maintenance_service_type(osv.Model):
    _name = 'maintenance.service.type'
    _columns = {
        'name': fields.char('Name', required=True),
    }

maintenance_service_type()

class maintenance_service(osv.Model):
    _name = 'maintenance.service'
    _columns = { 
        'order_id' : fields.many2one('maintenance.order', 'Order', required = True),
        'technical_id' : fields.many2one('maintenance.technical', 'Technical', required=True),
        'service_type_id': fields.many2one('maintenance.service.type', 'Type', required = True),
        'finish_date': fields.date('Finish Date'),
        'notes': fields.text('Notes'),
    }
    _rec_name = 'order_id'
maintenance_service()

class maintenance_order(osv.Model):
    _name = 'maintenance.order'
    _columns = {
        'order_number' : fields.integer('Order Number'),
        'applicant_id' : fields.many2one('hr.employee', 'Applicant'),
        'beneficiary_id' : fields.many2one('hr.department', 'Beneficiary'),
        'description' : fields.text('Description'),
        'asset_id' : fields.many2one('maintenance.asset', 'Asset'),
        'employee_id' : fields.many2one('hr.employee', 'Assigned Employee'),
        'start_date': fields.date('Start Date', required = True),
        'finish_date': fields.date('Finish Date', required = False),
        'service_ids': fields.one2many('maintenance.service','order_id','Services')
    }
    _defaults = {
        'start_date': fields.date.context_today,
    }
    _rec_name = 'order_number'

maintenance_order()

class maintenance_technical_type(osv.Model):
    _name = 'maintenance.technical.type'
    _columns = {
        'name' : fields.char('Name', required = True, help='technician performance area')
    }

maintenance_technical_type()

class maintenance_technical(osv.Model):
    _name = 'maintenance.technical'
    _columns = {
        'description': fields.text('Description'),
        'employee_id': fields.many2one('hr.employee', 'Employee', help='Employee who has this machine', required="True"),
        'service_ids': fields.one2many('maintenance.service','technical_id','Services'),
        'technical_type_id': fields.many2one('maintenance.technical.type', 'Type Technical', required=True)
    }
    _rec_name = 'employee_id'

