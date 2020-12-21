from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, FloatField, TextAreaField, FileField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length


class ItemForm(FlaskForm):
    title = StringField('Title',
                        validators=[InputRequired('Input is required.'), DataRequired('Data is required.'),
                                    Length(min=5, max=20, message='Input must be between 5 and 20 characters long.')])
    price = FloatField('Price')
    description = TextAreaField('Description',
                                validators=[InputRequired('Input is required.'), DataRequired('Data is required.'),
                                            Length(min=5, max=40,
                                                   message='Input must be between 5 and 40 characters long.')])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], message='Images only')])


class NewItemForm(ItemForm):
    category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int)
    submit = SubmitField('Add')


class EditItemForm(ItemForm):
    submit = SubmitField('Update')


class DeleteItemForm(FlaskForm):
    price = FloatField('Price')
    submit = SubmitField('Delete')

    # TODO extra validators (in class)

    @staticmethod
    def validate_price(self, new_price):
        return False


class FilterForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=20, message='Less than 20')])
    description = StringField('Description', validators=[Length(max=40, message='Less than 40')])
    price = SelectField('Price', coerce=int, choices=[(0, '---'), (1, 'Max to min'), (2, 'Min to max')])
    category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int)
    cheap_items = BooleanField('Items up to 40 pln')
    submit = SubmitField('Filter')
