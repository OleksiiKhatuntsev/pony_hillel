from pony.orm import db_session, select, left_join

from models import User, Role
from role_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        self.model = User

    @db_session
    def get_all_by_lambda(self):
        users = User.select(lambda role: role)
        return users.prefetch(Role).page(1).to_list()

    @db_session
    def get_users_oldest_than_age(self, age):
        users = User.select(lambda u: u.age > age)
        return users.page(1).to_list()

    @db_session
    def left_join(self):
        results = left_join((user, role) for user in User for role in user.role)
        for result in results:
            user = result[0]
            role = result[1]
            print(f"{user} |||| {role}")

if __name__ == '__main__':
    user_repo = UserRepository()
    res = user_repo.get_by_id(1)
    print(res)