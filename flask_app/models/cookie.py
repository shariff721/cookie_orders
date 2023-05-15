from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie:
    db = "cookie_orders"

    def __init__(self,data):
        self.id = data["id"]
        self.customer_name = data["customer_name"]
        self.cookie_type = data["cookie_type"]
        self.number_of_boxes = data["number_of_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def add_order(cls,data):
        query = """
            INSERT INTO cookies
            (customer_name, cookie_type, number_of_boxes)
            VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)
    

    @classmethod
    def update_order(cls,data):
        query = """
            UPDATE cookies
            SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def get_all_orders(cls):
        query = """
            SELECT * FROM cookies;
        """
        all_cookies = []
        results = connectToMySQL(cls.db).query_db(query)
        for one_order in results:
            all_cookies.append(cls(one_order))
        return all_cookies
    
    @classmethod
    def get_one_order(cls,data):
        query = """
            SELECT * FROM cookies WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])
    
    @staticmethod
    def validate_cookie(cookie):
        is_valid = True
        if len(cookie['customer_name']) < 2:
            flash("Customer Name must be atleast 2 characters.")
            is_valid = False
        if len(cookie['cookie_type']) < 2:
            flash("Cookie type must be atleast 2 characters.")
            is_valid = False
        if len(cookie['number_of_boxes']) == 0:
            flash("Number of boxes is required")
            is_valid = False
        elif int(cookie['number_of_boxes']) <= 0:
            flash("Number of boxes has to be a positive number")
            is_valid = False
        return is_valid


