class Email():

    has_been_read = False # initialise emails to unread

    # Initialise the instance variables for this class
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    # Method to channge has_been_read from False to True
    def mark_as_read(self):
        self.has_been_read = True
    
inbox = [] # initialise an empty to store email objects

# Function to initially populate inbox with 3 emails
def populate_inbox():
    email1 = Email("abc@def.com", "Welcome to DEF!", "We're glad to have you!")
    email2 = Email("ghi@def.com", "Here's your code!", "Get 25\% off your first order.")
    email3 = Email("jkl@def.com", "How was it?", "Tell us what you think of MonpQ")
    
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)
    return inbox

# Method to list all emails in inbox
def list_emails():
    i = 0
    for email in inbox:
        em_list = inbox[i]
        print(str(i) + " " + em_list.subject_line)
        i += 1

# Method to read emails and set has_been_read() function to True
def read_email():
    i = int(input("Enter the index of the email you want to read: "))
    print("Sender email address: ", inbox[i].email_address)
    print("Email subject line: ", inbox[i].subject_line)
    print("Here's the email content:\n", inbox[i].email_content)
    inbox[i].has_been_read = True
    print(f"Email from {inbox[i].email_address} marked as read")

populate_inbox() # runs the populate_inbox 

# Other menu operations
menu = True

while True:
    print("1. Read an email \n2. View unread emails \n3. Quit application")
    user_choice = int(input("Enter selection: "))

    if user_choice == 1:
        read_email()

    elif user_choice == 2:
        i = 0
        for email in inbox:
            if inbox[i].has_been_read == False:
                print(str(i), inbox[i].subject_line)
            i += 1

    elif user_choice == 3:
        exit()
    else:
        print("Oops! You have entered an incorrect input")