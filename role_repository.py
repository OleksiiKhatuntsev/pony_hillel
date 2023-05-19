from pony.orm import db_session, select
from models import Role


class BaseRepository:
    def __init__(self):
        self.model = None

    @db_session
    def get_by_id(self, id):
        entity = self.model.get(lambda r: r.id == id)
        return entity

    @db_session
    def delete_by_id(self, id):
        entity = self.get_by_id(id)
        entity.delete()
class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = Role

    # @db_session
    # def get_role_by_id(self, id):
    #     role = self.__model.get(lambda r: r.id == id)
    #     return role

    @db_session
    def get_all_by_lambda(self):
        roles = Role.select(lambda role: role)
        return roles.page(1).to_list()

    @db_session
    def update_title_by_id(self, id, new_title):
        role = self.get_role_by_id(id)
        role.title = new_title

    @db_session
    def delete_by_id(self, id):
        role_to_delete = self.get_role_by_id(id)
        role_to_delete.delete()

    @db_session
    def delete_by_id_range(self, id):
        roles = self.model.select(lambda r: r.id > id)
        for r in roles:
            r.delete()

    # @db_session
    # def get_all_by_sql(self):
    #     roles = self.__model.select_by_sql("SELECT * FROM roles")
    #     return roles

    @db_session
    def get_all_by_cycle(self):
        roles = select(role for role in self.model).page(1).to_list()
        return roles



    @db_session
    def add_role(self, title):
        self.model(title=title)

if __name__ == '__main__':
    role_repo = RoleRepository()
    result = role_repo.get_by_id(1)
    print(result)

