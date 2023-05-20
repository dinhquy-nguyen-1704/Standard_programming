from sub_module import emailProcess, printMsg

def main():
    emails = ["qwe@gmail.com", "12345@gmail.com", "zxcvbnm@gmail.com"]
    for email in emails:
        email_username, email_domain = emailProcess(email)
        printMsg(email_username, email_domain)

if __name__ == "__main__":
    main()