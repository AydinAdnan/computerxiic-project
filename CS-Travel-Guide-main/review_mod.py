"""M"""
import os
import sys
import random


def Wiki():  # Add wikipedia to Python path
    path = os.getcwd()
    wiki_path = path + r"\Wikipediam"
    sys.path.append(wiki_path)


Wiki()
import wikipedia

def welcome():  # welcome message
    print("\t\t\t\tWELCOME! \n\nThis program has been designed to help you find information regarding places in Kerala.We hope this will be of help to you in finding what you are looking for!\t\t\t\t\n")


def info(conn, infoplace):   # Show Reviews
    result = wikipedia.summary(infoplace, sentences=5)
    print(result)
    p_wiki = result.split()[0]
    status(conn, infoplace, p_wiki)
    print("\nReviews:")
    show_reviews_info(conn, infoplace, p_wiki)
    ch = input("Do you want to add review?(y/n): ")
    if ch.lower() == "y":
        create(conn, infoplace)
    print()


def attrofday(conn):
    curs = conn.cursor()
    query = 'SELECT DISTINCT Place FROM reviews'
    curs.execute(query)
    placesl = curs.fetchall()
    places = []
    for i in placesl:
        places.append(i[0])
    attraction = random.choice(places)
    info(conn, attraction)
    curs.close()


def create(conn, place):  # for writing reviews
    f = 2
    curs = conn.cursor()
    while f != 1:
        m = input('Write your review here: ')
        ctad = input("Current restrictions(Skip if not available): ")
        name = input("Enter Your name: ")
        curs.execute("SELECT max(rev_id) FROM Reviews")
        n = curs.fetchone()[0]
        print("Reference id for editing or deleting your review is: ", n + 1)
        t = (n + 1, name, place, m, ctad)
        s = 'insert into Reviews(rev_id,usr_name,Place,Reviews,trvl_avl) values(%s,%s,%s,%s,%s)'
        curs.execute(s, t)
        conn.commit()
        f = int(input('Enter zero to quit '))
        f = f + 1
    curs.close()


# for displaying reviews along with places
def show_reviews_info(conn, place, pl_wiki):
    curs = conn.cursor()
    curs.execute(
        "SELECT usr_name,REVIEWS,revdate,trvl_avl FROM Reviews WHERE Place in (%s,%s)", (place, pl_wiki))
    rev = curs.fetchall()
    if rev:
        for i in rev:
            print(i[0], '  ', i[2], '\n', i[1])
    else:
        print("No Reviews were Found.")
    print()
    curs.close()


def edit(conn):  # for editing reviews previously entered
    curs = conn.cursor()
    a = int(input("Enter Review Id for the review you would like to edit: "))
    show_reviews(conn, a, 'edit')
    b = input("Enter new review: ")
    ctad = input("Current restrictions(Skip if not available): ")
    s = ("Update Reviews set Reviews=%s, trvl_avl=%s where rev_id=%s")
    curs.execute(s, (b, ctad, a))
    if curs.rowcount == 0:
        print("The reference id entered does not exist.Enter a valid id")
    else:
        print("Review has been updated")
    conn.commit()
    curs.close()


def delete(conn):  # for deleting reviews previously entered
    curs = conn.cursor()
    d = int(input("Enter the reference id for the review you would like to delete: "))
    s = ('Delete from Reviews where rev_id=%s')
    curs.execute(s, (d,))
    if curs.rowcount == 0:
        print("The reference id entered does not exist.Enter a valid id.")
    else:
        print("Review has been deleted")
    conn.commit()
    curs.close()


def status(conn, pl, plw):  # show status of a place if available
    curs = conn.cursor()
    curs.execute("SELECT trvl_avl,rev_id,usr_name,revdate FROM Reviews WHERE Place=%s or Place=%s GROUP BY revdate HAVING revdate=max(revdate);", (pl, plw))
    l = curs.fetchall()
    if l:
        sta = l[0][0]
        date = l[0][3]
        name = l[0][2]
        if sta != "Data not available":
            print("Current Status ( last updated on", date, 'by', name, ') :', sta)
        else:
            print("Current Status: (Please add through reviews)")
    else:
        print("Current Status: (Please add through reviews)")
    curs.close()


def show_reviews(conn, id, f="d"):  # show reviews according to revid
    curso = conn.cursor()
    curso.execute("SELECT Reviews,Place FROM Reviews WHERE rev_id=%s", (id,))
    r = curso.fetchone()
    place, rev = r[1], r[0]
    if r != None:
        if f == 'edit':  # show reviews in edit op
            print("Old review of", place, ":", rev)
        elif f == 'd':  # show reviews according to id
            print("Your review of", place, ":", rev)
    else:
        if f == 'd':
            print("Review id doesn't exist")
    curso.close()
