from appConfigure import app
from routesVeg import index


app.add_url_rule('/', view_func=index.index)

app.add_url_rule('/create_vegetable',
                 view_func=index.createVegetable,
                 methods=['GET', 'POST']
                 )

app.add_url_rule('/vegetable/delete/<int:id>', view_func=index.deleteVegetable)
app.add_url_rule('/vegetable/edit/<int:id>',
                 view_func=index.editVegetable, methods=["GET", "POST"])

# @app.route('/')
# def index():

#     newVegetable = Vegetable('Potato', 123)
#     db.session.add(newVegetable)
#     db.session.commit()

#     # student1 = students("ahmad", "Gorakhpur", "jaddu pipra", "273301")

#     # db.session.add(student1)
#     # db.session.commit()

#     # print(student1)

#     return render_template('vegetables/index.html')


# @app.route('/all')
# def all():
#     vegetables =  Vegetable.query.all()
#     return render_template('vegetables/all_vegetables.html', students =vegetables)
