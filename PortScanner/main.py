
import socket


def ask_user():

    # assigning local variables
    show_closed = ""
    lower_ports = 0
    upper_ports = 0

    host = input("Enter the IP address or the Website: ")

    try:
        ip = socket.gethostbyname(host) # gets the ip from the hostname given by the user
    except:
        print("Please enter a valid hostname or IP address.")
        return

    try:
        while lower_ports < 1 or lower_ports > 65535:
            lower_ports = int(input("Enter the lower bound of the ports you want to scan: "))

        while upper_ports < 1 or upper_ports > 65535:
            upper_ports = int(input("Enter the upper bound of the ports you want to scan: "))

        if lower_ports > upper_ports: # error handling for the upper and lower bound
            print("The lower bound cannot exceed the upper bound.")
            return # goes back to try

    except ValueError:
        print("Please enter a valid number between 1 and 65535.")
        return # goes back to the try block

    while show_closed != "y" and show_closed != "n":
        show_closed = input("Would you like to show the closed ports? (y/n): ").lower()
        if show_closed != "y" and show_closed != "n":
            print("Please enter either 'y' or 'n'.")

    scan(ip,lower_ports,upper_ports,show_closed)


def scan(ip, lower_ports, upper_ports, show_closed):
    print("Scanning for open ports...")
    for port in range(lower_ports, upper_ports + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # only works for ipv4, also sock_stream makes it so it checks w DNS
        s.settimeout(1) # if it takes too long, it skips

        try:
            s.connect((ip, port))
            print("Port {} is open".format(port))

        except:
            if show_closed == "y":
                print("Port {} is closed".format(port))

        finally:
            s.close()


if __name__ == "__main__":
    flag = False
    while not flag:
        ask_user()
        try:
            choice = input("Would you like to scan for more open ports? (y/n): ")
            if choice.lower() == "n":
                flag = True

        except ValueError:
            print("please enter either 'y' or 'n'.")


