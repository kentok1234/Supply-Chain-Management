from Core.controller import Controller
import wx


class TambahSupplierController(Controller):
    def __init__(self, parent):
        super(TambahSupplierController, self).__init__()
        self.frame = self.view("TambahSupplier").TambahSupplier(parent)
        self.modelsupplier = self.model("Supplier").SupplierModel()

        # event
        self.frame.Bind(wx.EVT_BUTTON, self.btn_tambahOnClicked, self.frame.btn_tambah)
        self.frame.Bind(wx.EVT_BUTTON, self.btn_batalOnClicked, self.frame.btn_batal)

    def main(self):
        self.frame.Show()

    def dataValidation(self):
        namasupplier = self.frame.input_suppliername.GetValue()
        kontak = self.frame.input_contact.GetValue()
        alamat = self.frame.input_address.GetValue()
        kota = self.frame.input_city.GetValue()

        # Check Data Null
        if namasupplier == "" or kontak == "" or alamat == "" or kota == "":
            return 0
        else:
            return 1

    def btn_tambahOnClicked(self, event):
        if self.dataValidation() == 0:
            wx.MessageDialog(self.frame, "Data harus diisi!", "Error tambah supplier").ShowModal()

        else:
            namasupplier = self.frame.input_suppliername.GetValue()
            kontak = self.frame.input_contact.GetValue()
            alamat = self.frame.input_address.GetValue()
            kota = self.frame.input_city.GetValue()

            if self.modelsupplier.setDataSupplier((namasupplier, kontak, alamat, kota)) == 1:
                wx.MessageDialog(self.frame, "Data supplier berhasil ditambahkan!", "Success").ShowModal()
                self.frame.Close()

            else:
                wx.MessageDialog(self.frame, "Terjadi kesalahan", "Error tambah supplier").ShowModal()

    def btn_batalOnClicked(self, event):
        self.frame.Close()
