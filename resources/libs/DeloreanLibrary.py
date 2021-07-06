import psycopg2
from logging import info

class DeloreanLibrary():

    def connect(self):
        return psycopg2.connect(
            host='ec2-52-7-115-250.compute-1.amazonaws.com',
            database='d8rvaccp6aaf5v',
            user='fylrfbtcrrunbh',
            password='e1ce1f5ae449b4c613a1b93421a038d25bef37b6021638beb9f4b88196945058'
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
            
