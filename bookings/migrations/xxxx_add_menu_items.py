from django.db import migrations

def add_menu_items(apps, schema_editor):
    Menu = apps.get_model('bookings', 'Menu')
    
    menu_data = [
        # Appetizers
        {
            'name': 'Samosa',
            'description': 'Crispy pastry filled with spiced potatoes and peas.',
            'price': 3.99,
            'category': 'APP'
        },
        {
            'name': 'Chicken Tikka',
            'description': 'Grilled chicken marinated in yogurt and spices.',
            'price': 6.99,
            'category': 'APP'
        },
        {
            'name': 'Falafel',
            'description': 'Deep-fried balls made from ground chickpeas and herbs.',
            'price': 4.99,
            'category': 'APP'
        },
        
        # Main Courses
        {
            'name': 'Chicken Biryani',
            'description': 'Fragrant rice cooked with tender chicken and aromatic spices.',
            'price': 12.99,
            'category': 'MAIN'
        },
        {
            'name': 'Beef Kebab Platter',
            'description': 'Grilled beef kebabs served with rice and salad.',
            'price': 14.99,
            'category': 'MAIN'
        },
        {
            'name': 'Vegetable Curry',
            'description': 'A mix of seasonal vegetables cooked in a rich, spiced gravy.',
            'price': 10.99,
            'category': 'MAIN'
        },
        {
            'name': 'Lamb Rogan Josh',
            'description': 'Tender lamb cooked in a flavorful tomato and onion gravy.',
            'price': 15.99,
            'category': 'MAIN'
        },
        
        # Desserts
        {
            'name': 'Baklava',
            'description': 'Layers of filo pastry filled with nuts and sweetened with syrup.',
            'price': 5.99,
            'category': 'DESS'
        },
        {
            'name': 'Gulab Jamun',
            'description': 'Soft, fried dough balls soaked in sugar syrup.',
            'price': 4.99,
            'category': 'DESS'
        },
        {
            'name': 'Kheer',
            'description': 'Creamy rice pudding flavored with cardamom and saffron.',
            'price': 4.99,
            'category': 'DESS'
        },
        
        # Beverages
        {
            'name': 'Mango Lassi',
            'description': 'A refreshing yogurt-based drink with mango pulp.',
            'price': 3.99,
            'category': 'BEV'
        },
        {
            'name': 'Mint Lemonade',
            'description': 'Fresh lemonade with a hint of mint.',
            'price': 2.99,
            'category': 'BEV'
        },
        {
            'name': 'Green Tea',
            'description': 'A soothing cup of green tea.',
            'price': 1.99,
            'category': 'BEV'
        }
    ]
    
    for item in menu_data:
        Menu.objects.create(**item)

class Migration(migrations.Migration):
    dependencies = [
        ('bookings', '0001_initial'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(add_menu_items),
    ]