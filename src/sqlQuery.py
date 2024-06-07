from src.database import mysql


class MySqlQuery:
    def __init__(self) -> object:
        pass

    def emailCheck(self, sDict):
        q = f"SELECT name FROM users WHERE email = '{sDict['checkValue']}'"
        try:
            cur = mysql.connection.cursor()
            cur.execute(q)
            fetchData = cur.fetchall()
            cur.close()
            if fetchData:
                return 1
            else:
                return 0
        except Exception as e:
            return e

    def registerUser(self, iDict):
        qu = 'INSERT INTO users(email, password, name, createdon) VALUES (%(email)s, %(password)s, %(name)s,  %(createon)s)'
        try:
            cur = mysql.connection.cursor()
            cur.execute(qu, iDict['insertVal'])
            mysql.connection.commit()
            return cur.lastrowid
        except Exception as e:
            return e

    def selQuery(self, sDict):
        if sDict['type'] == 'email_check':
            return self.emailCheck(sDict)
        if sDict['type'] == 'register':
            return self.registerUser(sDict)
