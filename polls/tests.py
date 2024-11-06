from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
 
class MySeleniumTests(StaticLiveServerTestCase):
    # carregar una BD de test
    fixtures = ['testdb.json',]
 
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
 
    @classmethod
    def tearDownClass(cls):
        # tanquem browser
        # comentar la propera línia si volem veure el resultat de l'execució al navegador
        cls.selenium.quit()
        super().tearDownClass()
 
    '''def test_login(self):
        # anem directament a la pàgina d'accés a l'admin panel
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
 
        # comprovem que el títol de la pàgina és el que esperem
        self.assertEqual( self.selenium.title , "Iniciar sesión | Sitio de administración de Django" )
 
        # introduïm dades de login i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('isard')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Iniciar sesión"]').click()
 
        # testejem que hem entrat a l'admin panel comprovant el títol de la pàgina
        self.assertEqual( self.selenium.title , "Sitio administrativo | Sitio de administración de Django" )

    def test_login_error(self):
        # comprovem que amb un usuari i contrasenya inexistent, el test falla
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        self.assertEqual( self.selenium.title , "Iniciar sesión | Sitio de administración de Django" )
 
        # introduim dades de login
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('usuari_no_existent')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('contrasenya_incorrecta')
        self.selenium.find_element(By.XPATH,'//input[@value="Iniciar sesión"]').click()
 
        # utilitzem assertNotEqual per testejar que NO hem entrat
        self.assertNotEqual( self.selenium.title , "Sitio administrativo | Sitio de administración de Django" )
        '''

    def test_staff_create(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
 
        # comprovem que el títol de la pàgina és el que esperem
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )
 
        # introduïm dades de login i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('isard')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
 
        # testejem que hem entrat a l'admin panel comprovant el títol de la pàgina
        self.assertEqual( self.selenium.title , "Site administration | Django site admin" )       
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/auth/user/add/'))
        #self.selenium.find_element(By.XPATH,'//input[@value="Añadir usuario"]').click()
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('staff')
        password_input = self.selenium.find_element(By.NAME,"password1")
        password_input.send_keys('pirineus')
        password_input = self.selenium.find_element(By.NAME,"password2")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()

        #self.assertEqual( self.selenium.title , "staff | Modificar usuario | Sitio de administración de Django" )

        username_input = self.selenium.find_element(By.NAME,"first_name")
        username_input.send_keys('staff')
        self.selenium.find_element(By.NAME, 'is_staff').click()
        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()
     #   self.assertEqual( self.selenium.title , "Iniciar sesión | Sitio de administración de Django" )
     
     #   self.selenium.find_element(By.NAME,'CERRAR SESIÓN').click()
    #    self.selenium.find_element(By.XPATH,'//input[@value="Iniciar sesión de nuevo"]').click()

    def test_staff_login(self):
        # anem directament a la pàgina d'accés a l'admin panel
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
 
        # comprovem que el títol de la pàgina és el que esperem
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )

        # introduïm dades de login i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('staff')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
        #self.assertEqual( self.selenium.title , "Site administration | Django site admin" ) 