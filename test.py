import sqlite3

DATABASE = 'Cars.db'

def print_all_cars():
    speed = input('What speed: ')
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT car_name,top_speed FROM Car WHERE top_speed > ?;"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall()
        #print them nicely

        for Car in results:
            print(f"Car: {Car[0]} Top Speed: {Car[1]}")


if __name__ == "__main__":
   print_all_cars()