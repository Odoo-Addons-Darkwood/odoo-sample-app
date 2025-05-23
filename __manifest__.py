{
    "name": "Tutorial Application",
    "summary": "Tutorial of VyNT",
    "description": """
    ====================
    Long description
    *hello*
    **world**

    Bullet Hell:
    - 1
    - 2
    - 3
    ====================
    """,
    "author": "Nguyen The Vy",
    "website": "https://github.com/vyngt/odoo-sample-app",
    "category": "Services/Library",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/tutorial_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/menu.xml",
        "views/book_list_template.xml",
        "reports/tutorial_library_book_report.xml",
        "reports/library_publisher_report.xml",
    ],
    "application": True,
    "demo": [
        "data/res.partner.csv",
        "data/tutorial.library.book.csv",
        "data/book_demo.xml",
    ],
}
