import time
import os
import sys
import webbrowser
import mysql.connector as mysql


def Wiki():
    """Add wikipedia module and pwinput module file to Python path"""
    path = os.getcwd()
    wiki_path = path + r"\Wikipediam"
    pw_path = path + r"\pwinput"
    sys.path.append(wiki_path)
    sys.path.append(pw_path)


try:
    import wikipedia
    import pwinput
except ImportError:
    Wiki()  # option to add file to path
    import wikipedia
    import pwinput


def welcome():  # welcome message
    print("\t\t\t\tWELCOME! \n")
    print("\nThis program has been designed to help you find information regarding places in Kerala.", end="")
    print("We hope this will be of help to you in finding what you are looking for!\t\t\t\t\n")


def connectdb():
    usr = input("Enter Username: ")
    psw = pwinput.pwinput("Enter Password: ")
    con = mysql.connect(host='localhost', user=usr, passwd=psw)
    curs = con.cursor()
    create_dbase(curs)
    print("\nMySQL connection established ✅")
    return con


def create_dbase(curs):  # creating database
    curs.execute(
        "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Review') AND (TABLE_NAME = 'Reviews')")
    c = curs.fetchone()[0]
    if c == 0:
        curs.execute("Create Database Review")
        curs.execute("Use Review")
        path = os.getcwd().replace('\\', '/') + "/review_reviews.sql"
        create_rev(path, curs)
    else:
        curs.execute("Use Review")


def create_rev(fname, curso):  # creating database from dump file
    fd = open(fname, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                curso.execute(command)
        except IOError as msg:
            print("Command skipped: ", msg)


def info():
    infoplace = input("Enter the place you would like to know about : ")
    result = wikipedia.summary(infoplace, sentences=5)
    print(result)
    p_wiki = result.split()[0]
    status(con, infoplace, p_wiki)
    print("\nReviews:")
    show_reviews_info(con, infoplace, p_wiki)
    ch = input("Do you want to add review?(y/n): ")
    if ch.lower() == "y":
        create(con, infoplace)
    print()


# for displaying reviews along with places
def show_reviews_info(conn, place, pl_wiki):
    curs = conn.cursor()
    curs.execute("SELECT usr_name,REVIEWS,revdate,trvl_avl FROM Reviews WHERE Place in (%s,%s)", (place, pl_wiki))
    rev = curs.fetchall()
    if rev:
        for i in rev:
            print(i[0], '  ', i[2], '\n', i[1])
    else:
        print("No Reviews were Found.")
    print()
    curs.close()


def status(conn, pl, plw):  # show status of a place if available
    curs = conn.cursor()
    curs.execute("SELECT trvl_avl,rev_id,usr_name,revdate FROM Reviews WHERE Place=%s or Place=%s GROUP BY revdate HAVING revdate=max(revdate);", (pl, plw))
    status_data = curs.fetchall()
    if status_data:
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


def yatra():
    place = input("\nEnter Destination : ")
    adults = int(input("Enter total number of Adults : "))
    children = int(input("Enter total number of children : "))
    yatra = ("https://www.yatra.com/pwa/hotels/srp?roomRequests[0].id=1&roomRequests[0].noOfAdults={}&roomRequests[0].noOfChildren={}&source=BOOKING_ENGINE&pg=1&tenant=B2C&isPersnldSrp=1&city.name={}&city.code={}&state.name=KER&state.code=KER&country.name=India&country.code=IND".format(
        adults, children, place, place))
    print("You are being redirected")
    webbrowser.open(yatra, new=1)


def easemytrip():
    destination = input("Enter your Destination : ")
    checkin = input("Enter Check-in date in format DD/MM/YYYY : ")
    checkout = input("Enter Check-out date in format DD/MM/YYYY : ")
    pax = input("Enter number of adults : ")
    rooms = input("Enter number of rooms required : ")
    easemytrip = ("https://hotels.easemytrip.com/newhotel/Hotel/HotelListing?e=202193214436&city={},%20India&cin={}&cOut={}&Hotel=NA&Rooms={}&pax={}".format(
        destination, checkin, checkout, rooms, pax))
    print("You are being redirected")
    webbrowser.open(easemytrip, new=1)


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


def show_reviews(conn, id, f="d"):  # show reviews according to revid
    curso = conn.cursor()
    curso.execute("SELECT Reviews,Place FROM Reviews WHERE rev_id=%s", (id,))
    r = curso.fetchone()
    place, rev = r[1], r[0]
    if r:
        if f == 'edit':  # show reviews in edit op
            print("Old review of", place, ":", rev)
        elif f == 'd':  # show reviews according to id
            print("Your review of", place, ":", rev)
    else:
        if f == 'd':
            print("Review id doesn't exist")
    curso.close()


welcome()

print("Please Enter your Mysql Credintials to continue:")

while True:
    try:
        con = connectdb()
        break
    except Exception as e:
        print(e)
        print("Something went wrong.Please try again.\n")

os.system("cls")

while True:
    print('\n\t\tMain Menu\n\nChoose an option from the below listed : \n\n 1. Information of place ')
    print(' 2. Hotel bookings \n 3. Reviews \n 4. Exit ')
    q = input("\n\nYour choice (1,2,3,4) : ")

    if q == '1':
        try:
            info()
        except:
            print("Please check your input!")
        time.sleep(0.5)

    elif q == '2':
        print("\n\nEnter the website you would like to do your hotel booking in : \n 1. Yatra\n 2. Easemytrip\n 3. Exit \n\n")
        while True:
            choice = input("Your response :")
            
            if choice == "1":
                yatra()
                break
            
            elif choice == "2":
                easemytrip()
                break
            
            elif choice == "3":
                break
            
            else:
                print("Sorry , please enter a valid option")
                time.sleep(0.5)

    elif q == '3':
        while True:
            print("\n\nEnter a : To write review \nEnter b : To edit a review ")
            print(
                "Enter c : To delete a review \nEnter d : To view previous reviews \nEnter e : Exit this option")
            op4 = input("\n\nYour choice (a,b,c,d,e) : ")
            
            if op4.lower() == 'a':
                p = input("Enter the Place: ")
                create(con, p)
                op3 = 0
            
            elif op4.lower() == "b":
                edit(con)
                op3 = 0
            
            elif op4.lower() == "c":
                delete(con)
                op3 = 0
            
            elif op4.lower() == "d":
                id = int(input("Enter the reference id: "))
                show_reviews(con, id)
                time.sleep(1)
                op3 = 0
            
            elif op4.lower() == 'e':
                break
            
            else:
                print("Kindly enter a valid option")
                time.sleep(0.5)
        
        time.sleep(0.7)

    elif q == '4':
        break

    else:
        print("Please enter a valid choice.")

con.close()

print("Thank you for using our service")

time.sleep(1.5)
