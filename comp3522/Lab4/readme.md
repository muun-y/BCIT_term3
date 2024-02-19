[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13620342&assignment_repo_type=AssignmentRepo)
**Lab 4 - The F.A.M.**

**(Family Appointed Moderator)**


**Introduction**

You may work in groups of two (2) for this lab work. Create a team or
join an existing team on GitHub classroom. Make sure to include both
your names and student numbers in comments at the top of `driver.py`.

This lab work will provide a platform for you to use the Python
Fundamentals you have learnt so far while you stretch and flex your OOP
muscles. You will get a chance to see how Object-oriented design can
have a crucial role to play and an opportunity to implement the SOLID
design principles.

Now, imagine if you will (or don\'t if this is already a reality for
you) that you have a teenage child that is spoiled. This child tends to
go on spending sprees and does not use their allowance and the salary
from their part-time work responsibly. As a concerned parent you are
worried that 2 years from now when your child leaves home to go to
university, they won\'t have any savings to draw upon.

Enter the **F.A.M.**

The **Family Appointed Moderator (or F.A.M.)** is a parental control
lock on an individual's bank account. In this lab work, you will create
a MVP (Minimum Viable Prototype) of the F.A.M. system. Your system will
register a user, keep track of all the spending/transactions on their
bank account and lock the account if certain conditions are met.

When going through the lab work brief, start drawing out a preliminary
UML class diagram to identify all the classes, attributes and any behaviors that you may need. This should be done before writing any code.

This lab work is quite open ended and designed that way so you can personalize the end result and have fun with it. Come up with
interesting concepts and ideas. Be creative and enjoy the process! I
encourage you to come discuss your designs with me if you want any
feedback.

**Submission Requirements**

1.  This is a group lab work. All code, if any, must be written by the group members. 


**Grading**

The lab work is marked out of **100**. For full marks, you must:


1.  Submit a UML Class Diagram depicting appropriate use of OOP principles, inheritance and design in your code. **70 Marks**

2.  Structure/design your classes to maximize code re-use, make it readable and maintainable. Follow the SOLID principles and the Law of Demeter. **30 Marks**


**Implementation Requirements**

The F.A.M. must implement the following features:

**Registering A User**

On startup, the user (usually a parent) must register their child\'s
financial details. This includes (but is not necessarily limited to):

-   The users name

-   Age

-   User Type (more on this below)

-   Bank Account number

-   Bank Name

-   Bank Balance

-   Their budgets (more on this below)

For testing purposes **you must** also include a load_test_users() method/function that loads hardcoded test users. This will help you test your code and avoid entering user details every time you run the program.

You must still allow anyone using this program to register a user if they want to. The test method is for testing purposes only. Your program
should also **support multiple users** and the functionality to **switch between them**.

No need for a username/password login, present a list of existing users and allow the user to select the account they wish to log into

```
Log in as:                                                            
1. Jeff                                                              
2. Lawrence                                                          
3. Chrissy                                                           
```

Log into Jeff's account by pressing '1' and 'Enter'

**Budget Categories**

Each child that is being monitored is assigned the following budget
categories. The exact value of each budget is assigned when registering
the child as a user.

-   Games and Entertainment

-   Clothing and Accessories

-   Eating Out

-   Miscellaneous

A User Menu

Once the user account is set up and the budgets have been created, the
system should prompt the user with the following menu options (or a
variation of the following menu). The rest of the lab work brief
explains how the app/each of these menu options should work.

1. **View Budgets**

Selecting this option should show the user the current status of their
budgets (locked or not) in addition to the amount spent, amount left,
and the total amount allocated to the budget.

2. **Record a Transaction**

This should take the user to a sub-menu where they are prompted to
enter the transaction details (refer to the \"Record Transactions\"
heading below).

3. **View Transactions by Budget**

This should take the user to a sub-menu where they select their budget
category and view all the transactions to date in that category.

4. **View Bank Account Details**

The application should print out the bank account details of the user
and all transactions conducted to date alongside the closing balance.

5. **Logout**

Returns the user to the main menu

**Record Transactions**

The application should maintain a collection of transactions which
represent money going out of the users bank account. Provide the user an
option to enter transaction details.

Each transaction should contain the following information:

-   The timestamp the transaction was recorded (a nicely formatted
datetime value).

-   The dollar amount (positive, non-zero number).

