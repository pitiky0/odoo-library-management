{
    'name': 'Library Management',
    'summary': 'Manage books, authors, and members',
    'description': """
        Module for managing a library:
        - Books Management
        - Authors Management
        - Member details in Contacts
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'category': 'Tools',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/library_security.xml',    # 1. تعريف المجموعات
        'security/ir.model.access.csv',     # 2. حقوق الوصول
        'data/library_cron.xml',            # 3. تعريف الـ Cron Job

        # 👇 الويزارد خاصو يتشارجا هو الأول حيت الكتب كيحتاجوه
        'wizard/library_rent_wizard_views.xml',

        'views/library_book_views.xml',     # 3. واجهة الكتب
        'views/library_author_views.xml',   # 4. واجهة الكتاب
        'views/res_partner_views.xml',      # 5. واجهة الأعضاء (Inheritance)
        'report/library_book_report.xml',   # 6. تقرير الكتب
        'views/library_dashboard_views.xml',# 7. واجهة لوحة القيادة
    ],

    # 👇 القسم الجديد الخاص بـ JS/XML
    'assets': {
        'web.assets_backend': [
            'library_app/static/src/components/star_rating/star_rating.xml',
            'library_app/static/src/components/star_rating/star_rating.js',
        ],
    },

    'installable': True,
    'application': True,
}