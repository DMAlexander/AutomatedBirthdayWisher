import smtplib

my_email = "alexanderdevin50@gmail.com"
password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="appbrewerytesting@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
    connection.close()