-   The budget category that this transaction belongs to.

    -   Instead of prompting the user to enter the name of the budget
    category, provide them with a list of categories and ask them
    to select one.

-   The name of the shop/website where the purchase took place.

The user should **not** be allowed to record a transaction if the
transaction would cause their bank balance to go below zero.
Additionally, the system should subtract the required amount from the
users bank balance once a transaction has been recorded.

Depending on the type of user (more on this in the **User Types**
section below), after a transaction has been recorded your system will
want to perform checks to see if a notification should be issued. A list
of transactions that have taken place in a budget category should be
printed out to the console if:

-   The user receives a notification that they are getting close to
exceeding their assigned budget for the category in question

-   The user receives a notification that they have exceeded their
assigned budget for the category in question.

The transactions printed should be the transactions pertaining to the
budget category in question. That is, if the user gets a notification
that they are about to exceed their budget for \"Games and
Entertainment\", then any transactions belonging to this category should
be printed for review.

**Lock Out**

The app has the ability to lock a user out of recording transactions
(and effectively spending any money) based on certain conditions as
specified by their User Type (more on this in the User Types section
below).

If a user has been locked from a budget category:

-   They should be notified of this via a console message.

-   Any attempt at recording transactions in the affected budget
category should be denied.

**User Types**

Every family and every child is unique. The F.A.M. prototype recognizes
this face and supports different types of users. The app provides
different moderation levels for each user type.

**The Angel**

The Angel represents a user whose parents are not worried at all. This
child has never (as far as their parents are concerned) broken a single
rule. They already have a five-year plan in place and a roadmap which is
guaranteed to get them into Harvard. The Angel is the child who would
set up their own FAM account so they can monitor their expenses.

This user type:

-   Gets a notification if they exceed more than 90% of a budget.

-   Gets **politely** notified if they exceed a budget category.

-   Never gets locked out of a budget category. They can continue
spending money even if they exceed the budget in question.

**The Troublemaker**

The Troublemaker represents a user who often finds themselves in\...
well.. trouble. These are usually minor incidents and their parents are
concerned but not worried. Parents usually set up a FAM account to
monitor their expenses and impose light restrictions.

This user type:

-   Gets a notification if they exceed more than 75% of a budget
category.

-   Gets **politely** notified if they exceed a budget category.

-   Gets locked out of conducting transactions in a budget category if
they exceed it by 120% of the amount assigned to the budget in
question.

**The Rebel**

The Rebel represents a user who refuses to follow any rules and believes
that society should be broken down and restructured. They do not want to
pursue \"*a* *standard education*\", \"*conform to the
economic/capitalist foundations of society*\" or \"*get a job*\".
Parents of these children are quite worried and turn to F.A.M. when they
are out of options.

This user type is strictly monitored:

-   Gets a notification if they exceed more than 50% of a budget
category.

-   Gets **ruthlessly** notified if they exceed a budget category.

-   Gets locked out of conducting transactions in a budget category if
they exceed it by 100% of the amount assigned to the budget in
question.

-   If they exceed their budget in 2 or more categories then they get
locked out of their account completely. Display a message
indicating the user is locked out, and kick them out of the user
menu immediately, returning to the main menu.

**Concluding Thoughts**

Remember to approach your code in an object-oriented fashion. Don\'t
just start bashing out code and hoping that it will all work out.
Consider these steps.

1.  Identify the classes and objects you will need. Figure out what each
class is responsible for.

2.  Draw a UML class diagram showing how the classes/objects relate to
each other. Write down the attributes and methods.

    a.  At this stage you can do a simple sketch on paper. Don\'t worry
    about syntax and only mention the important
    attributes/methods.

3.  **OPTIONAL** Write some code. Writing the classes and methods will help you identify any issues with your design. You can always go back and change your UML diagram. This is an iterative process. Writing methods specifications will help you identify what each method should do. 

4.  Repeat from step 1. (Take an iterative approach!)

When creating your final UML diagram, be sure to check syntax, and
mention all the attributes and methods.

That's it. Good luck, and have fun!

**FAQ**

***Can a child spend more than their budget?***

Yes, think of the budget as a soft ceiling on how much a user can spend
in a specific category. If a user begins approaching or exceeding their
budget, the system will warn the user or lock them out of that budget
category depending on the user type (Angel, Troublemaker, Rebel)

