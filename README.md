# Fpro-Play_Submissions-Grabber
Short script to retrieve program submissions on the fpro_play website that was used in subject programming fundamentals of the Master in computer engineering couse [MIEIC]

### Requires
- html2text (you can get this using pip for example)
- a valid username and token (token is stored in your browser's cookies OR a valid login link (which you can get by cleaning your browser cookies, entering the website and after inserting your email you will receive in your email the link you need)

### Output

Only the completed submissions will be retrieved, wrong or incomplete exercises won't be downloaded.

The files will be stored in folders matching each of the topics, in the same folder where this script is run.

Files are stored in .py extension and utf-8 encoding.

The files contain the question and your answer.

## Warning
If you have previously used the program, the files will be overwritten so make sure to save your changes online, on a different folder or under a different name

Do not force close or some files may be incomplete or may still be open on the background not and you won't be able to delete or edit them while they're not closed.
