class utils:
    def assertListText(self,list,value):
        for i in list:
            print(i.text)
            assert i.text == value
            print("assert pass")