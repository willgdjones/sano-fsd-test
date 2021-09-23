# Sano Genetics Full-stack engineer task

# Installation

* Install Python 3.8 and Node 12.x.x
* Install Postgres. For Mac, we recommend Postgres app: https://postgresapp.com/
* Run a local postgres server and create a new database called `fsd`
* Set `connection_url` key in `local-config.json` to the database URL
* Within the `server/` directory, seed your local database with example studies by running:
  - `pip install virtualenv`
  - `virtualenv -p python3 venv`
  - `source venv/bin/activate`
  - `pip install -r requirements.txt`
  - `python run/seed_db.py`
* Within the `server/` directory, run the server locally with `run/server`.
* In a seperate terminal shell, inside the `client/` directory, download the client dependencies and run the client locally with `run/client`.
* Navigate to http://0.0.0.0:2000 in your browser

# Solutions
## Task 1-5
Answer: Please check the code and the Loom link https://www.loom.com/share/99d0219f8c0f44fb9d46f59048d6c1e8 (password: sano).
## Task 6 Client data stores
Answer: To achieve Studies and Enrollments data persistence between pages, we need to build:
* Server side: a private API to retrieve all enrolled studies of a user, e.g. /user/enrollments.
* Client side: AJAX calls in the background to keep local data updated, change the displayed content without reloading the entire page when switching between pages.
## Task 7 Forum system
Answer: A typical design is to build a Threads table and a Posts table.  A Thread (id, userId, title, created_at, updated_at) corresponds to the thread of the post created by a user and all its comments. A post (id, threadId, userId, body, created_at, updated_at) can correspond to the post itself or a comment. Users-Threads, Threads-Posts and Users-Posts form three one-to-many relationships.

Some efforts are needed to make data retrieval efficient, e.g. building indexes upon Posts, keeping data in memory if immediate updates are unnecessary.

Another element to maintain a healthy forum is to defend against malicious content. A starting point can be building a profanity filter based on a word list. More advanced methods include using regular expressions to filter out dangerous external links and utilizing natural language processing techniques for spam detection.
## Task 8 Password security
Answer: There are a couple of common rules for a strong password, e.g.:
* Minimum 8 characters (and maximum X characters).
* At least 1 letter between [a-z] and 1 letter between [A-Z].
* At least 1 digit between [0-9].
* At least 1 character from [!@#?].

The above list may serve as a starting point. There are other methods to further check the complexity of a password, e.g. the entropy calculation and dictionary-based approaches, however, we should be aware that we need to give users informative suggestions for improvement when they fill in unsafe passwords.

I only suggest using a third party solution (e.g. an open source library https://pypi.org/project/password-strength/ ) after careful scrutiny (to check if the code does some malicious behaviors getting the passwords exposed, e.g. writing down the password into logs). Considering that the logic of password validation is not extremely complex, an in-house solution may be sufficient and take less time.
## Task 9 Token authentication
Answer: The localStorage is not secure because an attacker who can run JavaScript on the website (e.g. XSS) can access it. If the site uses a third party JavaScript library located in another site, which is compromised, the attacker is able to alter the lib code to steal the authentication information in the localStorage.

A more secure way is to use HttpOnly cookies, which are inaccessible by the client side. A nice post regarding this issue is https://dev.to/rdegges/please-stop-using-local-storage-1i04 .
