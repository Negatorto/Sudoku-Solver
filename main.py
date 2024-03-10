# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from ui import Ui_Widget


def stamp(sudoku):
    for riga in sudoku:
        print(" ".join(map(str, riga)))


def search_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None


def line(sudoku, num, pos):
    return num not in sudoku[pos[0]]


def column(sudoku, num, pos):
    return num not in [sudoku[i][pos[1]] for i in range(9)]


def box(sudoku, num, pos):
    box_line = pos[0] // 3
    box_column = pos[1] // 3
    for i in range(box_line * 3, box_line * 3 + 3):
        for j in range(box_column * 3, box_column * 3 + 3):
            if sudoku[i][j] == num and (i, j) != pos:
                return False
    return True


def resolve(sudoku):
    empty = search_empty(sudoku)
    if not empty:
        return True
    ln, cn = empty

    for num in range(1, 10):
        if line(sudoku, num, (ln, cn)) and column(sudoku, num, (ln, cn)) and box(sudoku, num, (ln, cn)):
            sudoku[ln][cn] = num

            if resolve(sudoku):
                return True

            sudoku[ln][cn] = 0

    return False


class Sudoku:
    def __init__(self, line: list):
        self.complete = []

        self.l1 = line.copy()
        self.l2 = line.copy()
        self.l3 = line.copy()
        self.l4 = line.copy()
        self.l5 = line.copy()
        self.l6 = line.copy()
        self.l7 = line.copy()
        self.l8 = line.copy()
        self.l9 = line.copy()

    def generate(self):
        self.complete += [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9]
        # for sublist in self.complete:
        #     print(sublist)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.sudoku = Sudoku([0] * 9)

        self.ui.solveButton.clicked.connect(self.solve)
        self.ui.cancelBotton.clicked.connect(self.clear)

    def clear(self):
        self.sudoku = Sudoku([""] * 9)

        for widget_name in self.ui.__dict__:
            widget = getattr(self.ui, widget_name)
            if isinstance(widget, QLineEdit):
                widget.clear()

        self.update_labels()
        QMessageBox.information(self, "Successful", "Sudoku has been canceled.")

    def update_labels(self):
        label_mapping = {
            'a1_2': self.sudoku.l1[0], 'a2_2': self.sudoku.l1[1], 'a3_2': self.sudoku.l1[2],
            'b1_2': self.sudoku.l1[3], 'b2_2': self.sudoku.l1[4], 'b3_2': self.sudoku.l1[5],
            'c1_2': self.sudoku.l1[6], 'c2_2': self.sudoku.l1[7], 'c3_2': self.sudoku.l1[8],

            'a4_2': self.sudoku.l2[0], 'a5_2': self.sudoku.l2[1], 'a6_2': self.sudoku.l2[2],
            'b4_2': self.sudoku.l2[3], 'b5_2': self.sudoku.l2[4], 'b6_2': self.sudoku.l2[5],
            'c4_2': self.sudoku.l2[6], 'c5_2': self.sudoku.l2[7], 'c6_2': self.sudoku.l2[8],

            'a7_2': self.sudoku.l3[0], 'a8_2': self.sudoku.l3[1], 'a9_2': self.sudoku.l3[2],
            'b7_2': self.sudoku.l3[3], 'b8_2': self.sudoku.l3[4], 'b9_2': self.sudoku.l3[5],
            'c7_2': self.sudoku.l3[6], 'c8_2': self.sudoku.l3[7], 'c9_2': self.sudoku.l3[8],

            'd1_2': self.sudoku.l4[0], 'd2_2': self.sudoku.l4[1], 'd3_2': self.sudoku.l4[2],
            'e1_2': self.sudoku.l4[3], 'e2_2': self.sudoku.l4[4], 'e3_2': self.sudoku.l4[5],
            'f1_2': self.sudoku.l4[6], 'f2_2': self.sudoku.l4[7], 'f3_2': self.sudoku.l4[8],

            'd4_2': self.sudoku.l5[0], 'd5_2': self.sudoku.l5[1], 'd6_2': self.sudoku.l5[2],
            'e4_2': self.sudoku.l5[3], 'e5_2': self.sudoku.l5[4], 'e6_2': self.sudoku.l5[5],
            'f4_2': self.sudoku.l5[6], 'f5_2': self.sudoku.l5[7], 'f6_2': self.sudoku.l5[8],

            'd7_2': self.sudoku.l6[0], 'd8_2': self.sudoku.l6[1], 'd9_2': self.sudoku.l6[2],
            'e7_2': self.sudoku.l6[3], 'e8_2': self.sudoku.l6[4], 'e9_2': self.sudoku.l6[5],
            'f7_2': self.sudoku.l6[6], 'f8_2': self.sudoku.l6[7], 'f9_2': self.sudoku.l6[8],

            'g1_2': self.sudoku.l7[0], 'g2_2': self.sudoku.l7[1], 'g3_2': self.sudoku.l7[2],
            'h1_2': self.sudoku.l7[3], 'h2_2': self.sudoku.l7[4], 'h3_2': self.sudoku.l7[5],
            'i1_2': self.sudoku.l7[6], 'i2_2': self.sudoku.l7[7], 'i3_2': self.sudoku.l7[8],

            'g4_2': self.sudoku.l8[0], 'g5_2': self.sudoku.l8[1], 'g6_2': self.sudoku.l8[2],
            'h4_2': self.sudoku.l8[3], 'h5_2': self.sudoku.l8[4], 'h6_2': self.sudoku.l8[5],
            'i4_2': self.sudoku.l8[6], 'i5_2': self.sudoku.l8[7], 'i6_2': self.sudoku.l8[8],

            'g7_2': self.sudoku.l9[0], 'g8_2': self.sudoku.l9[1], 'g9_2': self.sudoku.l9[2],
            'h7_2': self.sudoku.l9[3], 'h8_2': self.sudoku.l9[4], 'h9_2': self.sudoku.l9[5],
            'i7_2': self.sudoku.l9[6], 'i8_2': self.sudoku.l9[7], 'i9_2': self.sudoku.l9[8],
        }

        for label_name, value in label_mapping.items():
            label = getattr(self.ui, label_name)
            label.setText(str(value))

    def solve(self):
        index_mapping_l1 = {'a1': 0, 'a2': 1, 'a3': 2, 'b1': 3, 'b2': 4, 'b3': 5, 'c1': 6, 'c2': 7, 'c3': 8}
        index_mapping_l2 = {'a4': 0, 'a5': 1, 'a6': 2, 'b4': 3, 'b5': 4, 'b6': 5, 'c4': 6, 'c5': 7, 'c6': 8}
        index_mapping_l3 = {'a7': 0, 'a8': 1, 'a9': 2, 'b7': 3, 'b8': 4, 'b9': 5, 'c7': 6, 'c8': 7, 'c9': 8}
        index_mapping_l4 = {'d1': 0, 'd2': 1, 'd3': 2, 'e1': 3, 'e2': 4, 'e3': 5, 'f1': 6, 'f2': 7, 'f3': 8}
        index_mapping_l5 = {'d4': 0, 'd5': 1, 'd6': 2, 'e4': 3, 'e5': 4, 'e6': 5, 'f4': 6, 'f5': 7, 'f6': 8}
        index_mapping_l6 = {'d7': 0, 'd8': 1, 'd9': 2, 'e7': 3, 'e8': 4, 'e9': 5, 'f7': 6, 'f8': 7, 'f9': 8}
        index_mapping_l7 = {'g1': 0, 'g2': 1, 'g3': 2, 'h1': 3, 'h2': 4, 'h3': 5, 'i1': 6, 'i2': 7, 'i3': 8}
        index_mapping_l8 = {'g4': 0, 'g5': 1, 'g6': 2, 'h4': 3, 'h5': 4, 'h6': 5, 'i4': 6, 'i5': 7, 'i6': 8}
        index_mapping_l9 = {'g7': 0, 'g8': 1, 'g9': 2, 'h7': 3, 'h8': 4, 'h9': 5, 'i7': 6, 'i8': 7, 'i9': 8}

        for key, value in index_mapping_l1.items():
            self.sudoku.l1[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l2.items():
            self.sudoku.l2[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l3.items():
            self.sudoku.l3[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l4.items():
            self.sudoku.l4[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l5.items():
            self.sudoku.l5[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l6.items():
            self.sudoku.l6[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l7.items():
            self.sudoku.l7[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l8.items():
            self.sudoku.l8[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        for key, value in index_mapping_l9.items():
            self.sudoku.l9[value] = int(getattr(self.ui, key).text()) if getattr(self.ui, key).text().isdigit() else 0

        self.sudoku.generate()
        resolve(self.sudoku.complete)
        stamp(self.sudoku.complete)
        self.update_labels()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
