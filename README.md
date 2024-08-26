## Welcome to Surf Swap

### Problem Statement:
1. Surfboards are expensive, and rental options are bleak.
2. There aren't many options to try a surfboard before commiting to buying one, which is upwards of $750 each time!

### Our Solution
* Try before you buy
* We connect surfers, and help them gain access to one another's collections of surfboards
* Users can create an account, add their own surfboards, and make reservations to borrow other people's boards
* This eliminates the risk of buying a board that simply does not click, which unsurprisingly happens a lot
* Have a dream board you're dying to try? Find it on Surf Swap

### This project is made with
- Django
- SQLite database

To run the project locally:
- activate your virtual environment
- `python manage.py runserver`
- open in browser at localhost:8000

To access the admin interface:
- localhost:8000/admin

### Entity Relationship Diagram
![Surf Swap ERD](https://github.com/user-attachments/assets/3f6bc02e-0be6-40f0-a867-074ce15b2974)

### Endpoints
<img width="897" alt="Screenshot 2024-08-26 at 1 49 46 PM" src="https://github.com/user-attachments/assets/c09c3fd3-6439-4f6c-8062-f804ae7512a4">

### Screen Shots
Landing Page:
<img width="1628" alt="Screenshot 2024-08-21 at 8 13 04 PM" src="https://github.com/user-attachments/assets/4571092a-ee62-4fdd-bcd0-e084a90d21de">
User Collection:
<img width="1225" alt="Screenshot 2024-08-21 at 8 20 39 PM" src="https://github.com/user-attachments/assets/24665203-4fbf-4418-a550-d17da2009f6d">
Surfboard Detail:
<img width="1502" alt="Screenshot 2024-08-21 at 8 21 02 PM" src="https://github.com/user-attachments/assets/ae9c94ca-34f2-45ed-a09e-32fd4d885a0f">
Empty Reservation Section:
<img width="1035" alt="Screenshot 2024-08-21 at 8 29 55 PM" src="https://github.com/user-attachments/assets/afa269dc-7189-4bdc-bce6-8cf414acb7f3">

### Future Developments
- Break application into microservices using Docker
- Add ability to send messages
- Add user regions to display boards within a specific distance to user
- additional reservation features/ wait list
- increased testing coverage
