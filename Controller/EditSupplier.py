from Core.controller import Controller
import wx


class EditSupplierController(Controller):
    def __init__(self, parent, data):
        super(EditSupplierController, self).__init__()
        self.frame = self.view("EditSupplier").EditSupplier(parent)
        self.suppliermodel = self.model(("Supplier")).SupplierModel()
        self.data = data

        # set data
        self.frame.input_suppliername.SetValue(self.data[1])
        self.frame.input_contact.SetValue(self.data[2])
        self.frame.input_address.SetValue(self.data[3])
        self.frame.input_city.SetValue(self.data[4])

        # event
        self.frame.btn_batal.Bind(wx.EVT_BUTTON, self.btn_batalOnButtonClick)
        self.frame.btn_simpan.Bind(wx.EVT_BUTTON, self.btn_simpanOnButtonClick)

    def main(self):
        self.frame.Show()

    def btn_batalOnButtonClick(self, event):
        self.frame.Close()

    def btn_simpanOnButtonClick(self, event):
        if self.dataValidation() == 0:
            wx.MessageDialog(self.frame, "Data harus diisi!", "Error edit supplier").ShowModal()
        else:
            suppliername = self.frame.input_suppliername.GetValue()
            kontak = self.frame.input_contact.GetValue()
            alamat = self.frame.input_address.GetValue()
            kota = self.frame.input_city.GetValue()

            if self.suppliermodel.updateDataSupplier((suppliername, kontak, alamat, kota, self.data[0])) == 1:
                wx.MessageDialog(self.frame, "Data supplier berhasil diedit!", "Success").ShowModal()
                self.frame.Close()

            else:
                wx.MessageDialog(self.frame, "Terjadi kesalahan", "Error edit supplier").ShowModal()

    def dataValidation(self):
        suppliername = self.frame.input_suppliername.GetValue()
        kontak = self.frame.input_contact.GetValue()
        alamat = self.frame.input_address.GetValue()
        kota = self.frame.input_city.GetValue()

        # Check Data Null
        if suppliername == "" or kontak == "" or alamat == "" or kota == "":
            return 0

        return 1
