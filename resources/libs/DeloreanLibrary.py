import psycopg2
from logging import info

class DeloreanLibrary():

    def connect(self):
        return psycopg2.connect(
            host='ec2-3-234-85-177.compute-1.amazonaws.com',
            database='d7lvcfh7tv8hts',
            user='kspvidrcffyoll',
            password='b1f5878c3d2b52ce198f7a7fc51ac6fab29d4457c614f587ec9132f3a8e83f9e'
        )
        
    # No Robot vira uma KW automágicamente => Remove Student     email@dejado.com
    def remove_student(self, email):

        query = "delete from students where email = '{}'".format(email)
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

    def remove_student_by_name(self, name):

        query = "delete from students where name LIKE '%{}%'".format(name)
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

    def insert_student(self, student):

        self.remove_student(student['email'])

        query = ("insert into students (name, email, age, weight, feet_tall,created_at,updated_at)"
                "values('{}','{}',{},{},{},NOW(),NOW());"
                .format(student['name'], student['email'], student['age'], student['weight'], student['feet_tall']))
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()
            
