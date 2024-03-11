# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(700, 450)

        self.titleLabel = QLabel(Widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 20, 701, 31))

        font = QFont()
        font.setFamilies([u"League Spartan"])
        font.setPointSize(23)
        font.setBold(False)
        font.setStrikeOut(False)
        font.setKerning(True)

        fontLight = QFont()
        fontLight.setFamilies([u"League Spartan Light"])
        fontLight.setPointSize(15)

        cssLabel = "border: 1px solid rgba(0, 0, 0, 0.15)"

        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setWordWrap(False)

        self.separator = QFrame(Widget)
        self.separator.setObjectName(u"separator")
        self.separator.setGeometry(QRect(340, 70, 20, 351))
        self.separator.setMinimumSize(QSize(3, 0))
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.solveButton = QPushButton(Widget)
        self.solveButton.setObjectName(u"solveButton")
        self.solveButton.setGeometry(QRect(118, 390, 115, 40))
        self.solveButton.setFont(fontLight)

        self.cancelBotton = QPushButton(Widget)
        self.cancelBotton.setObjectName(u"cancelBotton")
        self.cancelBotton.setGeometry(QRect(474, 390, 115, 40))
        self.cancelBotton.setFont(fontLight)

        # Block A
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 80, 91, 89))

        self.block_A = QGridLayout(self.gridLayoutWidget)
        self.block_A.setObjectName(u"block_A")
        self.block_A.setContentsMargins(0, 0, 0, 0)

        self.a1 = QLineEdit(self.gridLayoutWidget)
        self.a1.setObjectName(u"a1")
        self.block_A.addWidget(self.a1, 0, 0, 1, 1)

        self.a2 = QLineEdit(self.gridLayoutWidget)
        self.a2.setObjectName(u"a2")
        self.block_A.addWidget(self.a2, 0, 1, 1, 1)

        self.a3 = QLineEdit(self.gridLayoutWidget)
        self.a3.setObjectName(u"a3")
        self.block_A.addWidget(self.a3, 0, 2, 1, 1)

        self.a4 = QLineEdit(self.gridLayoutWidget)
        self.a4.setObjectName(u"a4")
        self.block_A.addWidget(self.a4, 1, 0, 1, 1)

        self.a5 = QLineEdit(self.gridLayoutWidget)
        self.a5.setObjectName(u"a5")
        self.block_A.addWidget(self.a5, 1, 1, 1, 1)

        self.a6 = QLineEdit(self.gridLayoutWidget)
        self.a6.setObjectName(u"a6")
        self.block_A.addWidget(self.a6, 1, 2, 1, 1)

        self.a7 = QLineEdit(self.gridLayoutWidget)
        self.a7.setObjectName(u"a7")
        self.block_A.addWidget(self.a7, 2, 0, 1, 1)

        self.a8 = QLineEdit(self.gridLayoutWidget)
        self.a8.setObjectName(u"a8")
        self.block_A.addWidget(self.a8, 2, 1, 1, 1)

        self.a9 = QLineEdit(self.gridLayoutWidget)
        self.a9.setObjectName(u"a9")
        self.block_A.addWidget(self.a9, 2, 2, 1, 1)

        #Block B
        self.gridLayoutWidget_2 = QWidget(Widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(130, 80, 91, 89))

        self.block_B = QGridLayout(self.gridLayoutWidget_2)
        self.block_B.setObjectName(u"block_B")
        self.block_B.setContentsMargins(0, 0, 0, 0)

        self.b1 = QLineEdit(self.gridLayoutWidget_2)
        self.b1.setObjectName(u"b1")
        self.block_B.addWidget(self.b1, 0, 0, 1, 1)

        self.b2 = QLineEdit(self.gridLayoutWidget_2)
        self.b2.setObjectName(u"b2")
        self.block_B.addWidget(self.b2, 0, 1, 1, 1)

        self.b3 = QLineEdit(self.gridLayoutWidget_2)
        self.b3.setObjectName(u"b3")
        self.block_B.addWidget(self.b3, 0, 2, 1, 1)

        self.b4 = QLineEdit(self.gridLayoutWidget_2)
        self.b4.setObjectName(u"b4")
        self.block_B.addWidget(self.b4, 1, 0, 1, 1)

        self.b5 = QLineEdit(self.gridLayoutWidget_2)
        self.b5.setObjectName(u"b5")
        self.block_B.addWidget(self.b5, 1, 1, 1, 1)

        self.b6 = QLineEdit(self.gridLayoutWidget_2)
        self.b6.setObjectName(u"b6")
        self.block_B.addWidget(self.b6, 1, 2, 1, 1)

        self.b7 = QLineEdit(self.gridLayoutWidget_2)
        self.b7.setObjectName(u"b7")
        self.block_B.addWidget(self.b7, 2, 0, 1, 1)

        self.b8 = QLineEdit(self.gridLayoutWidget_2)
        self.b8.setObjectName(u"b8")
        self.block_B.addWidget(self.b8, 2, 1, 1, 1)

        self.b9 = QLineEdit(self.gridLayoutWidget_2)
        self.b9.setObjectName(u"b9")
        self.block_B.addWidget(self.b9, 2, 2, 1, 1)

        #Block C
        self.gridLayoutWidget_3 = QWidget(Widget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(230, 80, 91, 89))

        self.block_C = QGridLayout(self.gridLayoutWidget_3)
        self.block_C.setObjectName(u"block_C")
        self.block_C.setContentsMargins(0, 0, 0, 0)

        self.c1 = QLineEdit(self.gridLayoutWidget_3)
        self.c1.setObjectName(u"c1")
        self.block_C.addWidget(self.c1, 0, 0, 1, 1)

        self.c2 = QLineEdit(self.gridLayoutWidget_3)
        self.c2.setObjectName(u"c2")
        self.block_C.addWidget(self.c2, 0, 1, 1, 1)

        self.c3 = QLineEdit(self.gridLayoutWidget_3)
        self.c3.setObjectName(u"c3")
        self.block_C.addWidget(self.c3, 0, 2, 1, 1)

        self.c4 = QLineEdit(self.gridLayoutWidget_3)
        self.c4.setObjectName(u"c4")
        self.block_C.addWidget(self.c4, 1, 0, 1, 1)

        self.c5 = QLineEdit(self.gridLayoutWidget_3)
        self.c5.setObjectName(u"c5")
        self.block_C.addWidget(self.c5, 1, 1, 1, 1)

        self.c6 = QLineEdit(self.gridLayoutWidget_3)
        self.c6.setObjectName(u"c6")
        self.block_C.addWidget(self.c6, 1, 2, 1, 1)

        self.c7 = QLineEdit(self.gridLayoutWidget_3)
        self.c7.setObjectName(u"c7")
        self.block_C.addWidget(self.c7, 2, 0, 1, 1)

        self.c8 = QLineEdit(self.gridLayoutWidget_3)
        self.c8.setObjectName(u"c8")
        self.block_C.addWidget(self.c8, 2, 1, 1, 1)

        self.c9 = QLineEdit(self.gridLayoutWidget_3)
        self.c9.setObjectName(u"c9")
        self.block_C.addWidget(self.c9, 2, 2, 1, 1)

        #Block D
        self.gridLayoutWidget_4 = QWidget(Widget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(30, 180, 91, 89))

        self.block_D = QGridLayout(self.gridLayoutWidget_4)
        self.block_D.setObjectName(u"block_D")
        self.block_D.setContentsMargins(0, 0, 0, 0)

        self.d1 = QLineEdit(self.gridLayoutWidget_4)
        self.d1.setObjectName(u"d1")
        self.block_D.addWidget(self.d1, 0, 0, 1, 1)

        self.d2 = QLineEdit(self.gridLayoutWidget_4)
        self.d2.setObjectName(u"d2")
        self.block_D.addWidget(self.d2, 0, 1, 1, 1)

        self.d3 = QLineEdit(self.gridLayoutWidget_4)
        self.d3.setObjectName(u"d3")
        self.block_D.addWidget(self.d3, 0, 2, 1, 1)

        self.d4 = QLineEdit(self.gridLayoutWidget_4)
        self.d4.setObjectName(u"d4")
        self.block_D.addWidget(self.d4, 1, 0, 1, 1)

        self.d5 = QLineEdit(self.gridLayoutWidget_4)
        self.d5.setObjectName(u"d5")
        self.block_D.addWidget(self.d5, 1, 1, 1, 1)

        self.d6 = QLineEdit(self.gridLayoutWidget_4)
        self.d6.setObjectName(u"d6")
        self.block_D.addWidget(self.d6, 1, 2, 1, 1)

        self.d7 = QLineEdit(self.gridLayoutWidget_4)
        self.d7.setObjectName(u"d7")
        self.block_D.addWidget(self.d7, 2, 0, 1, 1)

        self.d8 = QLineEdit(self.gridLayoutWidget_4)
        self.d8.setObjectName(u"d8")
        self.block_D.addWidget(self.d8, 2, 1, 1, 1)

        self.d9 = QLineEdit(self.gridLayoutWidget_4)
        self.d9.setObjectName(u"d9")
        self.block_D.addWidget(self.d9, 2, 2, 1, 1)

        #Block E
        self.gridLayoutWidget_5 = QWidget(Widget)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(130, 180, 91, 89))

        self.block_E = QGridLayout(self.gridLayoutWidget_5)
        self.block_E.setObjectName(u"block_E")
        self.block_E.setContentsMargins(0, 0, 0, 0)

        self.e1 = QLineEdit(self.gridLayoutWidget_5)
        self.e1.setObjectName(u"e1")
        self.block_E.addWidget(self.e1, 0, 0, 1, 1)

        self.e2 = QLineEdit(self.gridLayoutWidget_5)
        self.e2.setObjectName(u"e2")
        self.block_E.addWidget(self.e2, 0, 1, 1, 1)

        self.e3 = QLineEdit(self.gridLayoutWidget_5)
        self.e3.setObjectName(u"e3")
        self.block_E.addWidget(self.e3, 0, 2, 1, 1)

        self.e4 = QLineEdit(self.gridLayoutWidget_5)
        self.e4.setObjectName(u"e4")
        self.block_E.addWidget(self.e4, 1, 0, 1, 1)

        self.e5 = QLineEdit(self.gridLayoutWidget_5)
        self.e5.setObjectName(u"e5")
        self.block_E.addWidget(self.e5, 1, 1, 1, 1)

        self.e6 = QLineEdit(self.gridLayoutWidget_5)
        self.e6.setObjectName(u"e6")
        self.block_E.addWidget(self.e6, 1, 2, 1, 1)

        self.e7 = QLineEdit(self.gridLayoutWidget_5)
        self.e7.setObjectName(u"e7")
        self.block_E.addWidget(self.e7, 2, 0, 1, 1)

        self.e8 = QLineEdit(self.gridLayoutWidget_5)
        self.e8.setObjectName(u"e8")
        self.block_E.addWidget(self.e8, 2, 1, 1, 1)

        self.e9 = QLineEdit(self.gridLayoutWidget_5)
        self.e9.setObjectName(u"e9")
        self.block_E.addWidget(self.e9, 2, 2, 1, 1)

        #Block F
        self.gridLayoutWidget_6 = QWidget(Widget)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(230, 180, 91, 89))

        self.block_F = QGridLayout(self.gridLayoutWidget_6)
        self.block_F.setObjectName(u"block_F")
        self.block_F.setContentsMargins(0, 0, 0, 0)

        self.f1 = QLineEdit(self.gridLayoutWidget_6)
        self.f1.setObjectName(u"f1")
        self.block_F.addWidget(self.f1, 0, 0, 1, 1)

        self.f2 = QLineEdit(self.gridLayoutWidget_6)
        self.f2.setObjectName(u"f2")
        self.block_F.addWidget(self.f2, 0, 1, 1, 1)

        self.f3 = QLineEdit(self.gridLayoutWidget_6)
        self.f3.setObjectName(u"f3")
        self.block_F.addWidget(self.f3, 0, 2, 1, 1)

        self.f4 = QLineEdit(self.gridLayoutWidget_6)
        self.f4.setObjectName(u"f4")
        self.block_F.addWidget(self.f4, 1, 0, 1, 1)

        self.f5 = QLineEdit(self.gridLayoutWidget_6)
        self.f5.setObjectName(u"f5")
        self.block_F.addWidget(self.f5, 1, 1, 1, 1)

        self.f6 = QLineEdit(self.gridLayoutWidget_6)
        self.f6.setObjectName(u"f6")
        self.block_F.addWidget(self.f6, 1, 2, 1, 1)

        self.f7 = QLineEdit(self.gridLayoutWidget_6)
        self.f7.setObjectName(u"f7")
        self.block_F.addWidget(self.f7, 2, 0, 1, 1)

        self.f8 = QLineEdit(self.gridLayoutWidget_6)
        self.f8.setObjectName(u"f8")
        self.block_F.addWidget(self.f8, 2, 1, 1, 1)

        self.f9 = QLineEdit(self.gridLayoutWidget_6)
        self.f9.setObjectName(u"f9")
        self.block_F.addWidget(self.f9, 2, 2, 1, 1)

        #Block G
        self.gridLayoutWidget_7 = QWidget(Widget)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(30, 280, 91, 89))

        self.block_G = QGridLayout(self.gridLayoutWidget_7)
        self.block_G.setObjectName(u"block_G")
        self.block_G.setContentsMargins(0, 0, 0, 0)

        self.g1 = QLineEdit(self.gridLayoutWidget_7)
        self.g1.setObjectName(u"g1")
        self.block_G.addWidget(self.g1, 0, 0, 1, 1)

        self.g2 = QLineEdit(self.gridLayoutWidget_7)
        self.g2.setObjectName(u"g2")
        self.block_G.addWidget(self.g2, 0, 1, 1, 1)

        self.g3 = QLineEdit(self.gridLayoutWidget_7)
        self.g3.setObjectName(u"g3")
        self.block_G.addWidget(self.g3, 0, 2, 1, 1)

        self.g4 = QLineEdit(self.gridLayoutWidget_7)
        self.g4.setObjectName(u"g4")
        self.block_G.addWidget(self.g4, 1, 0, 1, 1)

        self.g5 = QLineEdit(self.gridLayoutWidget_7)
        self.g5.setObjectName(u"g5")
        self.block_G.addWidget(self.g5, 1, 1, 1, 1)

        self.g6 = QLineEdit(self.gridLayoutWidget_7)
        self.g6.setObjectName(u"g6")
        self.block_G.addWidget(self.g6, 1, 2, 1, 1)

        self.g7 = QLineEdit(self.gridLayoutWidget_7)
        self.g7.setObjectName(u"g7")
        self.block_G.addWidget(self.g7, 2, 0, 1, 1)

        self.g8 = QLineEdit(self.gridLayoutWidget_7)
        self.g8.setObjectName(u"g8")
        self.block_G.addWidget(self.g8, 2, 1, 1, 1)

        self.g9 = QLineEdit(self.gridLayoutWidget_7)
        self.g9.setObjectName(u"g9")
        self.block_G.addWidget(self.g9, 2, 2, 1, 1)

        #Block H
        self.gridLayoutWidget_8 = QWidget(Widget)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(130, 280, 91, 89))

        self.block_H = QGridLayout(self.gridLayoutWidget_8)
        self.block_H.setObjectName(u"block_H")
        self.block_H.setContentsMargins(0, 0, 0, 0)

        self.h1 = QLineEdit(self.gridLayoutWidget_8)
        self.h1.setObjectName(u"h1")
        self.block_H.addWidget(self.h1, 0, 0, 1, 1)

        self.h2 = QLineEdit(self.gridLayoutWidget_8)
        self.h2.setObjectName(u"h2")
        self.block_H.addWidget(self.h2, 0, 1, 1, 1)

        self.h3 = QLineEdit(self.gridLayoutWidget_8)
        self.h3.setObjectName(u"h3")
        self.block_H.addWidget(self.h3, 0, 2, 1, 1)

        self.h4 = QLineEdit(self.gridLayoutWidget_8)
        self.h4.setObjectName(u"h4")
        self.block_H.addWidget(self.h4, 1, 0, 1, 1)

        self.h5 = QLineEdit(self.gridLayoutWidget_8)
        self.h5.setObjectName(u"h5")
        self.block_H.addWidget(self.h5, 1, 1, 1, 1)

        self.h6 = QLineEdit(self.gridLayoutWidget_8)
        self.h6.setObjectName(u"h6")
        self.block_H.addWidget(self.h6, 1, 2, 1, 1)

        self.h7 = QLineEdit(self.gridLayoutWidget_8)
        self.h7.setObjectName(u"h7")
        self.block_H.addWidget(self.h7, 2, 0, 1, 1)

        self.h8 = QLineEdit(self.gridLayoutWidget_8)
        self.h8.setObjectName(u"h8")
        self.block_H.addWidget(self.h8, 2, 1, 1, 1)

        self.h9 = QLineEdit(self.gridLayoutWidget_8)
        self.h9.setObjectName(u"h9")
        self.block_H.addWidget(self.h9, 2, 2, 1, 1)

        #Block I
        self.gridLayoutWidget_9 = QWidget(Widget)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(230, 280, 91, 89))

        self.block_I = QGridLayout(self.gridLayoutWidget_9)
        self.block_I.setObjectName(u"block_I")
        self.block_I.setContentsMargins(0, 0, 0, 0)

        self.i1 = QLineEdit(self.gridLayoutWidget_9)
        self.i1.setObjectName(u"i1")
        self.block_I.addWidget(self.i1, 0, 0, 1, 1)

        self.i2 = QLineEdit(self.gridLayoutWidget_9)
        self.i2.setObjectName(u"i2")
        self.block_I.addWidget(self.i2, 0, 1, 1, 1)

        self.i3 = QLineEdit(self.gridLayoutWidget_9)
        self.i3.setObjectName(u"i3")
        self.block_I.addWidget(self.i3, 0, 2, 1, 1)

        self.i4 = QLineEdit(self.gridLayoutWidget_9)
        self.i4.setObjectName(u"i4")
        self.block_I.addWidget(self.i4, 1, 0, 1, 1)

        self.i5 = QLineEdit(self.gridLayoutWidget_9)
        self.i5.setObjectName(u"i5")
        self.block_I.addWidget(self.i5, 1, 1, 1, 1)

        self.i6 = QLineEdit(self.gridLayoutWidget_9)
        self.i6.setObjectName(u"i6")
        self.block_I.addWidget(self.i6, 1, 2, 1, 1)

        self.i7 = QLineEdit(self.gridLayoutWidget_9)
        self.i7.setObjectName(u"i7")
        self.block_I.addWidget(self.i7, 2, 0, 1, 1)

        self.i8 = QLineEdit(self.gridLayoutWidget_9)
        self.i8.setObjectName(u"i8")
        self.block_I.addWidget(self.i8, 2, 1, 1, 1)

        self.i9 = QLineEdit(self.gridLayoutWidget_9)
        self.i9.setObjectName(u"i9")
        self.block_I.addWidget(self.i9, 2, 2, 1, 1)

        #Line separator
        self.line1 = QFrame(Widget)
        self.line1.setObjectName(u"line1")
        self.line1.setGeometry(QRect(30, 160, 291, 27))
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)

        self.line2 = QFrame(Widget)
        self.line2.setObjectName(u"line2")
        self.line2.setGeometry(QRect(30, 260, 291, 27))
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.line3 = QFrame(Widget)
        self.line3.setObjectName(u"line3")
        self.line3.setGeometry(QRect(115, 80, 20, 291))
        self.line3.setFrameShape(QFrame.VLine)
        self.line3.setFrameShadow(QFrame.Sunken)

        self.line4 = QFrame(Widget)
        self.line4.setObjectName(u"line4")
        self.line4.setGeometry(QRect(215, 80, 20, 291))
        self.line4.setFrameShape(QFrame.VLine)
        self.line4.setFrameShadow(QFrame.Sunken)

        #Solution A
        self.gridLayoutWidget_10 = QWidget(Widget)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(380, 90, 91, 81))

        self.Sol_A = QGridLayout(self.gridLayoutWidget_10)
        self.Sol_A.setSpacing(0)
        self.Sol_A.setObjectName(u"Sol_A")
        self.Sol_A.setContentsMargins(0, 0, 0, 0)

        self.a1_2 = QLabel(self.gridLayoutWidget_10)
        self.a1_2.setObjectName(u"a1_2")
        self.a1_2.setStyleSheet(cssLabel)
        self.a1_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a1_2, 0, 0, 1, 1)

        self.a2_2 = QLabel(self.gridLayoutWidget_10)
        self.a2_2.setObjectName(u"a2_2")
        self.a2_2.setStyleSheet(cssLabel)
        self.a2_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a2_2, 0, 1, 1, 1)

        self.a3_2 = QLabel(self.gridLayoutWidget_10)
        self.a3_2.setObjectName(u"a3_2")
        self.a3_2.setStyleSheet(cssLabel)
        self.a3_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a3_2, 0, 2, 1, 1)

        self.a4_2 = QLabel(self.gridLayoutWidget_10)
        self.a4_2.setObjectName(u"a4_2")
        self.a4_2.setStyleSheet(cssLabel)
        self.a4_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a4_2, 1, 0, 1, 1)

        self.a5_2 = QLabel(self.gridLayoutWidget_10)
        self.a5_2.setObjectName(u"a5_2")
        self.a5_2.setStyleSheet(cssLabel)
        self.a5_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a5_2, 1, 1, 1, 1)

        self.a6_2 = QLabel(self.gridLayoutWidget_10)
        self.a6_2.setObjectName(u"a6_2")
        self.a6_2.setStyleSheet(cssLabel)
        self.a6_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a6_2, 1, 2, 1, 1)

        self.a7_2 = QLabel(self.gridLayoutWidget_10)
        self.a7_2.setObjectName(u"a7_2")
        self.a7_2.setStyleSheet(cssLabel)
        self.a7_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a7_2, 2, 0, 1, 1)

        self.a8_2 = QLabel(self.gridLayoutWidget_10)
        self.a8_2.setObjectName(u"a8_2")
        self.a8_2.setStyleSheet(cssLabel)
        self.a8_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a8_2, 2, 1, 1, 1)

        self.a9_2 = QLabel(self.gridLayoutWidget_10)
        self.a9_2.setObjectName(u"a9_2")
        self.a9_2.setStyleSheet(cssLabel)
        self.a9_2.setAlignment(Qt.AlignCenter)
        self.Sol_A.addWidget(self.a9_2, 2, 2, 1, 1)

        #Solution B
        self.gridLayoutWidget_11 = QWidget(Widget)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(480, 90, 91, 80))

        self.Sol_B = QGridLayout(self.gridLayoutWidget_11)
        self.Sol_B.setSpacing(0)
        self.Sol_B.setObjectName(u"Sol_B")
        self.Sol_B.setContentsMargins(0, 0, 0, 0)

        self.b1_2 = QLabel(self.gridLayoutWidget_11)
        self.b1_2.setObjectName(u"b1_2")
        self.b1_2.setStyleSheet(cssLabel)
        self.b1_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b1_2, 0, 0, 1, 1)

        self.b2_2 = QLabel(self.gridLayoutWidget_11)
        self.b2_2.setObjectName(u"b2_2")
        self.b2_2.setStyleSheet(cssLabel)
        self.b2_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b2_2, 0, 1, 1, 1)

        self.b3_2 = QLabel(self.gridLayoutWidget_11)
        self.b3_2.setObjectName(u"b3_2")
        self.b3_2.setStyleSheet(cssLabel)
        self.b3_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b3_2, 0, 2, 1, 1)

        self.b4_2 = QLabel(self.gridLayoutWidget_11)
        self.b4_2.setObjectName(u"b4_2")
        self.b4_2.setStyleSheet(cssLabel)
        self.b4_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b4_2, 1, 0, 1, 1)

        self.b5_2 = QLabel(self.gridLayoutWidget_11)
        self.b5_2.setObjectName(u"b5_2")
        self.b5_2.setStyleSheet(cssLabel)
        self.b5_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b5_2, 1, 1, 1, 1)

        self.b6_2 = QLabel(self.gridLayoutWidget_11)
        self.b6_2.setObjectName(u"b6_2")
        self.b6_2.setStyleSheet(cssLabel)
        self.b6_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b6_2, 1, 2, 1, 1)

        self.b7_2 = QLabel(self.gridLayoutWidget_11)
        self.b7_2.setObjectName(u"b7_2")
        self.b7_2.setStyleSheet(cssLabel)
        self.b7_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b7_2, 2, 0, 1, 1)

        self.b8_2 = QLabel(self.gridLayoutWidget_11)
        self.b8_2.setObjectName(u"b8_2")
        self.b8_2.setStyleSheet(cssLabel)
        self.b8_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b8_2, 2, 1, 1, 1)

        self.b9_2 = QLabel(self.gridLayoutWidget_11)
        self.b9_2.setObjectName(u"b9_2")
        self.b9_2.setStyleSheet(cssLabel)
        self.b9_2.setAlignment(Qt.AlignCenter)
        self.Sol_B.addWidget(self.b9_2, 2, 2, 1, 1)

        #Solution C
        self.gridLayoutWidget_12 = QWidget(Widget)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(580, 90, 91, 80))

        self.Sol_C = QGridLayout(self.gridLayoutWidget_12)
        self.Sol_C.setSpacing(0)
        self.Sol_C.setObjectName(u"Sol_C")
        self.Sol_C.setContentsMargins(0, 0, 0, 0)

        self.c1_2 = QLabel(self.gridLayoutWidget_12)
        self.c1_2.setObjectName(u"c1_2")
        self.c1_2.setStyleSheet(cssLabel)
        self.c1_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c1_2, 0, 0, 1, 1)

        self.c2_2 = QLabel(self.gridLayoutWidget_12)
        self.c2_2.setObjectName(u"c2_2")
        self.c2_2.setStyleSheet(cssLabel)
        self.c2_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c2_2, 0, 1, 1, 1)

        self.c3_2 = QLabel(self.gridLayoutWidget_12)
        self.c3_2.setObjectName(u"c3_2")
        self.c3_2.setStyleSheet(cssLabel)
        self.c3_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c3_2, 0, 2, 1, 1)

        self.c4_2 = QLabel(self.gridLayoutWidget_12)
        self.c4_2.setObjectName(u"c4_2")
        self.c4_2.setStyleSheet(cssLabel)
        self.c4_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c4_2, 1, 0, 1, 1)

        self.c5_2 = QLabel(self.gridLayoutWidget_12)
        self.c5_2.setObjectName(u"c5_2")
        self.c5_2.setStyleSheet(cssLabel)
        self.c5_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c5_2, 1, 1, 1, 1)

        self.c6_2 = QLabel(self.gridLayoutWidget_12)
        self.c6_2.setObjectName(u"c6_2")
        self.c6_2.setStyleSheet(cssLabel)
        self.c6_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c6_2, 1, 2, 1, 1)

        self.c7_2 = QLabel(self.gridLayoutWidget_12)
        self.c7_2.setObjectName(u"c7_2")
        self.c7_2.setStyleSheet(cssLabel)
        self.c7_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c7_2, 2, 0, 1, 1)

        self.c8_2 = QLabel(self.gridLayoutWidget_12)
        self.c8_2.setObjectName(u"c8_2")
        self.c8_2.setStyleSheet(cssLabel)
        self.c8_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c8_2, 2, 1, 1, 1)

        self.c9_2 = QLabel(self.gridLayoutWidget_12)
        self.c9_2.setObjectName(u"c9_2")
        self.c9_2.setStyleSheet(cssLabel)
        self.c9_2.setAlignment(Qt.AlignCenter)
        self.Sol_C.addWidget(self.c9_2, 2, 2, 1, 1)

        #Solution D
        self.gridLayoutWidget_13 = QWidget(Widget)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(380, 180, 91, 80))

        self.Sol_D = QGridLayout(self.gridLayoutWidget_13)
        self.Sol_D.setSpacing(0)
        self.Sol_D.setObjectName(u"Sol_D")
        self.Sol_D.setContentsMargins(0, 0, 0, 0)

        self.d1_2 = QLabel(self.gridLayoutWidget_13)
        self.d1_2.setObjectName(u"d1_2")
        self.d1_2.setStyleSheet(cssLabel)
        self.d1_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d1_2, 0, 0, 1, 1)

        self.d2_2 = QLabel(self.gridLayoutWidget_13)
        self.d2_2.setObjectName(u"d2_2")
        self.d2_2.setStyleSheet(cssLabel)
        self.d2_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d2_2, 0, 1, 1, 1)

        self.d3_2 = QLabel(self.gridLayoutWidget_13)
        self.d3_2.setObjectName(u"d3_2")
        self.d3_2.setStyleSheet(cssLabel)
        self.d3_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d3_2, 0, 2, 1, 1)

        self.d4_2 = QLabel(self.gridLayoutWidget_13)
        self.d4_2.setObjectName(u"d4_2")
        self.d4_2.setStyleSheet(cssLabel)
        self.d4_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d4_2, 1, 0, 1, 1)

        self.d5_2 = QLabel(self.gridLayoutWidget_13)
        self.d5_2.setObjectName(u"d5_2")
        self.d5_2.setStyleSheet(cssLabel)
        self.d5_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d5_2, 1, 1, 1, 1)

        self.d6_2 = QLabel(self.gridLayoutWidget_13)
        self.d6_2.setObjectName(u"d6_2")
        self.d6_2.setStyleSheet(cssLabel)
        self.d6_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d6_2, 1, 2, 1, 1)

        self.d7_2 = QLabel(self.gridLayoutWidget_13)
        self.d7_2.setObjectName(u"d7_2")
        self.d7_2.setStyleSheet(cssLabel)
        self.d7_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d7_2, 2, 0, 1, 1)

        self.d8_2 = QLabel(self.gridLayoutWidget_13)
        self.d8_2.setObjectName(u"d8_2")
        self.d8_2.setStyleSheet(cssLabel)
        self.d8_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d8_2, 2, 1, 1, 1)

        self.d9_2 = QLabel(self.gridLayoutWidget_13)
        self.d9_2.setObjectName(u"d9_2")
        self.d9_2.setStyleSheet(cssLabel)
        self.d9_2.setAlignment(Qt.AlignCenter)
        self.Sol_D.addWidget(self.d9_2, 2, 2, 1, 1)

        #Solution E
        self.gridLayoutWidget_14 = QWidget(Widget)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(480, 180, 91, 80))

        self.Sol_E = QGridLayout(self.gridLayoutWidget_14)
        self.Sol_E.setSpacing(0)
        self.Sol_E.setObjectName(u"Sol_E")
        self.Sol_E.setContentsMargins(0, 0, 0, 0)

        self.e1_2 = QLabel(self.gridLayoutWidget_14)
        self.e1_2.setObjectName(u"e1_2")
        self.e1_2.setStyleSheet(cssLabel)
        self.e1_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e1_2, 0, 0, 1, 1)

        self.e2_2 = QLabel(self.gridLayoutWidget_14)
        self.e2_2.setObjectName(u"e2_3")
        self.e2_2.setStyleSheet(cssLabel)
        self.e2_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e2_2, 0, 1, 1, 1)

        self.e3_2 = QLabel(self.gridLayoutWidget_14)
        self.e3_2.setObjectName(u"e3_2")
        self.e3_2.setStyleSheet(cssLabel)
        self.e3_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e3_2, 0, 2, 1, 1)

        self.e4_2 = QLabel(self.gridLayoutWidget_14)
        self.e4_2.setObjectName(u"e4_2")
        self.e4_2.setStyleSheet(cssLabel)
        self.e4_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e4_2, 1, 0, 1, 1)

        self.e5_2 = QLabel(self.gridLayoutWidget_14)
        self.e5_2.setObjectName(u"e5_2")
        self.e5_2.setStyleSheet(cssLabel)
        self.e5_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e5_2, 1, 1, 1, 1)

        self.e6_2 = QLabel(self.gridLayoutWidget_14)
        self.e6_2.setObjectName(u"e6_2")
        self.e6_2.setStyleSheet(cssLabel)
        self.e6_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e6_2, 1, 2, 1, 1)

        self.e7_2 = QLabel(self.gridLayoutWidget_14)
        self.e7_2.setObjectName(u"e7_2")
        self.e7_2.setStyleSheet(cssLabel)
        self.e7_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e7_2, 2, 0, 1, 1)

        self.e8_2 = QLabel(self.gridLayoutWidget_14)
        self.e8_2.setObjectName(u"e8_2")
        self.e8_2.setStyleSheet(cssLabel)
        self.e8_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e8_2, 2, 1, 1, 1)

        self.e9_2 = QLabel(self.gridLayoutWidget_14)
        self.e9_2.setObjectName(u"e9_2")
        self.e9_2.setStyleSheet(cssLabel)
        self.e9_2.setAlignment(Qt.AlignCenter)
        self.Sol_E.addWidget(self.e9_2, 2, 2, 1, 1)

        #Solution F
        self.gridLayoutWidget_15 = QWidget(Widget)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(580, 180, 91, 80))

        self.Sol_F = QGridLayout(self.gridLayoutWidget_15)
        self.Sol_F.setSpacing(0)
        self.Sol_F.setObjectName(u"Sol_F")
        self.Sol_F.setContentsMargins(0, 0, 0, 0)

        self.f1_2 = QLabel(self.gridLayoutWidget_15)
        self.f1_2.setObjectName(u"f1_2")
        self.f1_2.setStyleSheet(cssLabel)
        self.f1_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f1_2, 0, 0, 1, 1)

        self.f2_2 = QLabel(self.gridLayoutWidget_15)
        self.f2_2.setObjectName(u"f2_2")
        self.f2_2.setStyleSheet(cssLabel)
        self.f2_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f2_2, 0, 1, 1, 1)

        self.f3_2 = QLabel(self.gridLayoutWidget_15)
        self.f3_2.setObjectName(u"f3_2")
        self.f3_2.setStyleSheet(cssLabel)
        self.f3_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f3_2, 0, 2, 1, 1)

        self.f4_2 = QLabel(self.gridLayoutWidget_15)
        self.f4_2.setObjectName(u"f4_2")
        self.f4_2.setStyleSheet(cssLabel)
        self.f4_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f4_2, 1, 0, 1, 1)

        self.f5_2 = QLabel(self.gridLayoutWidget_15)
        self.f5_2.setObjectName(u"f5_2")
        self.f5_2.setStyleSheet(cssLabel)
        self.f5_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f5_2, 1, 1, 1, 1)

        self.f6_2 = QLabel(self.gridLayoutWidget_15)
        self.f6_2.setObjectName(u"f6_2")
        self.f6_2.setStyleSheet(cssLabel)
        self.f6_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f6_2, 1, 2, 1, 1)

        self.f7_2 = QLabel(self.gridLayoutWidget_15)
        self.f7_2.setObjectName(u"f7_2")
        self.f7_2.setStyleSheet(cssLabel)
        self.f7_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f7_2, 2, 0, 1, 1)

        self.f8_2 = QLabel(self.gridLayoutWidget_15)
        self.f8_2.setObjectName(u"f8_2")
        self.f8_2.setStyleSheet(cssLabel)
        self.f8_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f8_2, 2, 1, 1, 1)

        self.f9_2 = QLabel(self.gridLayoutWidget_15)
        self.f9_2.setObjectName(u"f9_2")
        self.f9_2.setStyleSheet(cssLabel)
        self.f9_2.setAlignment(Qt.AlignCenter)
        self.Sol_F.addWidget(self.f9_2, 2, 2, 1, 1)

        #Solution G
        self.gridLayoutWidget_16 = QWidget(Widget)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(380, 270, 91, 80))

        self.Sol_G = QGridLayout(self.gridLayoutWidget_16)
        self.Sol_G.setSpacing(0)
        self.Sol_G.setObjectName(u"Sol_G")
        self.Sol_G.setContentsMargins(0, 0, 0, 0)

        self.g1_2 = QLabel(self.gridLayoutWidget_16)
        self.g1_2.setObjectName(u"g1_2")
        self.g1_2.setStyleSheet(cssLabel)
        self.g1_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g1_2, 0, 0, 1, 1)

        self.g2_2 = QLabel(self.gridLayoutWidget_16)
        self.g2_2.setObjectName(u"g2_2")
        self.g2_2.setStyleSheet(cssLabel)
        self.g2_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g2_2, 0, 1, 1, 1)

        self.g3_2 = QLabel(self.gridLayoutWidget_16)
        self.g3_2.setObjectName(u"g3_2")
        self.g3_2.setStyleSheet(cssLabel)
        self.g3_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g3_2, 0, 2, 1, 1)

        self.g4_2 = QLabel(self.gridLayoutWidget_16)
        self.g4_2.setObjectName(u"g4_2")
        self.g4_2.setStyleSheet(cssLabel)
        self.g4_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g4_2, 1, 0, 1, 1)

        self.g5_2 = QLabel(self.gridLayoutWidget_16)
        self.g5_2.setObjectName(u"g5_2")
        self.g5_2.setStyleSheet(cssLabel)
        self.g5_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g5_2, 1, 1, 1, 1)

        self.g6_2 = QLabel(self.gridLayoutWidget_16)
        self.g6_2.setObjectName(u"g6_2")
        self.g6_2.setStyleSheet(cssLabel)
        self.g6_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g6_2, 1, 2, 1, 1)

        self.g7_2 = QLabel(self.gridLayoutWidget_16)
        self.g7_2.setObjectName(u"g7_2")
        self.g7_2.setStyleSheet(cssLabel)
        self.g7_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g7_2, 2, 0, 1, 1)

        self.g8_2 = QLabel(self.gridLayoutWidget_16)
        self.g8_2.setObjectName(u"g8_2")
        self.g8_2.setStyleSheet(cssLabel)
        self.g8_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g8_2, 2, 1, 1, 1)

        self.g9_2 = QLabel(self.gridLayoutWidget_16)
        self.g9_2.setObjectName(u"g9_2")
        self.g9_2.setStyleSheet(cssLabel)
        self.g9_2.setAlignment(Qt.AlignCenter)
        self.Sol_G.addWidget(self.g9_2, 2, 2, 1, 1)

        #Solution H
        self.gridLayoutWidget_17 = QWidget(Widget)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(480, 270, 91, 80))

        self.Sol_H = QGridLayout(self.gridLayoutWidget_17)
        self.Sol_H.setSpacing(0)
        self.Sol_H.setObjectName(u"Sol_H")
        self.Sol_H.setContentsMargins(0, 0, 0, 0)

        self.h1_2 = QLabel(self.gridLayoutWidget_17)
        self.h1_2.setObjectName(u"h1_2")
        self.h1_2.setStyleSheet(cssLabel)
        self.h1_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h1_2, 0, 0, 1, 1)

        self.h2_2 = QLabel(self.gridLayoutWidget_17)
        self.h2_2.setObjectName(u"h2_2")
        self.h2_2.setStyleSheet(cssLabel)
        self.h2_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h2_2, 0, 1, 1, 1)

        self.h3_2 = QLabel(self.gridLayoutWidget_17)
        self.h3_2.setObjectName(u"h3_2")
        self.h3_2.setStyleSheet(cssLabel)
        self.h3_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h3_2, 0, 2, 1, 1)

        self.h4_2 = QLabel(self.gridLayoutWidget_17)
        self.h4_2.setObjectName(u"h4_2")
        self.h4_2.setStyleSheet(cssLabel)
        self.h4_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h4_2, 1, 0, 1, 1)

        self.h5_2 = QLabel(self.gridLayoutWidget_17)
        self.h5_2.setObjectName(u"h5_2")
        self.h5_2.setStyleSheet(cssLabel)
        self.h5_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h5_2, 1, 1, 1, 1)

        self.h6_2 = QLabel(self.gridLayoutWidget_17)
        self.h6_2.setObjectName(u"h6_2")
        self.h6_2.setStyleSheet(cssLabel)
        self.h6_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h6_2, 1, 2, 1, 1)

        self.h7_2 = QLabel(self.gridLayoutWidget_17)
        self.h7_2.setObjectName(u"h7_2")
        self.h7_2.setStyleSheet(cssLabel)
        self.h7_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h7_2, 2, 0, 1, 1)

        self.h8_2 = QLabel(self.gridLayoutWidget_17)
        self.h8_2.setObjectName(u"h8_2")
        self.h8_2.setStyleSheet(cssLabel)
        self.h8_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h8_2, 2, 1, 1, 1)

        self.h9_2 = QLabel(self.gridLayoutWidget_17)
        self.h9_2.setObjectName(u"h9_2")
        self.h9_2.setStyleSheet(cssLabel)
        self.h9_2.setAlignment(Qt.AlignCenter)
        self.Sol_H.addWidget(self.h9_2, 2, 2, 1, 1)

        #Solution I
        self.gridLayoutWidget_18 = QWidget(Widget)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(580, 270, 91, 80))

        self.Sol_I = QGridLayout(self.gridLayoutWidget_18)
        self.Sol_I.setSpacing(0)
        self.Sol_I.setObjectName(u"Sol_H_2")
        self.Sol_I.setContentsMargins(0, 0, 0, 0)

        self.i1_2 = QLabel(self.gridLayoutWidget_18)
        self.i1_2.setObjectName(u"i1_2")
        self.i1_2.setStyleSheet(cssLabel)
        self.i1_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i1_2, 0, 0, 1, 1)

        self.i2_2 = QLabel(self.gridLayoutWidget_18)
        self.i2_2.setObjectName(u"i2_2")
        self.i2_2.setStyleSheet(cssLabel)
        self.i2_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i2_2, 0, 1, 1, 1)

        self.i3_2 = QLabel(self.gridLayoutWidget_18)
        self.i3_2.setObjectName(u"i3_2")
        self.i3_2.setStyleSheet(cssLabel)
        self.i3_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i3_2, 0, 2, 1, 1)

        self.i4_2 = QLabel(self.gridLayoutWidget_18)
        self.i4_2.setObjectName(u"i4_2")
        self.i4_2.setStyleSheet(cssLabel)
        self.i4_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i4_2, 1, 0, 1, 1)

        self.i5_2 = QLabel(self.gridLayoutWidget_18)
        self.i5_2.setObjectName(u"i5_2")
        self.i5_2.setStyleSheet(cssLabel)
        self.i5_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i5_2, 1, 1, 1, 1)

        self.i6_2 = QLabel(self.gridLayoutWidget_18)
        self.i6_2.setObjectName(u"i6_2")
        self.i6_2.setStyleSheet(cssLabel)
        self.i6_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i6_2, 1, 2, 1, 1)

        self.i7_2 = QLabel(self.gridLayoutWidget_18)
        self.i7_2.setObjectName(u"i7_2")
        self.i7_2.setStyleSheet(cssLabel)
        self.i7_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i7_2, 2, 0, 1, 1)

        self.i8_2 = QLabel(self.gridLayoutWidget_18)
        self.i8_2.setObjectName(u"i8_2")
        self.i8_2.setStyleSheet(cssLabel)
        self.i8_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i8_2, 2, 1, 1, 1)

        self.i9_2 = QLabel(self.gridLayoutWidget_18)
        self.i9_2.setObjectName(u"i9_2")
        self.i9_2.setStyleSheet(cssLabel)
        self.i9_2.setAlignment(Qt.AlignCenter)
        self.Sol_I.addWidget(self.i9_2, 2, 2, 1, 1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"SUDOKU SOLVER", None))
        self.titleLabel.setText(QCoreApplication.translate("Widget", u"SUDOKU SOLVER", None))
        self.solveButton.setText(QCoreApplication.translate("Widget", u"SOLVE", None))
        self.cancelBotton.setText(QCoreApplication.translate("Widget", u"CANCEL", None))
    # retranslateUi
