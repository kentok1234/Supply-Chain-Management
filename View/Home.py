import wx
import wx.grid


class Home(wx.Frame):
    def __init__(self, parent, len_row, len_row_supplier):
        super(Home, self).__init__(parent, size=(800, 300))
        self.SetTitle("Home")

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        boxsizer = wx.BoxSizer(wx.HORIZONTAL)

        self.list_book = wx.Listbook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.dashboard = wx.Panel(self.list_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gridsizer_dashboard = wx.GridSizer(2, 2, 0, 0)

        sb_jumlah_pegawai = wx.StaticBoxSizer(wx.StaticBox(self.dashboard, wx.ID_ANY, u"Jumlah pegawai"), wx.VERTICAL)

        self.label_jumlah_pegawai = wx.StaticText(sb_jumlah_pegawai.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.label_jumlah_pegawai.Wrap(-1)

        self.label_jumlah_pegawai.SetFont(
            wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sb_jumlah_pegawai.Add(self.label_jumlah_pegawai, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        gridsizer_dashboard.Add(sb_jumlah_pegawai, 1, wx.EXPAND, 5)

        sb_jumlah_produk = wx.StaticBoxSizer(wx.StaticBox(self.dashboard, wx.ID_ANY, u"Jumlah produk"), wx.VERTICAL)

        self.label_jumlah_produk = wx.StaticText(sb_jumlah_produk.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.label_jumlah_produk.Wrap(-1)

        self.label_jumlah_produk.SetFont(
            wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sb_jumlah_produk.Add(self.label_jumlah_produk, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        gridsizer_dashboard.Add(sb_jumlah_produk, 1, wx.EXPAND, 5)

        sb_jumlah_supplier = wx.StaticBoxSizer(wx.StaticBox(self.dashboard, wx.ID_ANY, u"Jumlah Supplier"), wx.VERTICAL)

        self.label_jumlah_supplier = wx.StaticText(sb_jumlah_supplier.GetStaticBox(), wx.ID_ANY, u"0",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_jumlah_supplier.Wrap(-1)

        self.label_jumlah_supplier.SetFont(
            wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sb_jumlah_supplier.Add(self.label_jumlah_supplier, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        gridsizer_dashboard.Add(sb_jumlah_supplier, 1, wx.EXPAND, 5)

        self.dashboard.SetSizer(gridsizer_dashboard)
        self.dashboard.Layout()
        gridsizer_dashboard.Fit(self.dashboard)
        self.list_book.AddPage(self.dashboard, u"Dashboard", False)
        self.produk = wx.Panel(self.list_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        boxsizer_produk = wx.BoxSizer(wx.VERTICAL)

        self.menu_toolbar = wx.ToolBar(self.produk, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL)
        self.tool_refresh = self.menu_toolbar.AddLabelTool(wx.ID_ANY, u"refresh",
                                                           wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR),
                                                           wx.NullBitmap, wx.ITEM_NORMAL, u"refresh", wx.EmptyString,
                                                           None)

        self.tool_add = self.menu_toolbar.AddLabelTool(wx.ID_ANY, u"tambah produk",
                                                       wx.ArtProvider.GetBitmap(wx.ART_PLUS, wx.ART_TOOLBAR),
                                                       wx.NullBitmap, wx.ITEM_NORMAL, u"tambah produk", wx.EmptyString,
                                                       None)

        self.tool_delete = self.menu_toolbar.AddLabelTool(wx.ID_ANY, u"hapus produk",
                                                          wx.ArtProvider.GetBitmap(wx.ART_MINUS, wx.ART_TOOLBAR),
                                                          wx.NullBitmap, wx.ITEM_NORMAL, u"hapus produk",
                                                          wx.EmptyString, None)

        self.tool_edit = self.menu_toolbar.AddLabelTool(wx.ID_ANY, u"Edit produk",
                                                        wx.ArtProvider.GetBitmap(wx.ART_FIND_AND_REPLACE,
                                                                                 wx.ART_TOOLBAR), wx.NullBitmap,
                                                        wx.ITEM_NORMAL, u"Edit produk", wx.EmptyString, None)

        self.menu_toolbar.Realize()

        boxsizer_produk.Add(self.menu_toolbar, 0, wx.EXPAND, 5)

        self.data_produk = wx.grid.Grid(self.produk, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1), 0)

        # Grid
        self.data_produk.CreateGrid(len_row, 4)
        self.data_produk.EnableCellEditControl(False)
        self.data_produk.EnableEditing(False)
        self.data_produk.EnableGridLines(True)
        self.data_produk.EnableDragGridSize(False)
        self.data_produk.SetMargins(0, 0)

        # Columns
        self.data_produk.SetColSize(0, 200)
        self.data_produk.EnableDragColMove(False)
        self.data_produk.EnableDragColSize(True)
        self.data_produk.SetColLabelSize(30)
        self.data_produk.SetColLabelValue(0, u"Supplier")
        self.data_produk.SetColLabelValue(1, u"Nama produk")
        self.data_produk.SetColLabelValue(2, u"Jumlah")
        self.data_produk.SetColLabelValue(3, u"Harga")
        self.data_produk.SetColLabelValue(4, wx.EmptyString)
        self.data_produk.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.data_produk.EnableDragRowSize(True)
        self.data_produk.SetRowLabelSize(80)
        self.data_produk.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.data_produk.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        boxsizer_produk.Add(self.data_produk, 1, wx.ALL | wx.EXPAND, 5)

        self.produk.SetSizer(boxsizer_produk)
        self.produk.Layout()
        boxsizer_produk.Fit(self.produk)

        self.list_book.AddPage(self.produk, u"Produk", True)

        self.supplier = wx.Panel(self.list_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        boxsizer_supplier = wx.BoxSizer(wx.VERTICAL)

        self.toolbar_supplier = wx.ToolBar(self.supplier, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TB_HORIZONTAL)
        self.tool_refresh_supplier = self.toolbar_supplier.AddLabelTool(wx.ID_ANY, u"Refresh",
                                                                        wx.ArtProvider.GetBitmap(wx.ART_REDO,
                                                                                                 wx.ART_TOOLBAR),
                                                                        wx.NullBitmap, wx.ITEM_NORMAL, u"Refresh",
                                                                        wx.EmptyString, None)

        self.tool_add_supplier = self.toolbar_supplier.AddLabelTool(wx.ID_ANY, u"Add",
                                                                    wx.ArtProvider.GetBitmap(wx.ART_PLUS,
                                                                                             wx.ART_TOOLBAR),
                                                                    wx.NullBitmap, wx.ITEM_NORMAL, u"Tambah data",
                                                                    wx.EmptyString, None)

        self.tool_delete_supplier = self.toolbar_supplier.AddLabelTool(wx.ID_ANY, u"Delete",
                                                                       wx.ArtProvider.GetBitmap(wx.ART_MINUS,
                                                                                                wx.ART_TOOLBAR),
                                                                       wx.NullBitmap, wx.ITEM_NORMAL, u"Hapus supplier",
                                                                       wx.EmptyString, None)

        self.tool_edit_supplier = self.toolbar_supplier.AddLabelTool(wx.ID_ANY, u"Edit",
                                                                     wx.ArtProvider.GetBitmap(wx.ART_FIND_AND_REPLACE,
                                                                                              wx.ART_TOOLBAR),
                                                                     wx.NullBitmap, wx.ITEM_NORMAL, u"Edit supplier",
                                                                     wx.EmptyString, None)

        self.toolbar_supplier.Realize()

        boxsizer_supplier.Add(self.toolbar_supplier, 0, wx.EXPAND, 5)

        self.data_supplier = wx.grid.Grid(self.supplier, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.data_supplier.CreateGrid(len_row_supplier, 4)
        self.data_supplier.EnableEditing(False)
        self.data_supplier.EnableGridLines(True)
        self.data_supplier.EnableDragGridSize(False)
        self.data_supplier.SetMargins(0, 0)

        # Columns
        self.data_supplier.SetColSize(0, 150)
        self.data_supplier.SetColSize(1, 120)
        self.data_supplier.SetColSize(2, 200)
        self.data_supplier.SetColSize(3, 1)
        self.data_supplier.EnableDragColMove(False)
        self.data_supplier.EnableDragColSize(True)
        self.data_supplier.SetColLabelSize(30)
        self.data_supplier.SetColLabelValue(0, u"Nama supplier")
        self.data_supplier.SetColLabelValue(1, u"Kontak")
        self.data_supplier.SetColLabelValue(2, u"Alamat")
        self.data_supplier.SetColLabelValue(3, u"Kota")
        self.data_supplier.SetColLabelValue(4, wx.EmptyString)
        self.data_supplier.SetColLabelValue(5, wx.EmptyString)
        self.data_supplier.SetColLabelValue(6, wx.EmptyString)
        self.data_supplier.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.data_supplier.EnableDragRowSize(True)
        self.data_supplier.SetRowLabelSize(80)
        self.data_supplier.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.data_supplier.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        boxsizer_supplier.Add(self.data_supplier, 0, wx.ALL, 5)

        self.supplier.SetSizer(boxsizer_supplier)
        self.supplier.Layout()
        boxsizer_supplier.Fit(self.supplier)
        self.list_book.AddPage(self.supplier, u"Supplier", True)

        self.profile = wx.Panel(self.list_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        flexsizer_profile = wx.FlexGridSizer(7, 2, 0, 0)
        flexsizer_profile.SetFlexibleDirection(wx.BOTH)
        flexsizer_profile.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_nama_depan = wx.StaticText(self.profile, wx.ID_ANY, u"Nama depan :", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.label_nama_depan.Wrap(-1)

        flexsizer_profile.Add(self.label_nama_depan, 0, wx.ALL, 5)

        self.input_nama_depan = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_nama_depan.Wrap(-1)

        flexsizer_profile.Add(self.input_nama_depan, 0, wx.ALL, 5)

        self.label_nama_belakang = wx.StaticText(self.profile, wx.ID_ANY, u"Nama belakang :", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.label_nama_belakang.Wrap(-1)

        flexsizer_profile.Add(self.label_nama_belakang, 0, wx.ALL, 5)

        self.input_nama_belakang = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_nama_belakang.Wrap(-1)

        flexsizer_profile.Add(self.input_nama_belakang, 0, wx.ALL, 5)

        self.label_telepon = wx.StaticText(self.profile, wx.ID_ANY, u"Telepon :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_telepon.Wrap(-1)

        flexsizer_profile.Add(self.label_telepon, 0, wx.ALL, 5)

        self.input_telepon = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_telepon.Wrap(-1)

        flexsizer_profile.Add(self.input_telepon, 0, wx.ALL, 5)

        self.label_email = wx.StaticText(self.profile, wx.ID_ANY, u"Email :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_email.Wrap(-1)

        flexsizer_profile.Add(self.label_email, 0, wx.ALL, 5)

        self.input_email = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_email.Wrap(-1)

        flexsizer_profile.Add(self.input_email, 0, wx.ALL, 5)

        self.label_alamat = wx.StaticText(self.profile, wx.ID_ANY, u"Alamat :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_alamat.Wrap(-1)

        flexsizer_profile.Add(self.label_alamat, 0, wx.ALL, 5)

        self.input_alamat = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_alamat.Wrap(-1)

        flexsizer_profile.Add(self.input_alamat, 0, wx.ALL, 5)

        self.label_kota = wx.StaticText(self.profile, wx.ID_ANY, u"Kota :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_kota.Wrap(-1)

        flexsizer_profile.Add(self.label_kota, 0, wx.ALL, 5)

        self.input_kota = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_kota.Wrap(-1)

        flexsizer_profile.Add(self.input_kota, 0, wx.ALL, 5)

        self.label_jabatan = wx.StaticText(self.profile, wx.ID_ANY, u"Jabatan :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_jabatan.Wrap(-1)

        flexsizer_profile.Add(self.label_jabatan, 0, wx.ALL, 5)

        self.input_jabatan = wx.StaticText(self.profile, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_jabatan.Wrap(-1)

        flexsizer_profile.Add(self.input_jabatan, 0, wx.ALL, 5)

        self.profile.SetSizer(flexsizer_profile)
        self.profile.Layout()
        flexsizer_profile.Fit(self.profile)
        self.list_book.AddPage(self.profile, u"Profile", True)

        boxsizer.Add(self.list_book, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(boxsizer)
        self.Layout()
        self.Centre(wx.BOTH)
