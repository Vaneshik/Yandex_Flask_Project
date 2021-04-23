import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


association_table = sqlalchemy.Table(
    'products_to_users',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('products', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('products.id'))
)


class Product(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    pics = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    amount = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    categories = orm.relation("Category",
                              secondary="categories_to_products",
                              backref="categories")

    products = orm.relation("User",
                            secondary="products_to_users",
                            backref="users")