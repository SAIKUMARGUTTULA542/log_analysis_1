#!/usr/bin/env python3
import psycopg2


def connect(dB_name="news"):
    # Connect or check database connection
    try:
        db = psycopg2.connect("dbname={}".format(dB_name))
        CurSor = db.cursor()
        return db, CurSor
    except Exception:
        print("Unable to connect to the database")

db, CurSor = connect()
q1 = ("create view query1view as select viewsforarticles.title, count(*)"
      "as viewcount from viewsforarticles join viewsforlog on "
      "viewsforlog.path group by viewsforarticles.title,"
      " viewsforlog.path order by viewcount desc")
# CurSor.execute(q1)
# db.commit()
q2 = ("create view query2view as select viewsforauthor.name, count(*) as "
      "ViewCount from viewsforarticles inner join viewsforauthor on"
      "viewsforarticles.id = viewsforauthor.id inner join viewsforlog on"
      "viewsforlog.path where group by viewsforauthor.name")
# CurSor.execute(q2)
# db.commit()
q3 = ("create view query3view as select day, perc from (select dy,"
      "round((sum(requests)/(select count(*) from viewsforlog where substring"
      "(to_char(viewsforlog.time,'Mon DDc,YYYY'), 0, 13) = day) * 100),2) as"
      "perc from (select substring(to_char(viewsforlog.time,'Mon DD,YYYY')"
      " , 0, 13)as day, count(*) as requests from viewsforlog where status"
      "like '%404%' group by day) as log_percentage group by day order by perc"
      " desc)as final_query")
# CurSor.execute(q3)
# db.commit()
# What are the most popular three articles of all time?
T1 = ("What are the most popular three articles of all time?")
Q1 = (
    "select title,viewcount from query1view order by viewcount desc fetch "
    "first 3 rows only")

# Who are the most popular article authors of all time?
T2 = ("Who are the most popular article authors of all time?")
Q2 = (
    "select name,ViewCount from query2view order by ViewCount desc")

# On which days did more than 1% of requests lead to errors
T3 = ("On which days did more than 1% of requests lead to errors?")
Q3 = (
    "select day,perc from query3view where perc >= 1")


def get_Results(q):
    # Return results
    db, CurSor = connect()
    CurSor.execute(q)
    return CurSor.fetchall()
    db.close()


def print_Results(qs):
    print(qs[1])
    for Index, Rs in enumerate(qs[0]):
        print(
            "\t" + str(Index+1) + "." + str(Rs[0]) +
            " - " + str(Rs[1]) + " viewcount")


def print_Error_Results(qs):
    print(qs[1])
    for rs in qs[0]:
        print("\t"+str(rs[0])+" - "+str(rs[1]) + "% errors")


if __name__ == '__main__':
    # get results
    query1 = get_Results(Q1), T1
    query2 = get_Results(Q2), T2
    query3 = get_Results(Q3), T3

    # print results
    print_Results(query1)
    print_Results(query2)
    print_Error_Results(query3)
