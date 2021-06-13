from Core.controller import Controller
import wx.grid
import wx


class HomeController(Controller):
    row = -1
    row_supplier = -1
    id = -1

    def __init__(self):
        super(HomeController, self).__init__()
        self.produkmodel = self.model("Produk").ProdukModel()
        self.employeemodel = self.model("Pegawai").PegawaiModel()
        self.suppliermodel = self.model("Supplier").SupplierModel()
        self.frame = self.view("Home").Home(None, self.produkmodel.getJumlahProduk()[0],
                                            self.suppliermodel.getJumlahSupplier()[0])
        self.data = self.produkmodel.getDataProduk()
        self.data_supplier = self.suppliermodel.getDataSupplier()

        self.jumlah_pegawai = self.employeemodel.getJumlahPegawai()
        self.jumlah_produk = self.produkmodel.getJumlahProduk()
        self.jumlah_supplier = self.suppliermodel.getJumlahSupplier()

        self.frame.label_jumlah_pegawai.SetLabel(str(self.jumlah_pegawai[0]))
        self.frame.label_jumlah_produk.SetLabel(str(self.jumlah_produk[0]))
        self.frame.label_jumlah_supplier.SetLabel(str(self.jumlah_supplier[0]))

        # Grid
        # self.frame.data_produk.SetCellValue((1, 2), "halo")
        self.setDataProduk()
        self.setDataSupplier()

        # Connect Events
        # Produk
        self.frame.Bind(wx.EVT_TOOL, self.tool_refreshOnToolClicked, id=self.frame.tool_refresh.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_addOnToolClicked, id=self.frame.tool_add.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_deleteOnToolClicked, id=self.frame.tool_delete.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_editOnToolClicked, id=self.frame.tool_edit.GetId())
        self.frame.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.data_produkOnGridCellLeftClick,
                        id=self.frame.data_produk.GetId())

        # Supplier
        self.frame.Bind(wx.EVT_TOOL, self.tool_refreshOnToolClicked, id=self.frame.tool_refresh_supplier.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_add_supplierOnToolClicked, id=self.frame.tool_add_supplier.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_delete_supplierOnToolCLicked, id=self.frame.tool_delete_supplier.GetId())
        self.frame.Bind(wx.EVT_TOOL, self.tool_edit_supplierOnToolClicked, id=self.frame.tool_edit_supplier.GetId())
        self.frame.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.data_supplierOnGridCellLeftClick,
                        id=self.frame.data_supplier.GetId())


    def main(self, id):
        self.id = id
        self.frame.Show()
        self.setDataProfile()

    def setDataProduk(self):
        for i in range(len(self.data)):
            for j in range(4):
                self.frame.data_produk.SetCellValue((i, j), str(self.data[i][j+1]))

    def setDataSupplier(self):
        for i in range(len(self.data_supplier)):
            for j in range(4):
                self.frame.data_supplier.SetCellValue((i, j), str(self.data_supplier[i][j+1]))

    def tool_refreshOnToolClicked(self, event):
        self.frame.Close()
        newcontroller = HomeController()
        newcontroller.main(self.id)

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

    def tool_add_supplierOnToolClicked(self, event):
        controller = self.controller("TambahSupplier").TambahSupplierController(self.frame)
        controller.main()

    def tool_delete_supplierOnToolCLicked(self, event):
        if self.row_supplier >= 0:
            controller = self.controller("EditSupplier").EditSupplierController()

        else:
            wx.MessageDialog(self.frame, "Pilih baris terlebih dahulu", "Error delete data").ShowModal()

    def tool_edit_supplierOnToolClicked(self, event):
        if self.row_supplier >= 0:
            controller = self.controller("EditSupplier").EditSupplierController(self.frame, self.data_supplier[self.row_supplier])
            controller.main()

        else:
            wx.MessageDialog(self.frame, "Pilih baris terlebih dahulu", "Error delete data").ShowModal()


    def data_produkOnGridCellLeftClick(self, event):
        self.row = event.GetRow()
        self.frame.data_produk.SelectRow(event.GetRow())

    def data_supplierOnGridCellLeftClick(self, event):
        self.row_supplier = event.GetRow()
        self.frame.data_supplier.SelectRow(event.GetRow())

    def setDataProfile(self):
        data = self.employeemodel.getDataPersonPegawai(self.id)

        self.frame.input_nama_depan.SetLabel(data[0])
        self.frame.input_nama_belakang.SetLabel(data[1])
        self.frame.input_telepon.SetLabel(data[2])
        self.frame.input_email.SetLabel(data[3])
        self.frame.input_alamat.SetLabel(data[4])
        self.frame.input_kota.SetLabel(data[5])
        self.frame.input_jabatan.SetLabel(data[6])
