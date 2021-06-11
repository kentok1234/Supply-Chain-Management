from Core.controller import Controller
import wx


class LoginController(Controller):

    def __init__(self):
        super(LoginController, self).__init__()
        self.frame = self.view("Login").Login(None)
        self.controlhome = self.controller("Home").HomeController()
        self.loginmodel = self.model("User").UserModel()

        # Connect Events
        self.frame.btn_batal.Bind(wx.EVT_BUTTON, self.btnBatalOnButtonClick)
        self.frame.btn_login.Bind(wx.EVT_BUTTON, self.btnLoginOnButtonClick)

    def main(self):
        self.frame.Show(True)

    def btnBatalOnButtonClick(self, event):
        self.frame.Close()

    def btnLoginOnButtonClick(self, event):
        if self.dataValidation() == 1:
            self.controlhome.main()
            self.frame.Close()

    def dataValidation(self):
        username = self.frame.input_username.GetValue()
        password = self.frame.input_password.GetValue()

        data = self.loginmodel.getOneDataUser((username, password))

        if data:
            return 1
