
from PyQt5 import QtCore, QtGui, QtWidgets
from functions import SwitchScreen
from functools import partial
from home_news_functions import HomeNews
from media_function import MediaChannels
from weather_function import Weather
from searchtab_function import Search, HistorySearch
from category_function import CategoryNews
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.side_bar_background = QtWidgets.QLabel(self.centralwidget)
        self.side_bar_background.setGeometry(QtCore.QRect(-10, -10, 171, 801))
        self.side_bar_background.setStyleSheet("background-color: rgb(65, 105, 236);")
        self.side_bar_background.setText("")
        self.side_bar_background.setObjectName("side_bar_background")
        self.main_background = QtWidgets.QLabel(self.centralwidget)
        self.main_background.setGeometry(QtCore.QRect(70, -10, 1221, 791))
        self.main_background.setStyleSheet("background-color: rgb(255, 247, 212);\n"
                                           "border-radius: 40px;")
        self.main_background.setText("")
        self.main_background.setObjectName("main_background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 410, 521, 161))
        self.label.setText("")
        self.label.setObjectName("label")
        self.home_icon = QtWidgets.QPushButton(self.centralwidget)
        self.home_icon.setGeometry(QtCore.QRect(15, 20, 41, 41))
        self.home_icon.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.home_icon.setStyleSheet("QPushButton\n"
                                     "{\n"
                                     "    background-color: rgb(65, 105, 236);\n"
                                     "    border: 2px rgb(255, 255, 255);\n"
                                     "    border-radius: 10px;\n"
                                     "    \n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:pressed\n"
                                     "{\n"
                                     "    background-color: rgb(33, 58, 95);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    \n"
                                     "    background-color: rgb(33, 58, 95);\n"
                                     "\n"
                                     "}\n"
                                     "")
        self.home_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/newspaper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_icon.setIcon(icon)
        self.home_icon.setIconSize(QtCore.QSize(50, 50))
        self.home_icon.setFlat(False)
        self.home_icon.setObjectName("home_icon")
        self.search_side_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_side_button.setGeometry(QtCore.QRect(15, 160, 41, 41))
        self.search_side_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.search_side_button.setStyleSheet("QPushButton\n"
                                              "{\n"
                                              "    background-color: rgb(65, 105, 236);\n"
                                              "    border: 2px rgb(255, 255, 255);\n"
                                              "    border-radius: 10px;\n"
                                              "    \n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "QPushButton:pressed\n"
                                              "{\n"
                                              "    background-color: rgb(33, 58, 95);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    \n"
                                              "    background-color: rgb(33, 58, 95);\n"
                                              "\n"
                                              "}\n"
                                              "")
        self.search_side_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/side_tab_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_side_button.setIcon(icon1)
        self.search_side_button.setIconSize(QtCore.QSize(50, 50))
        self.search_side_button.setFlat(False)
        self.search_side_button.setObjectName("search_side_button")
        self.category_side_button = QtWidgets.QPushButton(self.centralwidget)
        self.category_side_button.setGeometry(QtCore.QRect(15, 260, 41, 41))
        self.category_side_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.category_side_button.setStyleSheet("QPushButton\n"
                                                "{\n"
                                                "    background-color: rgb(65, 105, 236);\n"
                                                "    border: 2px rgb(255, 255, 255);\n"
                                                "    border-radius: 10px;\n"
                                                "    \n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "QPushButton:pressed\n"
                                                "{\n"
                                                "    background-color: rgb(33, 58, 95);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    \n"
                                                "    background-color: rgb(33, 58, 95);\n"
                                                "\n"
                                                "}\n"
                                                "")
        self.category_side_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/news_items.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.category_side_button.setIcon(icon2)
        self.category_side_button.setIconSize(QtCore.QSize(50, 50))
        self.category_side_button.setFlat(False)
        self.category_side_button.setObjectName("category_side_button")
        self.media_side_button = QtWidgets.QPushButton(self.centralwidget)
        self.media_side_button.setGeometry(QtCore.QRect(15, 360, 41, 41))
        self.media_side_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.media_side_button.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    background-color: rgb(65, 105, 236);\n"
                                             "    border: 2px rgb(255, 255, 255);\n"
                                             "    border-radius: 10px;\n"
                                             "    \n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "QPushButton:pressed\n"
                                             "{\n"
                                             "    background-color: rgb(33, 58, 95);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    \n"
                                             "    background-color: rgb(33, 58, 95);\n"
                                             "\n"
                                             "}\n"
                                             "")
        self.media_side_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/media_tab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.media_side_button.setIcon(icon3)
        self.media_side_button.setIconSize(QtCore.QSize(50, 50))
        self.media_side_button.setFlat(False)
        self.media_side_button.setObjectName("media_side_button")
        self.weather_side_button = QtWidgets.QPushButton(self.centralwidget)
        self.weather_side_button.setGeometry(QtCore.QRect(15, 460, 41, 41))
        self.weather_side_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.weather_side_button.setStyleSheet("QPushButton\n"
                                               "{\n"
                                               "    background-color: rgb(65, 105, 236);\n"
                                               "    border: 2px rgb(255, 255, 255);\n"
                                               "    border-radius: 10px;\n"
                                               "    \n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "QPushButton:pressed\n"
                                               "{\n"
                                               "    background-color: rgb(33, 58, 95);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    \n"
                                               "    background-color: rgb(33, 58, 95);\n"
                                               "\n"
                                               "}\n"
                                               "")
        self.weather_side_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/weather_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_side_button.setIcon(icon4)
        self.weather_side_button.setIconSize(QtCore.QSize(50, 50))
        self.weather_side_button.setFlat(False)
        self.weather_side_button.setObjectName("weather_side_button")
        self.divider = QtWidgets.QLabel(self.centralwidget)
        self.divider.setGeometry(QtCore.QRect(15, 220, 47, 13))
        self.divider.setStyleSheet("color: rgb(57, 94, 206);")
        self.divider.setObjectName("divider")
        self.divider_2 = QtWidgets.QLabel(self.centralwidget)
        self.divider_2.setGeometry(QtCore.QRect(15, 320, 47, 13))
        self.divider_2.setStyleSheet("color: rgb(57, 94, 206);")
        self.divider_2.setObjectName("divider_2")
        self.divider_3 = QtWidgets.QLabel(self.centralwidget)
        self.divider_3.setGeometry(QtCore.QRect(15, 420, 47, 13))
        self.divider_3.setStyleSheet("color: rgb(57, 94, 206);")
        self.divider_3.setObjectName("divider_3")
        self.divider_4 = QtWidgets.QLabel(self.centralwidget)
        self.divider_4.setGeometry(QtCore.QRect(15, 520, 47, 13))
        self.divider_4.setStyleSheet("color: rgb(57, 94, 206);")
        self.divider_4.setObjectName("divider_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(70, -20, 1131, 841))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 247, 212);\n"
                                     "")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.home_news_list = QtWidgets.QListWidget(self.home_tab)
        self.home_news_list.setGeometry(QtCore.QRect(30, 50, 1061, 701))
        self.home_news_list.setIconSize(QtCore.QSize(200, 200)) # size of news icon

        self.home_news_list.setStyleSheet(
            "QListWidget { background-color: rgb(255, 255, 255); color: rgb(117, 117, 117); font: 15pt \"Century Gothic\"; border: 2px rgb(255, 255, 255); } QScrollBar:vertical { border: none; background: rgb(65, 105, 236); width: 14px; margin: 15px 0 15px 0; border-radius: 0px; } QScrollBar::handle:vertical { background-color: rgb(43, 71, 156); min-height: 30px; border-radius: 7px; } QScrollBar::handle:vertical:hover{ background-color: rgb(198, 198, 198); } QScrollBar::handle:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::sub-line:vertical { border: none; background-color:  rgb(65, 105, 236); height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::add-line:vertical { border: none; background-color: rgb(65, 105, 236); height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::add-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }")

        self.home_news_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.home_news_list.setObjectName("home_news_list")
        item = QtWidgets.QListWidgetItem()
        self.home_news_list.addItem(item)
        self.white_backgroundhome = QtWidgets.QLabel(self.home_tab)
        self.white_backgroundhome.setGeometry(QtCore.QRect(10, 30, 1101, 741))
        self.white_backgroundhome.setStyleSheet("background-color: white;\n"
                                                "border: 2px rgb(255, 255, 255);\n"
                                                "border-radius: 30px;\n"
                                                "")
        self.white_backgroundhome.setText("")
        self.white_backgroundhome.setObjectName("white_backgroundhome")
        self.white_backgroundhome.raise_()
        self.home_news_list.raise_()
        self.tabWidget.addTab(self.home_tab, "")
        self.search_tab = QtWidgets.QWidget()
        self.search_tab.setObjectName("search_tab")
        self.search_button = QtWidgets.QPushButton(self.search_tab)
        self.search_button.setGeometry(QtCore.QRect(340, 35, 41, 41))
        self.search_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.search_button.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    border: 2px rgb(255, 255, 255);\n"
                                         "    border-radius: 10px;\n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    \n"
                                         "    background-color: rgb(238, 238, 238);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed\n"
                                         "{\n"
                                         "    background-color: rgb(238, 238, 238);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.search_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/search-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon5)
        self.search_button.setIconSize(QtCore.QSize(50, 50))
        self.search_button.setFlat(False)
        self.search_button.setObjectName("search_button")
        self.spacer = QtWidgets.QLabel(self.search_tab)
        self.spacer.setGeometry(QtCore.QRect(20, 35, 41, 41))
        self.spacer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spacer.setStyleSheet("background-color: white;\n"
                                  "border: 2px rgb(255, 255, 255);\n"
                                  "border-radius: 10px;\n"
                                  "\n"
                                  "\n"
                                  "\n"
                                  "")
        self.spacer.setText("")
        self.spacer.setPixmap(QtGui.QPixmap("../../../Downloads/icons/search_bar_icon.png"))
        self.spacer.setObjectName("spacer")
        self.search_bar = QtWidgets.QLineEdit(self.search_tab)
        self.search_bar.setGeometry(QtCore.QRect(40, 35, 311, 41))
        self.search_bar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.search_bar.setStyleSheet("background-color: white;\n"
                                      "color: rgb(26, 46, 75);\n"
                                      "font: 12pt \"Century Gothic\";\n"
                                      "border: 2px rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "")
        self.search_bar.setObjectName("search_bar")
        self.white_backgroundhome_2 = QtWidgets.QLabel(self.search_tab)
        self.white_backgroundhome_2.setGeometry(QtCore.QRect(40, 100, 1031, 231))
        self.white_backgroundhome_2.setStyleSheet("background-color: white;\n"
                                                  "border: 2px rgb(255, 255, 255);\n"
                                                  "border-radius: 30px;\n"
                                                  "")
        self.white_backgroundhome_2.setText("")
        self.white_backgroundhome_2.setObjectName("white_backgroundhome_2")
        self.popular_label = QtWidgets.QLabel(self.search_tab)
        self.popular_label.setGeometry(QtCore.QRect(60, 110, 161, 51))
        self.popular_label.setStyleSheet("font: 75 25pt \"Century Gothic\";\n"
                                         "background-color: rgb(255, 255, 255);")
        self.popular_label.setObjectName("popular_label")
        self.popular1 = QtWidgets.QPushButton(self.search_tab)
        self.popular1.setGeometry(QtCore.QRect(90, 190, 181, 41))
        self.popular1.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular1.setObjectName("popular1")
        self.popular5 = QtWidgets.QPushButton(self.search_tab)
        self.popular5.setGeometry(QtCore.QRect(90, 270, 181, 41))
        self.popular5.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular5.setObjectName("popular5")
        self.popular2 = QtWidgets.QPushButton(self.search_tab)
        self.popular2.setGeometry(QtCore.QRect(330, 190, 181, 41))
        self.popular2.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular2.setObjectName("popular2")
        self.popular6 = QtWidgets.QPushButton(self.search_tab)
        self.popular6.setGeometry(QtCore.QRect(330, 270, 181, 41))
        self.popular6.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular6.setObjectName("popular6")
        self.popular3 = QtWidgets.QPushButton(self.search_tab)
        self.popular3.setGeometry(QtCore.QRect(570, 190, 181, 41))
        self.popular3.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular3.setObjectName("popular3")
        self.popular7 = QtWidgets.QPushButton(self.search_tab)
        self.popular7.setGeometry(QtCore.QRect(570, 270, 181, 41))
        self.popular7.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular7.setObjectName("popular7")
        self.popular4 = QtWidgets.QPushButton(self.search_tab)
        self.popular4.setGeometry(QtCore.QRect(820, 190, 181, 41))
        self.popular4.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular4.setObjectName("popular4")
        self.popular8 = QtWidgets.QPushButton(self.search_tab)
        self.popular8.setGeometry(QtCore.QRect(820, 270, 181, 41))
        self.popular8.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: rgb(88, 88, 88);\n"
                                    "    background-color: rgb(227, 241, 244);\n"
                                    "    border :2px solid lightblue;\n"
                                    "    border-radius: 8px;\n"
                                    "\n"
                                    "    \n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed\n"
                                    "{\n"
                                    "    background-color: rgb(198, 210, 213);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.popular8.setObjectName("popular8")
        self.white_backgroundhome_3 = QtWidgets.QLabel(self.search_tab)
        self.white_backgroundhome_3.setGeometry(QtCore.QRect(20, 350, 1091, 421))
        self.white_backgroundhome_3.setStyleSheet("background-color: white;\n"
                                                  "border: 2px rgb(255, 255, 255);\n"
                                                  "border-radius: 30px;\n"
                                                  "")
        self.white_backgroundhome_3.setText("")
        self.white_backgroundhome_3.setObjectName("white_backgroundhome_3")
        self.divider_5 = QtWidgets.QLabel(self.search_tab)
        self.divider_5.setGeometry(QtCore.QRect(40, 156, 1031, 21))
        self.divider_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(225, 225, 225)")
        self.divider_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.divider_5.setObjectName("divider_5")
        self.history_label = QtWidgets.QLabel(self.search_tab)
        self.history_label.setGeometry(QtCore.QRect(40, 360, 161, 51))
        self.history_label.setStyleSheet("font: 75 25pt \"Century Gothic\";\n"
                                         "background-color: rgb(255, 255, 255);")
        self.history_label.setObjectName("history_label")
        self.divider_6 = QtWidgets.QLabel(self.search_tab)
        self.divider_6.setGeometry(QtCore.QRect(20, 410, 1091, 21))
        self.divider_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(225, 225, 225)")
        self.divider_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.divider_6.setObjectName("divider_6")
        self.history_search_list = QtWidgets.QListWidget(self.search_tab)
        self.history_search_list.setGeometry(QtCore.QRect(40, 430, 1061, 321))
        self.history_search_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "color: rgb(117, 117, 117);\n"
                                               "font: 15pt \"Century Gothic\";\n"
                                               "border: 2px rgb(255, 255, 255);\n"
                                               "\n"
                                               "")
        self.history_search_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history_search_list.setViewMode(QtWidgets.QListView.ListMode)
        self.history_search_list.setObjectName("history_search_list")
        self.spacer.raise_()
        self.search_bar.raise_()
        self.search_button.raise_()
        self.white_backgroundhome_2.raise_()
        self.popular_label.raise_()
        self.popular1.raise_()
        self.popular5.raise_()
        self.popular2.raise_()
        self.popular6.raise_()
        self.popular3.raise_()
        self.popular7.raise_()
        self.popular4.raise_()
        self.popular8.raise_()
        self.white_backgroundhome_3.raise_()
        self.divider_5.raise_()
        self.history_label.raise_()
        self.divider_6.raise_()
        self.history_search_list.raise_()
        self.tabWidget.addTab(self.search_tab, "")
        self.category_tab = QtWidgets.QWidget()
        self.category_tab.setObjectName("category_tab")
        self.politics_img = QtWidgets.QLabel(self.category_tab)
        self.politics_img.setGeometry(QtCore.QRect(0, 10, 1131, 101))
        self.politics_img.setText("")
        self.politics_img.setPixmap(QtGui.QPixmap("icons/politics_ic.jpg"))
        self.politics_img.setObjectName("politics_img")
        self.politics_button = QtWidgets.QPushButton(self.category_tab)
        self.politics_button.setGeometry(QtCore.QRect(-6, 12, 1131, 101))
        self.politics_button.setStyleSheet("QPushButton\n"
                                           "{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    font: 25pt \"Century Gothic\";\n"
                                           "    background-color: rgba(255, 255, 255, 0);\n"
                                           "    border: 2px;\n"
                                           "\n"
                                           "    \n"
                                           "    \n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "\n"
                                           "    background-color: rgba(50, 50, 50, 50);\n"
                                           "\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    background-color: rgba(65, 105, 236, 50);\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "")
        self.politics_button.setAutoDefault(False)
        self.politics_button.setDefault(False)
        self.politics_button.setFlat(False)
        self.politics_button.setObjectName("politics_button")
        self.business_img = QtWidgets.QLabel(self.category_tab)
        self.business_img.setGeometry(QtCore.QRect(-4, 120, 1131, 101))
        self.business_img.setText("")
        self.business_img.setPixmap(QtGui.QPixmap("icons/busines_img.jpg"))
        self.business_img.setScaledContents(False)
        self.business_img.setObjectName("business_img")
        self.business_button = QtWidgets.QPushButton(self.category_tab)
        self.business_button.setGeometry(QtCore.QRect(-10, 120, 1131, 101))
        self.business_button.setStyleSheet("QPushButton\n"
                                           "{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    font: 25pt \"Century Gothic\";\n"
                                           "    background-color: rgba(255, 255, 255, 0);\n"
                                           "    border: 2px;\n"
                                           "\n"
                                           "    \n"
                                           "    \n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "\n"
                                           "    background-color: rgba(50, 50, 50, 50);\n"
                                           "\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    background-color: rgba(65, 105, 236, 50);\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "")
        self.business_button.setAutoDefault(False)
        self.business_button.setDefault(False)
        self.business_button.setFlat(False)
        self.business_button.setObjectName("business_button")
        self.sports_img = QtWidgets.QLabel(self.category_tab)
        self.sports_img.setGeometry(QtCore.QRect(0, 230, 1131, 101))
        self.sports_img.setText("")
        self.sports_img.setPixmap(QtGui.QPixmap("icons/sports_ic.jpg"))
        self.sports_img.setScaledContents(False)
        self.sports_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.sports_img.setObjectName("sports_img")
        self.sports_button = QtWidgets.QPushButton(self.category_tab)
        self.sports_button.setGeometry(QtCore.QRect(-6, 230, 1131, 101))
        self.sports_button.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    font: 25pt \"Century Gothic\";\n"
                                         "    background-color: rgba(255, 255, 255, 0);\n"
                                         "    border: 2px;\n"
                                         "\n"
                                         "    \n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "\n"
                                         "    background-color: rgba(50, 50, 50, 50);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed\n"
                                         "{\n"
                                         "    background-color: rgba(65, 105, 236, 50);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.sports_button.setAutoDefault(False)
        self.sports_button.setDefault(False)
        self.sports_button.setFlat(False)
        self.sports_button.setObjectName("sports_button")
        self.technology_button = QtWidgets.QPushButton(self.category_tab)
        self.technology_button.setGeometry(QtCore.QRect(-16, 340, 1131, 101))
        self.technology_button.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    font: 25pt \"Century Gothic\";\n"
                                             "    background-color: rgba(255, 255, 255, 0);\n"
                                             "    border: 2px;\n"
                                             "\n"
                                             "    \n"
                                             "    \n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "\n"
                                             "    background-color: rgba(50, 50, 50, 50);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed\n"
                                             "{\n"
                                             "    background-color: rgba(65, 105, 236, 50);\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "")
        self.technology_button.setAutoDefault(False)
        self.technology_button.setDefault(False)
        self.technology_button.setFlat(False)
        self.technology_button.setObjectName("technology_button")
        self.technology_img = QtWidgets.QLabel(self.category_tab)
        self.technology_img.setGeometry(QtCore.QRect(-10, 340, 1131, 101))
        self.technology_img.setText("")
        self.technology_img.setPixmap(QtGui.QPixmap("icons/tech_img.jpg"))
        self.technology_img.setScaledContents(False)
        self.technology_img.setAlignment(QtCore.Qt.AlignCenter)
        self.technology_img.setObjectName("technology_img")
        self.health_img = QtWidgets.QLabel(self.category_tab)
        self.health_img.setGeometry(QtCore.QRect(0, 450, 1131, 101))
        self.health_img.setText("")
        self.health_img.setPixmap(QtGui.QPixmap("icons/health_img.jpg"))
        self.health_img.setScaledContents(False)
        self.health_img.setAlignment(QtCore.Qt.AlignCenter)
        self.health_img.setObjectName("health_img")
        self.health_button = QtWidgets.QPushButton(self.category_tab)
        self.health_button.setGeometry(QtCore.QRect(-6, 450, 1131, 101))
        self.health_button.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    font: 25pt \"Century Gothic\";\n"
                                         "    background-color: rgba(255, 255, 255, 0);\n"
                                         "    border: 2px;\n"
                                         "\n"
                                         "    \n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "\n"
                                         "    background-color: rgba(50, 50, 50, 50);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed\n"
                                         "{\n"
                                         "    background-color: rgba(65, 105, 236, 50);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.health_button.setAutoDefault(False)
        self.health_button.setDefault(False)
        self.health_button.setFlat(False)
        self.health_button.setObjectName("health_button")
        self.education_img = QtWidgets.QLabel(self.category_tab)
        self.education_img.setGeometry(QtCore.QRect(-4, 560, 1131, 101))
        self.education_img.setText("")
        self.education_img.setPixmap(QtGui.QPixmap("icons/education_img.jpg"))
        self.education_img.setScaledContents(False)
        self.education_img.setAlignment(QtCore.Qt.AlignCenter)
        self.education_img.setObjectName("education_img")
        self.education_button = QtWidgets.QPushButton(self.category_tab)
        self.education_button.setGeometry(QtCore.QRect(-10, 560, 1131, 101))
        self.education_button.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    font: 25pt \"Century Gothic\";\n"
                                            "    background-color: rgba(255, 255, 255, 0);\n"
                                            "    border: 2px;\n"
                                            "\n"
                                            "    \n"
                                            "    \n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "\n"
                                            "    background-color: rgba(50, 50, 50, 50);\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    background-color: rgba(65, 105, 236, 50);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "")
        self.education_button.setAutoDefault(False)
        self.education_button.setDefault(False)
        self.education_button.setFlat(False)
        self.education_button.setObjectName("education_button")
        self.fashion_img = QtWidgets.QLabel(self.category_tab)
        self.fashion_img.setGeometry(QtCore.QRect(0, 670, 1131, 111))
        self.fashion_img.setText("")
        self.fashion_img.setPixmap(QtGui.QPixmap("icons/clothes_img.jpg"))
        self.fashion_img.setScaledContents(False)
        self.fashion_img.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.fashion_img.setObjectName("fashion_img")
        self.fashion_button = QtWidgets.QPushButton(self.category_tab)
        self.fashion_button.setGeometry(QtCore.QRect(-6, 670, 1131, 111))
        self.fashion_button.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    font: 25pt \"Century Gothic\";\n"
                                          "    background-color: rgba(255, 255, 255, 0);\n"
                                          "    border: 2px;\n"
                                          "\n"
                                          "    \n"
                                          "    \n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "\n"
                                          "    background-color: rgba(50, 50, 50, 50);\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed\n"
                                          "{\n"
                                          "    background-color: rgba(65, 105, 236, 50);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.fashion_button.setAutoDefault(False)
        self.fashion_button.setDefault(False)
        self.fashion_button.setFlat(False)
        self.fashion_button.setObjectName("fashion_button")
        self.politics_img.raise_()
        self.politics_button.raise_()
        self.business_img.raise_()
        self.business_button.raise_()
        self.sports_img.raise_()
        self.sports_button.raise_()
        self.technology_img.raise_()
        self.technology_button.raise_()
        self.health_img.raise_()
        self.health_button.raise_()
        self.education_img.raise_()
        self.education_button.raise_()
        self.fashion_img.raise_()
        self.fashion_button.raise_()
        self.tabWidget.addTab(self.category_tab, "")
        self.media_tab = QtWidgets.QWidget()
        self.media_tab.setObjectName("media_tab")
        self.white_backgroundnews = QtWidgets.QLabel(self.media_tab)
        self.white_backgroundnews.setGeometry(QtCore.QRect(20, 30, 1081, 741))
        self.white_backgroundnews.setStyleSheet("background-color: white;\n"
                                                "border: 2px rgb(255, 255, 255);\n"
                                                "border-radius: 30px;\n"
                                                "")
        self.white_backgroundnews.setText("")
        self.white_backgroundnews.setObjectName("white_backgroundnews")
        self.news_channel1 = QtWidgets.QLabel(self.media_tab)
        self.news_channel1.setGeometry(QtCore.QRect(50, 50, 241, 221))
        self.news_channel1.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel1.setText("")
        self.news_channel1.setPixmap(QtGui.QPixmap("icons/abc_news.jpg"))
        self.news_channel1.setScaledContents(True)
        self.news_channel1.setObjectName("news_channel1")
        self.news_channel5 = QtWidgets.QLabel(self.media_tab)
        self.news_channel5.setGeometry(QtCore.QRect(50, 290, 241, 221))
        self.news_channel5.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel5.setText("")
        self.news_channel5.setPixmap(QtGui.QPixmap("icons/bbc_news.jpg"))
        self.news_channel5.setScaledContents(True)
        self.news_channel5.setObjectName("news_channel5")
        self.news_channel9 = QtWidgets.QLabel(self.media_tab)
        self.news_channel9.setGeometry(QtCore.QRect(50, 530, 241, 221))
        self.news_channel9.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel9.setText("")
        self.news_channel9.setPixmap(QtGui.QPixmap("icons/arabiya_news.png"))
        self.news_channel9.setScaledContents(True)
        self.news_channel9.setObjectName("news_channel9")
        self.news_channel2 = QtWidgets.QLabel(self.media_tab)
        self.news_channel2.setGeometry(QtCore.QRect(310, 50, 241, 221))
        self.news_channel2.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel2.setText("")
        self.news_channel2.setPixmap(QtGui.QPixmap("icons/cbsnews.png"))
        self.news_channel2.setScaledContents(True)
        self.news_channel2.setObjectName("news_channel2")
        self.news_channel6 = QtWidgets.QLabel(self.media_tab)
        self.news_channel6.setGeometry(QtCore.QRect(310, 290, 241, 221))
        self.news_channel6.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel6.setText("")
        self.news_channel6.setPixmap(QtGui.QPixmap("icons/skynews.png"))
        self.news_channel6.setScaledContents(True)
        self.news_channel6.setObjectName("news_channel6")
        self.news_channel10 = QtWidgets.QLabel(self.media_tab)
        self.news_channel10.setGeometry(QtCore.QRect(310, 530, 241, 221))
        self.news_channel10.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                          "")
        self.news_channel10.setText("")
        self.news_channel10.setPixmap(QtGui.QPixmap("icons/alazera_img.jpg"))
        self.news_channel10.setScaledContents(True)
        self.news_channel10.setObjectName("news_channel10")
        self.news_channel7 = QtWidgets.QLabel(self.media_tab)
        self.news_channel7.setGeometry(QtCore.QRect(570, 290, 241, 221))
        self.news_channel7.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel7.setText("")
        self.news_channel7.setPixmap(QtGui.QPixmap("icons/cnn news.png"))
        self.news_channel7.setScaledContents(True)
        self.news_channel7.setObjectName("news_channel7")
        self.news_channel11 = QtWidgets.QLabel(self.media_tab)
        self.news_channel11.setGeometry(QtCore.QRect(570, 530, 241, 221))
        self.news_channel11.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                          "")
        self.news_channel11.setText("")
        self.news_channel11.setPixmap(QtGui.QPixmap("icons/bloom_news.jpg"))
        self.news_channel11.setScaledContents(True)
        self.news_channel11.setObjectName("news_channel11")
        self.news_channel3 = QtWidgets.QLabel(self.media_tab)
        self.news_channel3.setGeometry(QtCore.QRect(570, 50, 241, 221))
        self.news_channel3.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel3.setText("")
        self.news_channel3.setPixmap(QtGui.QPixmap("icons/foxnews.png"))
        self.news_channel3.setScaledContents(True)
        self.news_channel3.setObjectName("news_channel3")
        self.news_channel8 = QtWidgets.QLabel(self.media_tab)
        self.news_channel8.setGeometry(QtCore.QRect(830, 290, 241, 221))
        self.news_channel8.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel8.setText("")
        self.news_channel8.setPixmap(QtGui.QPixmap("icons/euro_news.png"))
        self.news_channel8.setScaledContents(True)
        self.news_channel8.setObjectName("news_channel8")
        self.news_channel4 = QtWidgets.QLabel(self.media_tab)
        self.news_channel4.setGeometry(QtCore.QRect(830, 50, 241, 221))
        self.news_channel4.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                         "")
        self.news_channel4.setText("")
        self.news_channel4.setPixmap(QtGui.QPixmap("icons/msnbc_news.png"))
        self.news_channel4.setScaledContents(True)
        self.news_channel4.setObjectName("news_channel4")
        self.news_channel12 = QtWidgets.QLabel(self.media_tab)
        self.news_channel12.setGeometry(QtCore.QRect(830, 530, 241, 221))
        self.news_channel12.setStyleSheet("border: 3px solid rgba(65, 105, 236,100);\n"
                                          "")
        self.news_channel12.setText("")
        self.news_channel12.setPixmap(QtGui.QPixmap("icons/nywork_img.png"))
        self.news_channel12.setScaledContents(True)
        self.news_channel12.setObjectName("news_channel12")
        self.news_button1 = QtWidgets.QPushButton(self.media_tab)
        self.news_button1.setGeometry(QtCore.QRect(50, 50, 241, 221))
        self.news_button1.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button1.setText("")
        self.news_button1.setAutoDefault(False)
        self.news_button1.setDefault(False)
        self.news_button1.setFlat(False)
        self.news_button1.setObjectName("news_button1")
        self.news_button2 = QtWidgets.QPushButton(self.media_tab)
        self.news_button2.setGeometry(QtCore.QRect(310, 50, 241, 221))
        self.news_button2.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button2.setText("")
        self.news_button2.setAutoDefault(False)
        self.news_button2.setDefault(False)
        self.news_button2.setFlat(False)
        self.news_button2.setObjectName("news_button2")
        self.news_button3 = QtWidgets.QPushButton(self.media_tab)
        self.news_button3.setGeometry(QtCore.QRect(570, 50, 241, 221))
        self.news_button3.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button3.setText("")
        self.news_button3.setAutoDefault(False)
        self.news_button3.setDefault(False)
        self.news_button3.setFlat(False)
        self.news_button3.setObjectName("news_button3")
        self.news_button4 = QtWidgets.QPushButton(self.media_tab)
        self.news_button4.setGeometry(QtCore.QRect(830, 50, 241, 221))
        self.news_button4.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button4.setText("")
        self.news_button4.setAutoDefault(False)
        self.news_button4.setDefault(False)
        self.news_button4.setFlat(False)
        self.news_button4.setObjectName("news_button4")
        self.news_button5 = QtWidgets.QPushButton(self.media_tab)
        self.news_button5.setGeometry(QtCore.QRect(50, 290, 241, 221))
        self.news_button5.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button5.setText("")
        self.news_button5.setAutoDefault(False)
        self.news_button5.setDefault(False)
        self.news_button5.setFlat(False)
        self.news_button5.setObjectName("news_button5")
        self.news_button6 = QtWidgets.QPushButton(self.media_tab)
        self.news_button6.setGeometry(QtCore.QRect(310, 290, 241, 221))
        self.news_button6.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button6.setText("")
        self.news_button6.setAutoDefault(False)
        self.news_button6.setDefault(False)
        self.news_button6.setFlat(False)
        self.news_button6.setObjectName("news_button6")
        self.news_button7 = QtWidgets.QPushButton(self.media_tab)
        self.news_button7.setGeometry(QtCore.QRect(570, 290, 241, 221))
        self.news_button7.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button7.setText("")
        self.news_button7.setAutoDefault(False)
        self.news_button7.setDefault(False)
        self.news_button7.setFlat(False)
        self.news_button7.setObjectName("news_button7")
        self.news_button8 = QtWidgets.QPushButton(self.media_tab)
        self.news_button8.setGeometry(QtCore.QRect(830, 290, 241, 221))
        self.news_button8.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button8.setText("")
        self.news_button8.setAutoDefault(False)
        self.news_button8.setDefault(False)
        self.news_button8.setFlat(False)
        self.news_button8.setObjectName("news_button8")
        self.news_button9 = QtWidgets.QPushButton(self.media_tab)
        self.news_button9.setGeometry(QtCore.QRect(50, 530, 241, 221))
        self.news_button9.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 25pt \"Century Gothic\";\n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    border: 2px;\n"
                                        "\n"
                                        "    \n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "\n"
                                        "    background-color: rgba(50, 50, 50, 50);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "    background-color: rgba(65, 105, 236, 50);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.news_button9.setText("")
        self.news_button9.setAutoDefault(False)
        self.news_button9.setDefault(False)
        self.news_button9.setFlat(False)
        self.news_button9.setObjectName("news_button9")
        self.news_button10 = QtWidgets.QPushButton(self.media_tab)
        self.news_button10.setGeometry(QtCore.QRect(310, 530, 241, 221))
        self.news_button10.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    font: 25pt \"Century Gothic\";\n"
                                         "    background-color: rgba(255, 255, 255, 0);\n"
                                         "    border: 2px;\n"
                                         "\n"
                                         "    \n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "\n"
                                         "    background-color: rgba(50, 50, 50, 50);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed\n"
                                         "{\n"
                                         "    background-color: rgba(65, 105, 236, 50);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.news_button10.setText("")
        self.news_button10.setAutoDefault(False)
        self.news_button10.setDefault(False)
        self.news_button10.setFlat(False)
        self.news_button10.setObjectName("news_button10")
        self.news_button11 = QtWidgets.QPushButton(self.media_tab)
        self.news_button11.setGeometry(QtCore.QRect(570, 530, 241, 221))
        self.news_button11.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    font: 25pt \"Century Gothic\";\n"
                                         "    background-color: rgba(255, 255, 255, 0);\n"
                                         "    border: 2px;\n"
                                         "\n"
                                         "    \n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "\n"
                                         "    background-color: rgba(50, 50, 50, 50);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed\n"
                                         "{\n"
                                         "    background-color: rgba(65, 105, 236, 50);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.news_button11.setText("")
        self.news_button11.setAutoDefault(False)
        self.news_button11.setDefault(False)
        self.news_button11.setFlat(False)
        self.news_button11.setObjectName("news_button11")
        self.news_button12 = QtWidgets.QPushButton(self.media_tab)
        self.news_button12.setGeometry(QtCore.QRect(830, 530, 241, 221))
        self.news_button12.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    font: 25pt \"Century Gothic\";\n"
                                         "    background-color: rgba(255, 255, 255, 0);\n"
                                         "    border: 2px;\n"
                                         "\n"
                                         "    \n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "\n"
                                         "    background-color: rgba(50, 50, 50, 50);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed\n"
                                         "{\n"
                                         "    background-color: rgba(65, 105, 236, 50);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.news_button12.setText("")
        self.news_button12.setAutoDefault(False)
        self.news_button12.setDefault(False)
        self.news_button12.setFlat(False)
        self.news_button12.setObjectName("news_button12")
        self.tabWidget.addTab(self.media_tab, "")
        self.weather_tab = QtWidgets.QWidget()
        self.weather_tab.setObjectName("weather_tab")
        self.white_backgroundweather = QtWidgets.QLabel(self.weather_tab)
        self.white_backgroundweather.setGeometry(QtCore.QRect(10, 30, 1101, 751))
        self.white_backgroundweather.setStyleSheet("background-color: white;\n"
                                                   "border: 2px rgb(255, 255, 255);\n"
                                                   "border-radius: 30px;\n"
                                                   "")
        self.white_backgroundweather.setText("")
        self.white_backgroundweather.setObjectName("white_backgroundweather")
        self.weatherspacer = QtWidgets.QLabel(self.weather_tab)
        self.weatherspacer.setGeometry(QtCore.QRect(730, 40, 41, 41))
        self.weatherspacer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weatherspacer.setStyleSheet("background-color: rgb(203, 203, 203);\n"
                                         "border: 2px rgb(255, 255, 255);\n"
                                         "border-radius: 10px;\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.weatherspacer.setText("")
        self.weatherspacer.setPixmap(QtGui.QPixmap("../../../Downloads/icons/search_bar_icon.png"))
        self.weatherspacer.setObjectName("weatherspacer")
        self.weather_search_button = QtWidgets.QPushButton(self.weather_tab)
        self.weather_search_button.setGeometry(QtCore.QRect(1030, 40, 61, 41))
        self.weather_search_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.weather_search_button.setStyleSheet("QPushButton\n"
                                                 "{\n"
                                                 "    background-color: rgb(203, 203, 203);\n"
                                                 "    border: 2px rgb(255, 255, 255);\n"
                                                 "    border-radius: 10px;\n"
                                                 "    \n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    \n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed\n"
                                                 "{\n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.weather_search_button.setText("")
        self.weather_search_button.setIcon(icon5)
        self.weather_search_button.setIconSize(QtCore.QSize(50, 50))
        self.weather_search_button.setFlat(False)
        self.weather_search_button.setObjectName("weather_search_button")
        self.weather_search_bar = QtWidgets.QLineEdit(self.weather_tab)
        self.weather_search_bar.setGeometry(QtCore.QRect(750, 40, 301, 41))
        self.weather_search_bar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.weather_search_bar.setStyleSheet("background-color: rgb(203, 203, 203);\n"
                                              "color: rgb(26, 46, 75);\n"
                                              "font: 12pt \"Century Gothic\";\n"
                                              "border: 2px rgb(255, 255, 255);\n"
                                              "border-radius: 10px;\n"
                                              "")
        self.weather_search_bar.setObjectName("weather_search_bar")
        self.search_location = QtWidgets.QLabel(self.weather_tab)
        self.search_location.setGeometry(QtCore.QRect(10, 230, 1101, 61))
        self.search_location.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "font: 75 40pt \"Century Gothic\";")
        self.search_location.setAlignment(QtCore.Qt.AlignCenter)
        self.search_location.setObjectName("search_location")
        self.location_description = QtWidgets.QLabel(self.weather_tab)
        self.location_description.setGeometry(QtCore.QRect(10, 300, 1101, 31))
        self.location_description.setStyleSheet("font: 20pt \"Candara Light\";\n"
                                                "background-color: rgb(255, 255, 255);")
        self.location_description.setAlignment(QtCore.Qt.AlignCenter)
        self.location_description.setObjectName("location_description")
        self.weather_result_img = QtWidgets.QLabel(self.weather_tab)
        self.weather_result_img.setGeometry(QtCore.QRect(600, 340, 101, 91))
        self.weather_result_img.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.weather_result_img.setText("")
        self.weather_result_img.setPixmap(QtGui.QPixmap("icons/sunny.png"))
        self.weather_result_img.setScaledContents(True)
        self.weather_result_img.setObjectName("weather_result_img")
        self.temperature = QtWidgets.QLabel(self.weather_tab)
        self.temperature.setGeometry(QtCore.QRect(300, 340, 301, 121))
        self.temperature.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 87 90pt \"Arial Black\";")
        self.temperature.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.temperature.setObjectName("temperature")
        self.date_month = QtWidgets.QLabel(self.weather_tab)
        self.date_month.setGeometry(QtCore.QRect(30, 40, 311, 31))
        self.date_month.setStyleSheet("font: 13pt \"Century Gothic\";\n"
                                      "background-color: rgb(255, 255, 255);")
        self.date_month.setObjectName("date_month")
        self.mountain_img = QtWidgets.QLabel(self.weather_tab)
        self.mountain_img.setGeometry(QtCore.QRect(30, 590, 1061, 231))
        self.mountain_img.setText("")
        self.mountain_img.setPixmap(QtGui.QPixmap("icons/mountain_back.jpg"))
        self.mountain_img.setScaledContents(True)
        self.mountain_img.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.mountain_img.setObjectName("mountain_img")
        self.ooo = QtWidgets.QLabel(self.weather_tab)
        self.ooo.setGeometry(QtCore.QRect(10, 780, 1101, 101))
        self.ooo.setText("")
        self.ooo.setObjectName("ooo")
        self.white_backgroundweather.raise_()
        self.weatherspacer.raise_()
        self.weather_search_bar.raise_()
        self.weather_search_button.raise_()
        self.search_location.raise_()
        self.location_description.raise_()
        self.temperature.raise_()
        self.weather_result_img.raise_()
        self.date_month.raise_()
        self.mountain_img.raise_()
        self.ooo.raise_()
        self.tabWidget.addTab(self.weather_tab, "")
        self.news_display = QtWidgets.QWidget()
        self.news_display.setObjectName("news_display")
        self.white_background_news_showcase = QtWidgets.QLabel(self.news_display)
        self.white_background_news_showcase.setGeometry(QtCore.QRect(10, 30, 1101, 741))
        self.white_background_news_showcase.setStyleSheet("background-color: white;\n"
                                                          "border: 2px rgb(255, 255, 255);\n"
                                                          "border-radius: 30px;\n"
                                                          "")
        self.white_background_news_showcase.setText("")
        self.white_background_news_showcase.setObjectName("white_background_news_showcase")
        self.news_showcase = QtWidgets.QListWidget(self.news_display)
        self.news_showcase.setGeometry(QtCore.QRect(30, 50, 1061, 701))
        self.news_showcase.setStyleSheet(
            "QListWidget { background-color: rgb(255, 255, 255); color: rgb(117, 117, 117); font: 15pt \"Century Gothic\"; border: 2px rgb(255, 255, 255); } QScrollBar:vertical { border: none; background: rgb(65, 105, 236); width: 14px; margin: 15px 0 15px 0; border-radius: 0px; } QScrollBar::handle:vertical { background-color: rgb(43, 71, 156); min-height: 30px; border-radius: 7px; } QScrollBar::handle:vertical:hover{ background-color: rgb(198, 198, 198); } QScrollBar::handle:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::sub-line:vertical { border: none; background-color:  rgb(65, 105, 236); height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::add-line:vertical { border: none; background-color: rgb(65, 105, 236); height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::add-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }")

        self.news_showcase.setIconSize(QtCore.QSize(200, 200))
        self.news_showcase.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.news_showcase.setObjectName("news_showcase")
        item = QtWidgets.QListWidgetItem()
        self.news_showcase.addItem(item)
        self.tabWidget.addTab(self.news_display, "")
        self.side_bar_background.raise_()
        self.label.raise_()
        self.main_background.raise_()
        self.home_icon.raise_()
        self.search_side_button.raise_()
        self.category_side_button.raise_()
        self.media_side_button.raise_()
        self.weather_side_button.raise_()
        self.divider.raise_()
        self.divider_2.raise_()
        self.divider_3.raise_()
        self.divider_4.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # navigation functions ------------------------------------------------------
        self.home_icon.clicked.connect(partial(self.navigation, 'home'))
        self.search_side_button.clicked.connect(partial(self.navigation, 'search'))
        self.category_side_button.clicked.connect(partial(self.navigation, 'category'))
        self.media_side_button.clicked.connect(partial(self.navigation, 'media'))
        self.weather_side_button.clicked.connect(partial(self.navigation, 'weather'))
        self.search_button.clicked.connect(self.search_history)

        #media channel buttons ------------------------------------------------------
        self.news_button1.clicked.connect(partial(self.media_navigation, 1))
        self.news_button2.clicked.connect(partial(self.media_navigation, 2))
        self.news_button3.clicked.connect(partial(self.media_navigation, 3))
        self.news_button4.clicked.connect(partial(self.media_navigation, 4))
        self.news_button5.clicked.connect(partial(self.media_navigation, 5))
        self.news_button6.clicked.connect(partial(self.media_navigation, 6))
        self.news_button7.clicked.connect(partial(self.media_navigation, 7))
        self.news_button8.clicked.connect(partial(self.media_navigation, 8))
        self.news_button9.clicked.connect(partial(self.media_navigation, 9))
        self.news_button10.clicked.connect(partial(self.media_navigation, 10))
        self.news_button11.clicked.connect(partial(self.media_navigation, 11))
        self.news_button12.clicked.connect(partial(self.media_navigation, 12))

        #weather search button
        self.weather_search_button.clicked.connect(lambda x: self.weather())

        # category channel buttons ------------------------------------------------------
        self.politics_button.clicked.connect(partial(self.category_search, self.politics_button))
        self.business_button.clicked.connect(partial(self.category_search, self.business_button))
        self.sports_button.clicked.connect(partial(self.category_search, self.sports_button))
        self.technology_button.clicked.connect(partial(self.category_search, self.technology_button))
        self.health_button.clicked.connect(partial(self.category_search, self.health_button))
        self.education_button.clicked.connect(partial(self.category_search, self.education_button))
        self.fashion_button.clicked.connect(partial(self.category_search, self.fashion_button))

        # category channel buttons ------------------------------------------------------
        self.popular1.clicked.connect(partial(self.category_search, self.popular1))
        self.popular2.clicked.connect(partial(self.category_search, self.popular2))
        self.popular3.clicked.connect(partial(self.category_search, self.popular3))
        self.popular4.clicked.connect(partial(self.category_search, self.popular4))
        self.popular5.clicked.connect(partial(self.category_search, self.popular5))
        self.popular6.clicked.connect(partial(self.category_search, self.popular6))
        self.popular7.clicked.connect(partial(self.category_search, self.popular7))
        self.popular8.clicked.connect(partial(self.category_search, self.popular8))

        self.search_button.clicked.connect(lambda x: self.search_load())

        # news_item_clicked
        self.home_news_list.itemDoubleClicked.connect(self.home_newsitem_url)
        self.news_showcase.itemDoubleClicked.connect(self.category_newsitem_url)

        self.home_screen_news = HomeNews()
        self.home_news_loader()
        self.date()
        self.popular_categories()
        self.category = CategoryNews()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.divider.setText(_translate("MainWindow", "_______"))
        self.divider_2.setText(_translate("MainWindow", "_______"))
        self.divider_3.setText(_translate("MainWindow", "_______"))
        self.divider_4.setText(_translate("MainWindow", "_______"))
        __sortingEnabled = self.home_news_list.isSortingEnabled()
        self.home_news_list.setSortingEnabled(False)
        self.home_news_list.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("MainWindow", "Tab 1"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", " Search any word or phrase"))
        self.popular_label.setText(_translate("MainWindow", "Popular"))
        self.popular1.setText(_translate("MainWindow", "PushButton"))
        self.popular5.setText(_translate("MainWindow", "PushButton"))
        self.popular2.setText(_translate("MainWindow", "PushButton"))
        self.popular6.setText(_translate("MainWindow", "PushButton"))
        self.popular3.setText(_translate("MainWindow", "PushButton"))
        self.popular7.setText(_translate("MainWindow", "PushButton"))
        self.popular4.setText(_translate("MainWindow", "PushButton"))
        self.popular8.setText(_translate("MainWindow", "PushButton"))
        self.divider_5.setText(_translate("MainWindow",
                                          "_______________________________________________________________________________________________________________________________________________________________________________"))
        self.history_label.setText(_translate("MainWindow", "History"))
        self.divider_6.setText(_translate("MainWindow",
                                          "_______________________________________________________________________________________________________________________________________________________________________________________"))
        __sortingEnabled = self.history_search_list.isSortingEnabled()
        self.history_search_list.setSortingEnabled(False)
        """item = self.history_search_list.item(0)
        item.setText(_translate("MainWindow", "Sports news"))
        item = self.history_search_list.item(1)
        item.setText(_translate("MainWindow", "Tech news"))"""
        self.history_search_list.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_tab), _translate("MainWindow", "Page"))
        self.politics_button.setText(_translate("MainWindow", "Politics"))
        self.business_button.setText(_translate("MainWindow", "Business"))
        self.sports_button.setText(_translate("MainWindow", "Sports"))
        self.technology_button.setText(_translate("MainWindow", "Technology"))
        self.health_button.setText(_translate("MainWindow", "Health"))
        self.education_button.setText(_translate("MainWindow", "Education"))
        self.fashion_button.setText(_translate("MainWindow", "Fashion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.category_tab), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.media_tab), _translate("MainWindow", "Page"))
        self.weather_search_bar.setPlaceholderText(_translate("MainWindow", " Search any location"))
        self.search_location.setText(_translate("MainWindow", "California"))
        self.location_description.setText(_translate("MainWindow", "OVERCAST CLOUDS"))
        self.temperature.setText(_translate("MainWindow", "54°F"))
        self.date_month.setText(_translate("MainWindow", "Friday, 28 November 2022"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weather_tab), _translate("MainWindow", "Page"))
        __sortingEnabled = self.news_showcase.isSortingEnabled()
        self.news_showcase.setSortingEnabled(False)
        item = self.news_showcase.item(0)
        item.setText(_translate("MainWindow", "Apple"))
        self.news_showcase.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.news_display), _translate("MainWindow", "Page"))


    def navigation(self, screen):
        switch = SwitchScreen()
        switch.switch_screen(screen, self.tabWidget)

    def home_news_loader(self):
        self.home_screen_news.thread(self.home_news_list, QtWidgets, QtGui)

    def home_newsitem_url(self, news_title):
        self.home_screen_news.news_load_url(news_title.text())

    def popular_categories(self):
        categories_btn = [self.popular1, self.popular2, self.popular3, self.popular4, self.popular5, self.popular6, self.popular7, self.popular8]
        search = Search(categories_btn, self.history_search_list)

    def search_history(self):
        history = HistorySearch()
        history.add_search(self.search_bar.text(), self.history_search_list)


    def media_navigation(self, channel_button):
        channel = MediaChannels()
        channel.media_link_open(channel_button - 1)

    def date(self):
        now_date = datetime.datetime.now()
        date_time = now_date.strftime("%A, %d %B %Y")
        self.date_month.setText(date_time)

    def weather(self):
        weather_call = Weather(self.weather_search_bar.text())
        weather_call.grab_temperature(self.weather_search_bar, self.search_location, self.location_description, self.temperature, self.weather_result_img, QtGui)

    def search_load(self):
        self.category_search(self.search_bar)


    def category_search(self, topic):
        self.news_showcase.clear()
        self.tabWidget.setCurrentIndex(5)
        self.category.thread(self.news_showcase, QtWidgets, QtGui, topic.text())


    def category_newsitem_url(self, news_title):
        self.category.news_load_url(news_title.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
