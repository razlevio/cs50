import plates


class Test_Plates_Is_valid:
    def test_is_valid_1(self):
        result = plates.is_valid("user1+user2@mycompany.com")

    def test_is_valid_2(self):
        result = plates.is_valid("user@host:300")

    def test_is_valid_3(self):
        result = plates.is_valid("bed-free@tutanota.de")

    def test_is_valid_4(self):
        result = plates.is_valid("email@Google.com")

    def test_is_valid_5(self):
        result = plates.is_valid("something.example.com")

    def test_is_valid_6(self):
        result = plates.is_valid("")
