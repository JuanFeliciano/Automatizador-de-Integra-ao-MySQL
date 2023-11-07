import mysql.connector
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from integracao import Ui_MainWindow

conexao = mysql.connector.connect(
    host="localhost", user="root", password="151029", database="bdjuan"
)
cursor = conexao.cursor()


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.create)
        self.pushButton_6.clicked.connect(self.read)
        self.pushButton_7.clicked.connect(self.update)
        self.pushButton_8.clicked.connect(self.delete)

        self.tableWidget_resultados.setColumnCount(2)
        self.tableWidget_resultados.setHorizontalHeaderLabels(
            ["Nome do Produto", "Valor"]
        )
        self.tableWidget_resultados.addTab(self.tableWidget_resultados, "Resultados")

    def create(self):
        nome_produto = self.textEdit.toPlainText()
        valor = self.textEdit_2.toPlainText()
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}","{valor}")'
        cursor.execute(comando)
        conexao.commit()

    def read(self):
        comando = f"SELECT * FROM vendas"
        cursor.execute(comando)
        resultados = cursor.fetchall()

        self.tableWidget_resultados.setRowCount(0)

        for row, data in enumerate(resultados):
            self.tableWidget_resultados.insertRow(row)
            for col, values in enumerate(data):
                item = QTableWidgetItem(str(values))
                self.tableWidget_resultados.setItem(row, col, item)

    def update(self):
        nome_produto = self.textEdit_3.toPlainText()
        valor = self.textEdit_4.toPlainText()
        idVendas = self.textEdi_6.toPlainText()
        comando = f'UPDATE vendas SET nome_produto = "{nome_produto}", valor = "{valor}" WHERE idVendas = {idVendas}'
        cursor.execute(comando)
        conexao.commit()

    def delete(self):
        idVendas = self.lineEdit_textEdit_5.text()
        comando = f"DELETE FROM vendas WHERE idVendas = {idVendas}"
        cursor.execute(comando)
        conexao.commit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
