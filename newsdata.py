#!/usr/bin/python 3.6
import psycopg2

# The code forthe code for creating the views is saved in view.txt file.
db = psycopg2.connect("dbname=news")
c = db.cursor()


def print_menu():  # Your menu design here
    print 30 * "-", "MENU", 30 * "-"
    print "1.What are the most popular three articles of all time?"
    print "2.Who are the most popular article authors of all time?"
    print "3.On which days did more than 1% of requests lead to errors?"
    print "4.exit"
    print 67 * "-"


loop = True

while loop:  # While loop which will keep going until loop = False
    print_menu()  # Displays menu
    choice = input("Enter your choice [1-4]: ")
    if choice == 1:
        print "Menu 1 has been selected"
        query = ("select title"
                 ",hits from auth_slug_hit"
                 " order by hits desc limit 3;")
        c.execute(query)
        rows = c.fetchall()
        for (slughit, hits) in rows:
            print("{}----{}".format(slughit, hits))

    elif choice == 2:
        print "Menu 2 has been selected"
        # You can add your code or functions here
        query = ("select name, sum(hits) from authors"
                 ",auth_slug_hit where authors.id = auth_slug_hit.author"
                 " group by name"
                 " order by sum(hits) desc;")
        c.execute(query)
        rows = c.fetchall()
        for (name, hits) in rows:
            print("{}----{}".format(name, hits))
    elif (choice == 3):
        print "Menu 3 has been selected"
        # You can add your code or functions here
        query = ("select all_views.date as Days"
                 ",round(100.0*error_table.error_hits / all_views.views,2)"
                 " as percentage_error from error_table"
                 ",all_views where all_views.date = error_table.date"
                 " and round(100.0*error_table.error_hits / all_views.views,2)"
                 ">1.0;")
        c.execute(query)
        rows = c.fetchall()
        for (Days, percentage) in rows:
            print("{}----{}".format(Days, percentage))
    elif(choice == 4):
        db.close()
        print "Database connection has terminated"
        loop = False
