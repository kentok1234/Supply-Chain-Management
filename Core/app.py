from Core.controller import Controller
import wx


class App(wx.App):
    def OnInit(self):
        print('App was running. . .')
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        login = Controller()
        frame = login.controller("Login").LoginController()
        frame.main()
        return True