**Balances and budgets before:**

Troublemaker Jeff's balance is \$400

Game budget: \$100

Clothing budget: \$100

Eating budget: \$100

Misc budget: \$100

*Jeff attempts to spend \$105 in the Game category. The transaction is
accepted but he gets a notification indicating he's over the 75% Game
budget*

**Balances and budgets after:**

Troublemaker Jeff's balance is \$295

Game budget: \$-5

Clothing budget: \$100

Eating budget: \$100

Misc budget: \$100

***Can a child spend more than their balance?***

No, the system will block the transaction from being recorded and
display a message indicating there is not enough money left.

**Balances and budgets before:**

Troublemaker Jeff's balance is \$500

Game budget: \$100

Clothing budget: \$100

Eating budget: \$100

Misc budget: \$100

*Jeff attempts to spend \$600 in the Game category. The transaction is
REJECTED because the \$600 transaction amount is greater than Jeff's
remaining balance of \$500*

**Balances and budgets after:**

Troublemaker Jeff's balance is \$500

Game budget: \$100

Clothing budget: \$100

Eating budget: \$100

Misc budget: \$100

***Can a child's balance exceed the combined budget amounts?***

Yes, this is to allow children to exceed their budget. The balance must
be greater than or equal to the combined budgets

**Balances and budgets before:**

Troublemaker Jeff's balance is **\$500**

Game budget: **\$100**

Clothing budget: **\$100**

Eating budget: **\$100**

Misc budget: **\$100**

Notice the \$500 balance is greater than the combined \$400 value of
budgets

***Can budgets have different initial amounts?***

Yes

Troublemaker Jeff's balance is **\$2000**

Game budget: **\$100**

Clothing budget: **\$200**

Eating budget: **\$300**

Misc budget: **\$400**

***What does the menu flow look like?***

The user is provided with a main menu when starting the program

```
Welcome to the FAM! Select from the options below                    
                                                                     
1.  Register new user                                                
                                                                     
2.  Login existing user                                              
                                                                     
3.  Exit program                                                     
```

If the user selects option 1, open a new menu to allow the user to enter
information about a new user (name, age, user type, balance, bank name,
bank number, game budget, food budget, etc)

```
  Registering a new user

  Enter the user's name: Minnie
```

If the user selects option 2, open a new menu to select which user to
log in as:

```
Select user to log in as                                             
                                                                     
1.  Garfield (Troublemaker)                                          
                                                                     
2.  Snoopy (Rebel)                                                   
                                                                     
3.  Mickey (Angel)                                                   
```

After logging in, the user is presented with the user menu mentioned
earlier:

```
Logged in as Mickey (Angel)                                          
                                                                     
Select from one of the options below:                                
                                                                     
1.  View Budgets                                                     
                                                                     
2.  Record a Transaction                                             
                                                                     
3.  View Transactions by Budget                                      
                                                                     
4.  View Bank Account Details                                        
                                                                     
5.  Logout                                                           
```

Selecting Logout will bring the user back to the main menu

```
Welcome to the FAM! Select from the options below                    
                                                                     
1.  Register new user                                                
                                                                     
2.  Login existing user                                              
                                                                     
3.  Exit                                                             
```

**How should we store the Transaction time?**

Store the transaction time as `datetime.now()`, no need to ask the user
for specific hour, day, time.

**What happens when a locked out user tries to log in?**

The user will be prevented from logging into their account. In the
example below, the user is attempting to log into Snoopy's account but
it is locked

```
Select user to log in as                                             
                                                                     
1.  Garfield (Troublemaker)                                          
                                                                     
2.  Snoopy (Rebel) - LOCKED                                          
                                                                     
3.  Mickey (Angel)                                                   
                                                                     
Choose a user to log in as: **2**                                    
```

After attempting to log in as Snoopy, the user is shown a message
indicating the account is locked and they can not log in

```
Snoopy's account is LOCKED, they can not log in                      
                                                                     
Select user to log in as                                             
                                                                     
1.  Garfield (Troublemaker)                                          
                                                                     
2.  Snoopy (Rebel) - LOCKED                                          
                                                                     
3.  Mickey (Angel)                                                   
                                                                     
Choose a user to log in as:                                          
```

**Does data need to be saved between sessions?**

No. If you register 10 new accounts, add 100 transactions. All accounts and transactions will be lost if user end the program.