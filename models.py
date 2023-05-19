from pony.orm import Database, PrimaryKey, Optional, Required, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='admin', host='127.0.0.1', database='hillel_test_2')


class Role(db.Entity):
    _table_ = "roles"
    id = PrimaryKey(int, auto=True)
    title = Required(str, 50)
    users = Set("User")

    def __str__(self):
        return f"id = {self.id}; title = {self.title}"

    def __repr__(self):
        return f"id = {self.id}; title = {self.title}"


class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    email = Required(str, 50)
    password = Required(str, 20)
    age = Required(int)
    role = Required(Role, column="role_id")

    def __str__(self):
        return f"id = {self.id}; email = {self.email}"

    def __repr__(self):
        return f"{self.email} || {self.role.title}"


db.generate_mapping(create_tables=True)
