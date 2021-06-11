from Core.controller import Controller
import wx


class TambahProdukController(Controller):
    dataid = None
    dataname = None

    def __init__(self, parent):
        super(TambahProdukController, self).__init__()
        self.frame = self.view("TambahProduk").TambahProduk(parent)
        self.modelsupplier = self.model("Supplier").SupplierModel()
        self.modelproduk = self.model("Produk").ProdukModel()

        self.setValueCombobox()

        # Connect Events
        self.frame.btn_batal.Bind(wx.EVT_BUTTON, self.btn_batalOnButtonClick)
        self.frame.btn_simpan.Bind(wx.EVT_BUTTON, self.btn_simpanOnButtonClick)

    def main(self):
        self.frame.ShowModal()

    def setValueCombobox(self):
        data = self.modelsupplier.getNameSupplier()
        self.dataid = [id for id, nama in data]
        self.dataname = [nama for id, nama in data]

        self.frame.input_supplier.Append(self.dataname)

    def dataValidation(self):
        supplier = self.frame.input_supplier.GetValue()
        produk = self.frame.input_produk.GetValue()
        jumlah = self.frame.input_jumlah.GetValue()
        harga = self.frame.input_harga.GetValue()

        # Check Data Null
        if supplier == "" or produk == "" or jumlah == "" or harga == "":
            return 0
        else:
            if jumlah.isnumeric() and harga.isnumeric():
                return 1
            else:
                return -1

    def btn_batalOnButtonClick(self, event):
        self.frame.Close()

    def btn_simpanOnButtonClick(self, event):
        if self.dataValidation() < 0:
            wx.MessageDialog(self.frame, "Jumlah atau harga harus angka!", "Error tambah produk").ShowModal()

        elif self.dataValidation() == 0:
            wx.MessageDialog(self.frame, "Data harus diisi!", "Error tambah produk").ShowModal()

        else:
            supplier = self.frame.input_supplier.GetValue()
            supplierindex = self.dataname.index(supplier)
            supplierid = self.dataid[supplierindex]
            produk = self.frame.input_produk.GetValue()
            jumlah = self.frame.input_jumlah.GetValue()
            harga = self.frame.input_harga.GetValue()

            if self.modelproduk.setDataProduk((supplierid, produk, jumlah, harga)) == 1:
                wx.MessageDialog(self.frame, "Data produk berhasil ditambahkan!", "Success").ShowModal()
                self.frame.Close()

            else:
                wx.MessageDialog(self.frame, "Terjadi kesalahan", "Error tambah produk").ShowModal()
