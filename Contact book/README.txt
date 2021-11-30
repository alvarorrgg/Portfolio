
This is a sketch of a very simple contact book.
The program let you access, add, delete and modify data in the contact_book
The contact_book is a simple text file.
Its a easy way to practice python
A little bit harder implementation could using a GUI
This would make the contact book a better aproximation to a real life aplication.

To make things more realistic the contacts inside the contact book will have the next structure
Name | Surname | Surname_2 | Age | Phone_Number | Email | Relation|
You will be able to add a contact with some missming info.

Now lets apply some database knowledge.
If you think about it, There can be few people with the same Name, SUrname, Age and relation.
The only info that cant be repited is the email and phone.
This is not always true but we will make it this way to simplify things
This two will be our primary keys but it will be a little bit different than usual.
Since you can add a contact with missing info the only real requirement to add info is that either the mail or the phone number or both are added.
The id is auto added when adding a contact.
I think the only big deal in this proyect is when deleting or modifiying, get into the file search for the correct position to delete then change the whole
so te program doesnt mess.
Thats not really hard but it cang et really funny.
If you think about in the access routine, The user might search for a contact based on the name.
Well since we have non sorted values, the best way to find the correct value is using a LSearch.
But what if when adding a new contact we sorted all the contact book using a insert sort algorithm
THen we could use BSearch to search through the contact_book.

Well, you might think that the second way is better but actually it depends
If you were gonna add alot of contacts then sorting the contact_book everytime you add a contact would be really bad.
Therefor a LSearch with normal adding would be better.
On the other hand if you were looking for using ur contacts alot and adding new contacts from time to time then the BSearch would be the best option for you.
In this case, and since is a contact_book, which you usually use to search for phones and barely never add new phones, then we re gonna use Bsearch and sort algorithm.
