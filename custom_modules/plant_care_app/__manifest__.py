{
    'name': 'Plant Care App',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Plant watering schedule tracker',
    'sequence': -50,
    'description': """This application is a watering schedule and fertilizer schedule tracking module used to notify users of when they should be watering and feeding their plants""",
    'author': 'Nicole W',
    'installable': True,
    'application': True,
    'data': [
                "views/plant.xml",
                "views/user_template.xml",
                "views/users.xml",
                "security/plant_security.xml",
                "security/ir.model.access.csv"
            ],

    'demo': [
                "data/demo_data.xml"
            ]
}
