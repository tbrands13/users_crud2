from flask_app.config.mysqlconnection import connectToMySQL




class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_flask').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users


    @classmethod
    def got_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_flask').query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, occupation, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , %(occupation)s , NOW() , NOW());"
        return connectToMySQL('users_flask').query_db(query, data)

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, occupation, created_at, updated_at VALUES ( %(fname)s , %(lname)s , %(email)s , %(occupation)s , NOW() , NOW());"'
        results = connectToMySQL('users_flask').query_db(query, data)
        return results

    @classmethod
    def update_user(cls,data):
        query = 'UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, occupation = %(occupation)s, updated_at = NOW() WHERE id = %(id)s'
        results = connectToMySQL('users_flask').query_db(query, data)
        return results

    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        results = connectToMySQL('users_flask').query_db(query, data)
        return results