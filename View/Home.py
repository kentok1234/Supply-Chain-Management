import wx
import wx.grid

class Home(wx.Frame):
    def __init__(self, parent, len_row):
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
        self.data_produk.SetColLabelValue(2, u"Harga")
        self.data_produk.SetColLabelValue(3, u"Harga")
        self.data_produk.SetColLabelValue(4, u"Jumlah")
        self.data_produk.SetColLabelValue(5, wx.EmptyString)
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

        boxsizer.Add(self.list_book, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(boxsizer)
        self.Layout()
        self.Centre(wx.BOTH)
