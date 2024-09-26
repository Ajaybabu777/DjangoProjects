class father():
    def outputgf(self):
        print("Iam the father")

    def walking(self):
        print("iam going to walking in every day")

class mother():
    def output(self):
        print("Iam the parent")

    def office(self):
        print("iam going to office in every day")

    def club(self):
        print("iam going to club to play a cards")

class child(father,mother):
    def outputchild(self):
        print("iam a child")

    def school(self):
        print("iam going to school in every day")

    def playground(self):
        print("iam going to playground everyday to play a cricket")

a=child()
a.outputchild()
a.school()
a.club()
a.output()
a.walking()