from Core.controller import Controller
import wx.grid
import wx


class HomeController(Controller):
    row = -1

    def __init__(self):
        super(HomeController, self).__init__()
        self.produkmodel = self.model("Produk").ProdukModel()
        self.frame = self.view("Home").Home(None, self.produkmodel.getJumlahProduk()[0])
        self.employeemodel = self.model("Pegawai").PegawaiModel()
        self.data = self.produkmodel.getDataProduk()

        self.jumlah_pegawai = self.employeemodel.getJumlahPegawai()
        self.jumlah_produk = self.produkmodel.getJumlahProduk()

        self.frame.label_jumlah_pegawai.SetLabel(str(self.jumlah_pegawai[0]))
        self.frame.label_jumlah_produk.SetLabel(str(self.jumlah_produk[0]))

        # Grid
        # self.frame.data_produk.SetCellValue((1, 2), "halo")
        self.setDataProduk()

        # Connect Events
        self.frame.Bind(wx.EVT_TOOL, self.tool_refreshOnToolClicked, id=self.frame.tool_refresh.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_addOnToolClicked, id=self.frame.tool_add.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_deleteOnToolClicked, id=self.frame.tool_delete.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_editOnToolClicked, id=self.frame.tool_edit.GetId())
        self.frame.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.data_produkOnGridCellLeftClick,
                        id=self.frame.data_produk.GetId())

    def main(self):
        self.frame.Show()

    def setDataProduk(self):
        for i in range(len(self.data)):
            for j in range(4):
                self.frame.data_produk.SetCellValue((i, j), str(self.data[i][j+1]))

    def tool_refreshOnToolClicked(self, event):
        self.frame.Close()
        newcontroller = HomeController()
        newcontroller.main()

    def tool_addOnToolClicked(self, event):
        controller = self.controller("TambahProduk").TambahProdukController(self.frame)
        controller.main()

    def tool_deleteOnToolClicked(self, event):
        if self.row >= 0:
            msg = wx.MessageDialog(self.frame, "Apakah anda yakin akan menghapus data?", "Delete data", wx.OK|wx.CANCEL)

            if msg.ShowModal() == wx.ID_OK:
                self.produkmodel.deleteDataProduk(self.data[self.row][0])
                wx.MessageDialog(self.frame, "Produk telah terhapus", "Delete data").ShowModal()

        else:
            wx.MessageDialog(self.frame, "Pilih baris terlebih dahulu", "Error delete data").ShowModal()

    def tool_editOnToolClicked(self, event):
        if self.row >= 0:
            controller = self.controller("EditProduk").EditProdukController(self.frame, self.data[self.row])
            controller.main()

        else:
            wx.MessageDialog(self.frame, "Pilih baris terlebih dahulu", "Error delete data").ShowModal()

    def data_produkOnGridCellLeftClick(self, event):
        self.row = event.GetRow()
        self.frame.data_produk.SelectRow(event.GetRow())
