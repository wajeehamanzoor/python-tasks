from collections import namedtuple
from tokenize import String
from xmlrpc.client import Boolean

from Team import Team


class Menu:
    global team_info
    global team_data
    team_info = {}
    team_data = ['Enter City Name: ', 'Fee Paid? [yes/no]', 'Number of Players: ']
    Option = namedtuple('Option', 'label')
    _separator = "=" * 25
    _options = {1: Option("Add Team"), 2: Option("Select Team"),
                3: Option("Update Team"), 4: Option("Delete Team"),
                5: Option("Exit")}

    def print_header(self):
        print("{0}\n Please Select An Option\n{0}\n".format(self._separator))

    def print_mainMenu(self):
        self.print_header()
        for option in sorted(self._options.keys()):
            print("{0} {1}".format(option, self._options[option].label))

    def prompt(self):
        return int(input("Select Option: "))

    def handle_input(self, chosen_option):
        try:
            if chosen_option == 1:
                team_name = input("Enter Team Name: ")
                team_info[team_name] = {}
                for entry in team_data:
                    team_info[team_name][entry] = input(entry)
                print(team_info)

            if chosen_option == 2:
                name = input("Enter Team Name: ")
                for k, v in team_info.items():
                    if name == k:
                        for key, value in v.items():
                            print('City Name: ' + (v['Enter City Name: ']))
                            print('Fee Paid: ' + (v['Fee Paid? [yes/no]']))
                            print('Number of Players: ' + (v['Number of Players: ']))
                            break
                    else:
                        print("Enter correct name")
            if chosen_option == 3:
                name = input("Enter Team Name You Want To Update: ")
                for k, v in team_info.items():
                    if name == k:
                        team_info[k]['Enter City Name: '] = input('Enter City: ')
                        team_info[k]['Fee Paid? [yes/no]'] = input('Fee paid ?')
                        team_info[k]['Number of Players: '] = input('Enter Players: ')
                        break
                    else:
                        print("Enter correct name")

            if chosen_option == 4:
                name = input("Enter Team Name You Want To Delete: ")
                for k in list(team_info.keys()):
                    if name == k:
                        del team_info[k]
                    else:
                        print("Enter correct name")
                print(team_info)
        except KeyError:
            print("Wrong Option")


def main():
    menu = Menu()
    menu.print_mainMenu()
    menu.handle_input(menu.prompt())

    totalTeams = len(team_info)

    def totalFees(n):
        count = 0
        for k, v in team_info.items():
            for x, z in v.items():
                if z == 'yes':
                    count=count+1
        return count*Team.fee

    def nonPaidTeamsPercent(n):
        count = 0
        for k, v in team_info.items():
            for x, z in v.items():
                if z == 'no':
                    count = count + 1
        percentage = (count / n )* 100
        return percentage

    print("\nTotal Number of Teams are: ", totalTeams)
    print("\nTotal Sum of Fees is: ", totalFees(totalTeams))
    print("\nTotal percentage is: ", nonPaidTeamsPercent(totalTeams))
    main()


if __name__ == '__main__':
    main()
#     if x == 'Fee Paid? [yes/no]':
            #         if v == 'yes':
            #             count = count+1