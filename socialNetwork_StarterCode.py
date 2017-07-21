# Please complete the -- ADD YOUR CODE HERE -- parts ONLY!

-- ADD YOUR CODE HERE -- User:      
    """ Consists of the instance variables, methods etc to create a user object """

    def -- ADD YOUR CODE HERE --(self, user_name, user_id):     # Constructor to initialize the class instance variables
        """ Initializes the name and ID variables with the user entry """
        self.user_name = -- ADD YOUR CODE HERE --
        self.user_id = -- ADD YOUR CODE HERE --
        self.connections = []       # Creates a list to store the user object's connections

    def addConnection(self, connection_id):
        """ Adds the user object's connections to the connections list that was created in the __init__ function (constructor) """
        self.connections.append(-- ADD YOUR CODE HERE --)

    def getUserName(self):
        """ Returns the stored user name value """
        return self.user_name

    def getConnections(self):
        """ Returns the stored connection list values """
        return self.connections

    def getUserID(self):
        """ Returns the user ID value """
        return self.user_id

class Network:
    """ Consists of the instance variables, methods etc to create a social network platform """

    def __init__(self):         # Constructor to initialize the class instance variables
        """ Creates and initializes a users list to store the social network users """
        self.users = []

    def numUsers(self):
        """ Returns the length of the users list """
        return -- ADD YOUR CODE HERE --

    def addUser(self, username):
        """ Adds a user to be included in the users list by the append method """
        for -- ADD YOUR CODE HERE -- :     # Compares the new user with the values in the users list to determine the user name was not taken
            if username == user.getUserName():
                print("Sorry, that name is taken. Try again.")
                return
        #If username was not taken, add user to the network
        user_id = len(self.users)
        self.users.append(User(username, user_id))      # Keeps and tracks down the user ID related to the length of the users list

    def getUserID(self, username):
        """ Returns the user ID """
        user_id = -1
        for -- ADD YOUR CODE HERE -- :
            if -- ADD YOUR CODE HERE -- :
                user_id = user.getUserID()
        return user_id                          #If user_id = -1, that means that the username is not there

    def addConnection(self, user1, user2):      #connections are both ways in this program
        """ Adds and maintains connections for both of the users """
        user1_id = self.getUserID(-- ADD YOUR CODE HERE --)
        user2_id = self.getUserID(-- ADD YOUR CODE HERE --)

        user1 = self.users[-- ADD YOUR CODE HERE --]
        user2 = self.users[-- ADD YOUR CODE HERE --]

        if (user1_id == -1 or user2_id == -1):
            print("Sorry, one or more username is not correct. Try again.")
            return False                           #Failure, one or other username is wrong

        elif (user1_id == user2_id):
            print("Sorry, connections must be between two different users. Try again.")
            return False

        elif (user2_id in user1.getConnections()): #They're already friends
            print("{} and {} are already connected!".format(user1.getUserName(), user2.getUserName()))
            return True

        else:
            self.users[user1_id].addConnection(user2_id)
            self.users[user2_id].addConnection(user1_id)
            return True         #Success

    def printUsers(self):
        """ Prints all the users in the users list """
        print("Network Users:")
        for user in self.users:
            print("\tUser {}: {}".format(user.getUserID(), user.getUserName()))

    def printConnections(self, username):
        """ Prints all the connections of that particular user's connection list """
        user = self.users[self.getUserID(-- ADD YOUR CODE HERE --)]
        connections = user.getConnections()
        print("{}'s connections:".format(user.getUserName()))

        for friendID in connections:
            friend = self.users[friendID]
            print("\t{}".format(friend.getUserName()))

def main():
    """ To create an object of the Network class to call the related functions """

    myNetwork = -- ADD YOUR CODE HERE --       # Creates a Network class object called my_network

    done = -- ADD YOUR CODE HERE --                # Initializes the done variable to False

    while not done:             # Creates a while loop to display the menu and apply the user input
        print("\nSocial Network Menu: ")
        print("(u) Add a user")
        print("(p) Print users")
        print("(c) Add a connections")
        print("(pc) Print connections")
        print("(quit) Quit")

        action = input("Please make your choice: ")     # User entry for the menu item choice

        if action == "p":                               # Prints users
            myNetwork.printUsers()

        elif action == -- ADD YOUR CODE HERE --:        # Adds users
            username = input("What username? ")
            myNetwork.addUser(-- ADD YOUR CODE HERE --)

        elif action == "pc":                             # Prints connections
            user = input("For which user? ")
            myNetwork.printConnections(-- ADD YOUR CODE HERE --)

        elif action == -- ADD YOUR CODE HERE --:        # Adds connections
            if myNetwork.numUsers() < 2:
                print("You need at least two users to make a connection.")
                continue
            user1 = input("First username: ")
            user2 = input("Second username: ")
            myNetwork.addConnection(-- ADD YOUR CODE HERE --, -- ADD YOUR CODE HERE --)

        elif action == "quit":
            print("Sorry to see you go so soon!")
            break
        else:
            print("Sorry, I didn't understand that.")

if __name__ == "__main__":
    """ Call the main() function to test the related classes """
    main()
