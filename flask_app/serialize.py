from flask_marshmallow import Marshmallow

from flask_app.database import ChineseWord

ma = Marshmallow()


class ChineseWordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ChineseWord


chinese_word_schema = ChineseWordSchema()
chinse_words_list_schema = ChineseWordSchema(many=True)
