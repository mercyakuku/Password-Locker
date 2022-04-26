import unittest
from passcode import User
from passcode import Credentials

class TestClass(unittest.TestCase):
    
       # A Test class that defines test cases for the User class.
    
    def setUp(self):
        
        # Method that runs before each individual test methods run.
        
        self.new_user = User('Mercy Akuku','Z3(*@)f1pm')

    def test_init(self):
    
        # Test case to check if the object has been initialized correctly
        
        self.assertEqual(self.new_user.username,'Mercy Akuku')
        self.assertEqual(self.new_user.password,'Z3(*@)f1pm')

    def test_save_user(self):
        
        # Test case to test if a new user instance has been saved into the User list

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    
    # Test class that defines test cases for credentials class

    def setUp(self):
        
     # Method that runs before each individual credentials to test if methods run.

        self.new_credential = Credentials('Gmail','Mercy Akuku','mn5Gsi23*@')
    def test_init(self):
        
        # Test case to check if a new Credentials instance has been initialized correctly
        
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'Mercy Akuku')
        self.assertEqual(self.new_credential.password,'mn5Gsi23*@')

    def save_credential_test(self):
        
        # Test case to test if the credential object is saved into the credentials list.

        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):

        # Method that does clean up after each test case has run.
        
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        
        # Test to check if we can save multiple credentials objects to our credentials list
        
        self.new_credential.save_details()
        test_credential = Credentials("LinkedIn","Mercy Akuku","12sima()23") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        
        # Test method to test if we can remove an account credentials from our credentials_list
        
        self.new_credential.save_details()
        test_credential = Credentials("LinkedIn","Mercy Akuku","12sima()23")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentialr(self):
        
        # Test to check if we can find a credential entry by account name and display the details of the credential
        
        self.new_credential.save_details()
        test_credential = Credentials("LinkedIn","Mercy Akuku","12sima()23") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("LinkedIn")

        self.assertEqual(the_credential.account,test_credential.account)

    def test_credential_exist(self):
        
        # Test to check if we can return boolean true or false based on whether we or can't find the credential.
        
        self.new_credential.save_details()
        the_credential = Credentials("LinkedIn", "Mercy Akuku", "12sima()23")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("LinkedIn")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
        
        # Method that displays all the credentials that has been saved by the user
        
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()
