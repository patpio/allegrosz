from flask import Blueprint, render_template

from ..dbs.dbs import get_db

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/')
def index():
    conn = get_db()
    c = conn.cursor()

    c.execute('''SELECT
        i.id, i.title, i.description, i.price, i.image, c.name, s.name
        FROM
        item AS i
        INNER JOIN category AS c ON i.category_id = c.id
        INNER JOIN subcategory AS s ON i.subcategory_id = s.id
    ''')

    items_from_db = c.fetchall()

    items = []

    for row in items_from_db:
        item = {
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'price': row[3],
            'image': row[4],
            'category': row[5],
            'subcategory': row[6]
        }
        items.append(item)

    return render_template('index.html', items=items)
