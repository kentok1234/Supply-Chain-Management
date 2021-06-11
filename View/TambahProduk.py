import wx


class TambahProduk(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Edit produk", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_supplier = wx.StaticText(self, wx.ID_ANY, u"Supplier :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_supplier.Wrap(-1)

        fgSizer1.Add(self.label_supplier, 0, wx.ALL, 5)

        input_supplierChoices = []
        self.input_supplier = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1),
                                          input_supplierChoices, 0)
        fgSizer1.Add(self.input_supplier, 0, wx.ALL, 5)

        self.label_produk = wx.StaticText(self, wx.ID_ANY, u"Nama produk :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_produk.Wrap(-1)

        fgSizer1.Add(self.label_produk, 0, wx.ALL, 5)

        self.input_produk = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), 0)
        fgSizer1.Add(self.input_produk, 0, wx.ALL, 5)

        self.label_jumlah = wx.StaticText(self, wx.ID_ANY, u"Jumlah :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_jumlah.Wrap(-1)

        fgSizer1.Add(self.label_jumlah, 0, wx.ALL, 5)

        self.input_jumlah = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), 0)
        fgSizer1.Add(self.input_jumlah, 0, wx.ALL, 5)

        self.label_harga = wx.StaticText(self, wx.ID_ANY, u"Harga :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_harga.Wrap(-1)

        fgSizer1.Add(self.label_harga, 0, wx.ALL, 5)

        self.input_harga = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), 0)
        fgSizer1.Add(self.input_harga, 0, wx.ALL, 5)

        self.btn_batal = wx.Button(self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.btn_batal, 0, wx.ALL, 5)

        self.btn_simpan = wx.Button(self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.btn_simpan, 0, wx.ALL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()
        fgSizer1.Fit(self)

        self.Centre(wx.BOTH)
