from Core.controller import Controller
import wx


class EditProdukController(Controller):

    def __init__(self, parent, data):
        super(EditProdukController, self).__init__()
        self.frame = self.view("EditProduk").EditProduk(parent)
        self.modelsupplier = self.model("Supplier").SupplierModel()
        self.produkmodel = self.model("Produk").ProdukModel()
        self.data = data

        print(data)
        # set value
        self.setValueCombobox()
        self.frame.input_supplier.SetValue(str(self.data[1]))
        self.frame.input_produk.SetValue(str(self.data[2]))
        self.frame.input_jumlah.SetValue(str(self.data[3]))
        self.frame.input_harga.SetValue(str(self.data[4]))

        # Connect Events
        self.frame.btn_batal.Bind(wx.EVT_BUTTON, self.btn_batalOnButtonClick)
        self.frame.btn_simpan.Bind(wx.EVT_BUTTON, self.btn_simpanOnButtonClick)

    def main(self):
        self.frame.Show()

    def btn_batalOnButtonClick(self, event):
        self.frame.Close()

    def btn_simpanOnButtonClick(self, event):
        if self.dataValidation() < 0:
            wx.MessageDialog(self.frame, "Jumlah atau harga harus angka!", "Error edit produk").ShowModal()

        elif self.dataValidation() == 0:
            wx.MessageDialog(self.frame, "Data harus diisi!", "Error edit produk").ShowModal()

        else:
            supplier = self.frame.input_supplier.GetValue()
            supplierindex = self.dataname.index(supplier)
            supplierid = self.dataid[supplierindex]
            produk = self.frame.input_produk.GetValue()
            jumlah = self.frame.input_jumlah.GetValue()
            harga = self.frame.input_harga.GetValue()

            if self.produkmodel.updateDataProduk((supplierid, produk, jumlah, harga, self.data[0])) == 1:
                wx.MessageDialog(self.frame, "Data produk berhasil diedit!", "Success").ShowModal()
                self.frame.Close()

            else:
                wx.MessageDialog(self.frame, "Terjadi kesalahan", "Error edit produk").ShowModal()

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

    def setValueCombobox(self):
        data = self.modelsupplier.getNameSupplier()
        self.dataid = [id for id, nama in data]
        self.dataname = [nama for id, nama in data]

        self.frame.input_supplier.Append(self.dataname)
