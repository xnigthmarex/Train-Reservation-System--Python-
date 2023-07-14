import pymysql

# Establish connection
cnx = pymysql.connect(
    host='localhost',
    user='root',
    password='aryan2703',
    database='traindata_db'
)
cursor = cnx.cursor()


def user():
    def SignIn():
        # Sign in a user by checking username and password
        print("Enter username:")
        username = input("> ")
        print("Enter password:")
        userpassword = input("> ")

        select_query = "SELECT * FROM user WHERE username = %s AND password = %s"
        user_data = (username, userpassword)

        cursor.execute(select_query, user_data)
        result = cursor.fetchone()

        if result is not None:
            print("User signed in successfully!")
        else:
            print("Invalid username or password.")

    def SignUp():
        # Create a new user
        print("Enter username:")
        username = input("> ")
        print("Enter password:")
        userpassword = input("> ")

        select_query = "SELECT * FROM user WHERE username = %s"
        user_data = (username,)

        cursor.execute(select_query, user_data)
        result = cursor.fetchone()

        if result is None:
            create_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
            user_data = (username, userpassword)

            cursor.execute(create_query, user_data)
            cnx.commit()

            print("User created successfully!")
        else:
            print("Username already exists. Please choose a different username.")

    while True:
        print("Type 1 - SignIn")
        print("Type 2 - SignUp")
        print("Type 0 - Go Back")

        userinput = int(input("> "))

        if userinput == 1:
            SignIn()
        elif userinput == 2:
            SignUp()
        elif userinput == 0:
            break
        else:
            print("Invalid input. Please try again.")


def admin():
    def create_train():
        # Create a new train
        print("Enter Train Name:")
        trainname = input("> ")
        print("Create Starting Station")
        starting_station_id = create_station()
        print("Create Ending Station")
        ending_station_id = create_station()
        print("Creating train...")
        create_train_query = "INSERT INTO train (train_name,source_station_id,destination_station_id) VALUES (%s,%s,%s)"
        train_data = (trainname,starting_station_id,ending_station_id)

        try:
            cursor.execute(create_train_query, train_data)
            cnx.commit()
            train_id = cursor.lastrowid  # Retrieve the last inserted train ID
            print("Train created successfully!")
            return train_id
        except pymysql.Error as error:
            print("Error creating train:", error)

    def create_station():
        # Create a new station
        print("Enter Station Name:")
        stationname = input("> ")
        print("Enter Station Location:")
        stationlocation = input("> ")
        print("Creating station...")
        create_station_query = "INSERT INTO stations (station_name, location) VALUES (%s, %s)"
        station_data = (stationname, stationlocation)

        try:
            cursor.execute(create_station_query, station_data)
            cnx.commit()
            station_id = cursor.lastrowid 
            print("Station created successfully!")
            return station_id
        except pymysql.Error as error:
            print("Error creating station:", error)

    def create_coach(train_id):
        # Create a new coach
        print("Enter Coach Name:")
        coachname = input("> ")
        print("Enter Number of Seats:")
        capacity = int(input("> "))
        print("Creating coach...")
        create_coach_query = "INSERT INTO coaches (coach_number, train_id, capacity) VALUES (%s, %s, %s)"
        coach_data = (coachname, train_id, capacity)

        try:
            cursor.execute(create_coach_query, coach_data)
            cnx.commit()
            print("Coach created successfully!")
        except pymysql.Error as error:
            print("Error creating coach:", error)

    def add_intermediate_station(train_id):
        # Add intermediate stations to a train
        while True:
            print("Enter Intermediate Station Name (or type 'done' to finish adding intermediate stations):")
            stationname = input("> ")

            if stationname.lower() == "done":
                break

            print("Adding intermediate station...")
            create_station_query = "INSERT INTO intermediate_stations (train_id, station_name) VALUES (%s, %s)"
            station_data = (train_id, stationname)

            try:
                cursor.execute(create_station_query, station_data)
                cnx.commit()
                print("Intermediate station added successfully!")
            except pymysql.Error as error:
                print("Error adding intermediate station:", error)

    while True:
        print("Welcome to the admin page")
        print("Type 1 - List All Trains")
        print("Type 2 - Create New Train")
        print("Type 0 - Go Back")

        userinput = int(input("> "))

        if userinput == 1:
            print("Listing All Trains")
            select_query = "SELECT * FROM train"
            cursor.execute(select_query)
            result = cursor.fetchall()

            for row in result:
                print(row)

        elif userinput == 2:
            print("Adding Train...")
            train_id = create_train()

            if train_id:
                while True:
                    print("Type 1 - Add Coaches")
                    print("Type 2 - Add Stations")
                    print("Type 3 - Add Intermediate Station")
                    print("Type 0 - Go Back")

                    userinput = int(input("> "))

                    if userinput == 1:
                        create_coach(train_id)
                    elif userinput == 2:
                        create_station()
                    elif userinput == 3:
                        add_intermediate_station(train_id)
                    elif userinput == 0:
                        break
                    else:
                        print("Invalid input. Please try again.")

        elif userinput == 0:
            break
        else:
            print("Invalid input. Please try again.")


def enquiry():
    print("Enter PNR")


while True:
    print("Welcome to Indian Railways")
    print("Type 1 - PNR Enquiry")
    print("Type 2 - User Login/SignUp")
    print("Type 3 - Admin")
    print("Type 0 - Exit")

    userinput = int(input(":"))

    if userinput == 1:
        enquiry()
    elif userinput == 2:
        user()
    elif userinput == 3:
        admin()
    elif userinput == 0:
        print("Exiting program...")
        break
    else:
        print("Invalid input. Please try again.")
