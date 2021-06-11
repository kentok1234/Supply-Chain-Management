from Core.controller import Controller

class EditProdukController(Controller):

    def __init__(self, parent, data):
        super(EditProdukController, self).__init__()
        self.frame = self.view("EditProduk").EditProduk(parent)
        print(data)

    def main(self):
        self.frame.Show()