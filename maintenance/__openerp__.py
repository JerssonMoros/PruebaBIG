# -*- coding: utf-8 -*-

{
	'name': 'Maintenance',
	'description': 'This module will help manage asset maintenance',
	'version': '1.0',
	'author': 'Jersson Garzon',
	'sequence': 110,
	'depends': [
		'base', 'mail', 'board', 'hr'
	],
    'data': [
	    'maintenance_view.xml'
	],
	'instalable': True,
	"application": True,
	"auto_install": False
}
