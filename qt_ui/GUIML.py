# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIML.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Launcher(object):
    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(900, 540)
        Launcher.setMinimumSize(QtCore.QSize(0, 0))
        Launcher.setMaximumSize(QtCore.QSize(900, 550))
        self.centralwidget = QtWidgets.QWidget(Launcher)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 10, 441, 441))
        self.groupBox_4.setObjectName("groupBox_4")
        self.shell_window_text = QtWidgets.QTextEdit(self.groupBox_4)
        self.shell_window_text.setEnabled(True)
        self.shell_window_text.setGeometry(QtCore.QRect(10, 20, 421, 381))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.shell_window_text.setFont(font)
        self.shell_window_text.setWhatsThis("")
        self.shell_window_text.setFrameShape(QtWidgets.QFrame.Box)
        self.shell_window_text.setObjectName("shell_window_text")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 410, 61, 21))
        self.label.setObjectName("label")
        self.shell_send_button = QtWidgets.QPushButton(self.groupBox_4)
        self.shell_send_button.setGeometry(QtCore.QRect(380, 410, 51, 21))
        self.shell_send_button.setObjectName("shell_send_button")
        self.shell_text = QtWidgets.QLineEdit(self.groupBox_4)
        self.shell_text.setGeometry(QtCore.QRect(70, 410, 301, 21))
        self.shell_text.setObjectName("shell_text")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 401, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(90, 170, 301, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 81, 21))
        self.label_4.setObjectName("label_4")
        self.ext_env_mdiArea = QtWidgets.QMdiArea(self.groupBox_2)
        self.ext_env_mdiArea.setGeometry(QtCore.QRect(370, 80, 21, 21))
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ext_env_mdiArea.setBackground(brush)
        self.ext_env_mdiArea.setObjectName("ext_env_mdiArea")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(210, 50, 81, 21))
        self.label_10.setObjectName("label_10")
        self.base_env_mdiArea = QtWidgets.QMdiArea(self.groupBox_2)
        self.base_env_mdiArea.setGeometry(QtCore.QRect(370, 50, 21, 21))
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.base_env_mdiArea.setBackground(brush)
        self.base_env_mdiArea.setObjectName("base_env_mdiArea")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(210, 20, 81, 21))
        self.label_14.setObjectName("label_14")
        self.memory_mdiArea = QtWidgets.QMdiArea(self.groupBox_2)
        self.memory_mdiArea.setGeometry(QtCore.QRect(370, 20, 21, 21))
        self.memory_mdiArea.setAccessibleName("")
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.memory_mdiArea.setBackground(brush)
        self.memory_mdiArea.setObjectName("memory_mdiArea")
        self.mdiArea_mem_3 = QtWidgets.QMdiArea(self.groupBox_2)
        self.mdiArea_mem_3.setGeometry(QtCore.QRect(250, 140, 20, 21))
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea_mem_3.setBackground(brush)
        self.mdiArea_mem_3.setObjectName("mdiArea_mem_3")
        self.mdiArea_mem_4 = QtWidgets.QMdiArea(self.groupBox_2)
        self.mdiArea_mem_4.setGeometry(QtCore.QRect(310, 140, 21, 21))
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea_mem_4.setBackground(brush)
        self.mdiArea_mem_4.setObjectName("mdiArea_mem_4")
        self.mdiArea_mem_5 = QtWidgets.QMdiArea(self.groupBox_2)
        self.mdiArea_mem_5.setGeometry(QtCore.QRect(370, 140, 21, 21))
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea_mem_5.setBackground(brush)
        self.mdiArea_mem_5.setObjectName("mdiArea_mem_5")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(220, 140, 31, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(340, 140, 31, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(280, 140, 31, 21))
        self.label_22.setObjectName("label_22")
        self.memory_label = QtWidgets.QLabel(self.groupBox_2)
        self.memory_label.setGeometry(QtCore.QRect(300, 20, 54, 21))
        self.memory_label.setObjectName("memory_label")
        self.base_env_label = QtWidgets.QLabel(self.groupBox_2)
        self.base_env_label.setGeometry(QtCore.QRect(300, 50, 54, 21))
        self.base_env_label.setObjectName("base_env_label")
        self.ext_env_label = QtWidgets.QLabel(self.groupBox_2)
        self.ext_env_label.setGeometry(QtCore.QRect(300, 80, 54, 21))
        self.ext_env_label.setObjectName("ext_env_label")
        self.select_device_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.select_device_comboBox.setGeometry(QtCore.QRect(20, 40, 171, 20))
        self.select_device_comboBox.setObjectName("select_device_comboBox")
        self.select_device_comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 190, 41, 31))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(90, 196, 271, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_16.setObjectName("label_16")
        self.select_env_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.select_env_comboBox.setGeometry(QtCore.QRect(20, 100, 171, 20))
        self.select_env_comboBox.setObjectName("select_env_comboBox")
        self.select_env_comboBox.addItem("")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(210, 110, 81, 21))
        self.label_23.setObjectName("label_23")
        self.rate_mdiArea = QtWidgets.QMdiArea(self.groupBox_2)
        self.rate_mdiArea.setGeometry(QtCore.QRect(370, 110, 21, 21))
        self.rate_mdiArea.setAccessibleName("")
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.rate_mdiArea.setBackground(brush)
        self.rate_mdiArea.setObjectName("rate_mdiArea")
        self.rate_label = QtWidgets.QLabel(self.groupBox_2)
        self.rate_label.setGeometry(QtCore.QRect(300, 110, 61, 21))
        self.rate_label.setObjectName("rate_label")
        self.Launcher_button = QtWidgets.QPushButton(self.centralwidget)
        self.Launcher_button.setGeometry(QtCore.QRect(440, 460, 251, 31))
        self.Launcher_button.setObjectName("Launcher_button")
        self.shell_clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.shell_clear_button.setGeometry(QtCore.QRect(700, 460, 81, 31))
        self.shell_clear_button.setObjectName("shell_clear_button")
        self.shell_reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.shell_reset_button.setGeometry(QtCore.QRect(790, 460, 81, 31))
        self.shell_reset_button.setObjectName("shell_reset_button")
        self.module_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.module_widget.setGeometry(QtCore.QRect(16, 9, 411, 251))
        self.module_widget.setMovable(False)
        self.module_widget.setObjectName("module_widget")
        self.module_tab1 = QtWidgets.QWidget()
        self.module_tab1.setObjectName("module_tab1")
        self.module_flag = QtWidgets.QPushButton(self.module_tab1)
        self.module_flag.setGeometry(QtCore.QRect(300, 190, 75, 23))
        self.module_flag.setSizeIncrement(QtCore.QSize(0, 8))
        self.module_flag.setObjectName("module_flag")
        self.module_widget.addTab(self.module_tab1, "")
        self.module_tab2 = QtWidgets.QWidget()
        self.module_tab2.setObjectName("module_tab2")
        self.module_widget.addTab(self.module_tab2, "")
        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Launcher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        Launcher.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Launcher)
        self.statusBar.setObjectName("statusBar")
        Launcher.setStatusBar(self.statusBar)
        self.actionl_admin = QtWidgets.QAction(Launcher)
        self.actionl_admin.setObjectName("actionl_admin")
        self.actionSelect_venv = QtWidgets.QAction(Launcher)
        self.actionSelect_venv.setObjectName("actionSelect_venv")
        self.actionGithub = QtWidgets.QAction(Launcher)
        self.actionGithub.setObjectName("actionGithub")
        self.actionMake_GDModule = QtWidgets.QAction(Launcher)
        self.actionMake_GDModule.setObjectName("actionMake_GDModule")
        self.actionJoin_us = QtWidgets.QAction(Launcher)
        self.actionJoin_us.setObjectName("actionJoin_us")
        self.actionAI_Studio = QtWidgets.QAction(Launcher)
        self.actionAI_Studio.setObjectName("actionAI_Studio")
        self.actionQQ = QtWidgets.QAction(Launcher)
        self.actionQQ.setObjectName("actionQQ")
        self.actionrun_check = QtWidgets.QAction(Launcher)
        self.actionrun_check.setChecked(False)
        self.actionrun_check.setObjectName("actionrun_check")
        self.menu.addAction(self.actionl_admin)
        self.menu.addAction(self.actionrun_check)
        self.menu_2.addAction(self.actionAI_Studio)
        self.menu_2.addAction(self.actionGithub)
        self.menu_2.addAction(self.actionMake_GDModule)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionJoin_us)
        self.menu_2.addAction(self.actionQQ)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Launcher)
        self.module_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Launcher)
        Launcher.setTabOrder(self.Launcher_button, self.shell_window_text)
        Launcher.setTabOrder(self.shell_window_text, self.shell_text)
        Launcher.setTabOrder(self.shell_text, self.shell_clear_button)
        Launcher.setTabOrder(self.shell_clear_button, self.shell_send_button)

    def retranslateUi(self, Launcher):
        _translate = QtCore.QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "GDM程序启动器V0.1.0 Beta"))
        self.centralwidget.setStatusTip(_translate("Launcher", "宣传文本"))
        self.groupBox_4.setTitle(_translate("Launcher", "运行状态"))
        self.shell_window_text.setStatusTip(_translate("Launcher", "此处将展示运行状态"))
        self.shell_window_text.setHtml(_translate("Launcher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt;\">由于Module和启动器分离，若在使用过程中出现问题，可以先通过一下方案定位问题：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt;\">目光移动到左上角ヾﾉ≧∀≦)o! 点击环境设置-&gt;运行检测-&gt;启动器运行检测/Module示例数据检测</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt;\">若检测均能通过，说明Demo数据可以成功运行，请检查数据和配置本身是否存在问题。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt;\">当然，也可以在左侧\'Module说明\'中找到相关交流群(可能)信息。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt; color:#ff0000;\">(Module中可能包含第三方库，请勿使用中文文件名、路径，这将可能导致程序崩溃！)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt; color:#55aaff;\">-----启动器官方讨论群-----</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt;\">QQ群-月初阁：1128826410 (若满员请打开下方AI Studio主页获取最新群号)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt;\">AI Studio主页：</span><a href=\"z\"><span style=\" font-family:\'等线\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">暂无</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:9pt; color:#ffaa00;\">-----正在连接控制台-----</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'等线\'; font-size:9pt; color:#ffaa00;\"><br /></p></body></html>"))
        self.label.setText(_translate("Launcher", "Shell命令"))
        self.shell_send_button.setText(_translate("Launcher", "发送"))
        self.groupBox_2.setTitle(_translate("Launcher", "环境相关"))
        self.label_2.setText(_translate("Launcher", "资源准备进度"))
        self.label_4.setText(_translate("Launcher", "Ext环境状态"))
        self.label_10.setText(_translate("Launcher", "Base环境状态"))
        self.label_14.setText(_translate("Launcher", "内存/显存等级"))
        self.label_20.setText(_translate("Launcher", "正常"))
        self.label_21.setText(_translate("Launcher", "异常"))
        self.label_22.setText(_translate("Launcher", "警告"))
        self.memory_label.setText(_translate("Launcher", "未检测"))
        self.base_env_label.setText(_translate("Launcher", "未检测"))
        self.ext_env_label.setText(_translate("Launcher", "未检测"))
        self.select_device_comboBox.setItemText(0, _translate("Launcher", "仅CPU模式运行"))
        self.label_11.setText(_translate("Launcher", "状态："))
        self.label_15.setText(_translate("Launcher", "正在准备"))
        self.label_16.setText(_translate("Launcher", "运行硬件环境："))
        self.select_env_comboBox.setItemText(0, _translate("Launcher", "->点击此处新建一个环境<-"))
        self.label_19.setText(_translate("Launcher", "解释器(软件)环境："))
        self.label_23.setText(_translate("Launcher", "预计运行速度"))
        self.rate_label.setText(_translate("Launcher", "未检测"))
        self.Launcher_button.setText(_translate("Launcher", "启动"))
        self.shell_clear_button.setText(_translate("Launcher", "清空输出"))
        self.shell_reset_button.setText(_translate("Launcher", "重启终端"))
        self.module_flag.setText(_translate("Launcher", "占位"))
        self.module_widget.setTabText(self.module_widget.indexOf(self.module_tab1), _translate("Launcher", "Module配置"))
        self.module_widget.setTabText(self.module_widget.indexOf(self.module_tab2), _translate("Launcher", "关于作者"))
        self.menu.setTitle(_translate("Launcher", "环境配置"))
        self.menu_2.setTitle(_translate("Launcher", "关于启动器"))
        self.actionl_admin.setText(_translate("Launcher", "GDM管理员界面"))
        self.actionl_admin.setStatusTip(_translate("Launcher", "进入GDM最高权限的管理员界面，在这里可以更好操控虚拟环境以及其它设置。"))
        self.actionSelect_venv.setText(_translate("Launcher", "选择GDM环境"))
        self.actionGithub.setText(_translate("Launcher", "Github主页"))
        self.actionMake_GDModule.setText(_translate("Launcher", "GDModule制作指南"))
        self.actionJoin_us.setText(_translate("Launcher", "关于启动器"))
        self.actionAI_Studio.setText(_translate("Launcher", "AI Studio主页"))
        self.actionQQ.setText(_translate("Launcher", "加入QQ群一起讨论"))
        self.actionrun_check.setText(_translate("Launcher", "运行检测(&Ctrl+A)"))
        self.actionrun_check.setStatusTip(_translate("Launcher", "若当前Module运行出现问题可以尝试使用该选项判断"))
