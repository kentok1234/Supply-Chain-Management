import wx

# class login inheritance dari class frame
class Login(wx.Frame):

    def __init__(self, parent):
        """
        This is view login
        """
        # wx.frame.__init__(self, parent)
        super(Login, self).__init__(parent, style=wx.CAPTION | wx.TAB_TRAVERSAL, size=(300, 150))
        self.SetTitle("Login")
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        boxsizer = wx.BoxSizer(wx.VERTICAL)

        self.container = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, -1), wx.TAB_TRAVERSAL)
        gridsizer = wx.GridSizer(3, 2, 0, 0)

        self.label_username = wx.StaticText(self.container, wx.ID_ANY, u"username :", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.label_username.Wrap(-1)

        gridsizer.Add(self.label_username, 0, wx.ALL, 5)

        self.input_username = wx.TextCtrl(self.container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          0)
        gridsizer.Add(self.input_username, 0, wx.ALL, 5)

        self.label_password = wx.StaticText(self.container, wx.ID_ANY, u"password :", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.label_password.Wrap(-1)

        gridsizer.Add(self.label_password, 0, wx.ALL, 5)

        self.input_password = wx.TextCtrl(self.container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_PASSWORD)
        gridsizer.Add(self.input_password, 0, wx.ALL, 5)

        self.btn_batal = wx.Button(self.container, wx.ID_ANY, u"batal", wx.DefaultPosition, wx.DefaultSize, 0)
        gridsizer.Add(self.btn_batal, 0, wx.ALL, 5)

        self.btn_login = wx.Button(self.container, wx.ID_ANY, u"login", wx.DefaultPosition, wx.DefaultSize, 0)
        gridsizer.Add(self.btn_login, 0, wx.ALL, 5)

        self.container.SetSizer(gridsizer)
        self.container.Layout()
        boxsizer.Add(self.container, 1, wx.EXPAND, 5)

        self.SetSizer(boxsizer)
        self.Layout()

        self.Centre(wx.BOTH)
