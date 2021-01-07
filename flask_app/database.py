from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ChineseWord(db.Model):
    word_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.VARCHAR(4), nullable=False)

    def __repr__(self):
        return '<Word ID %r: %r>' % (self.word_id, self.word)


def get_all_chinese_words():
    return ChineseWord.query.order_by(ChineseWord.word_id).all()
