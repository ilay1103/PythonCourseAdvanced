
def decrypt_password(password):
    return ''.join([chr(((ord(x)+2) - ord('a')) % 26 + ord('a')) if str(x).isalpha() else x for x in password])

def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print(decrypt_password(password))



if __name__ == "__main__":
    main()