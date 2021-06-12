import wx


class TambahSupplier(wx.Dialog):
    def __init__(self, parent):
        super(TambahSupplier, self).__init__(parent, title="Tambah supplier")
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        flexsizer = wx.FlexGridSizer(5, 2, 0, 0)
        flexsizer.SetFlexibleDirection(wx.BOTH)
        flexsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_suppliername = wx.StaticText(self, wx.ID_ANY, u"Nama supplier :", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.label_suppliername.Wrap(-1)

        flexsizer.Add(self.label_suppliername, 0, wx.ALL, 5)

        self.input_suppliername = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        flexsizer.Add(self.input_suppliername, 0, wx.ALL, 5)

        self.label_contact = wx.StaticText(self, wx.ID_ANY, u"Kontak :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_contact.Wrap(-1)

        flexsizer.Add(self.label_contact, 0, wx.ALL, 5)

        self.input_contact = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        flexsizer.Add(self.input_contact, 0, wx.ALL, 5)

        self.label_alamat = wx.StaticText(self, wx.ID_ANY, u"Alamat :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_alamat.Wrap(-1)

        flexsizer.Add(self.label_alamat, 0, wx.ALL, 5)

        self.input_address = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        flexsizer.Add(self.input_address, 0, wx.ALL, 5)

        self.label_kota = wx.StaticText(self, wx.ID_ANY, u"Kota :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_kota.Wrap(-1)

        flexsizer.Add(self.label_kota, 0, wx.ALL, 5)

        self.input_city = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        flexsizer.Add(self.input_city, 0, wx.ALL, 5)

        self.btn_batal = wx.Button(self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0)
        flexsizer.Add(self.btn_batal, 0, wx.ALL, 5)

        self.btn_tambah = wx.Button(self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0)
        flexsizer.Add(self.btn_tambah, 0, wx.ALL, 5)

        self.SetSizer(flexsizer)
        self.Layout()
        flexsizer.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
