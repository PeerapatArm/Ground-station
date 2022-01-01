from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from setting_file import *
from setting_file import Port
from setting_file import Clock

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_bt()
        self.port_box = None
        self.refresh()
        self.show()
        

    def connect_bt(self):
        self.ui.clear_bt.clicked.connect(self.clear)
        self.ui.start_bt.clicked.connect(self.start)
        self.ui.refresh_bt.clicked.connect(self.refresh)
        self.ui.send_CMD_bt.clicked.connect(self.sendcmd)

    def sendcmd(self):
        pass

    def clear(self):
        print("Clear")
        
    def refresh(self):
        self.ui.port_box.clear()
        self.ui.Baud_box.clear()
        for i in range(5):
            self.ui.port_box.addItem(str(i))
        number =[110,300,600,1200,2400,4800,9600,14400]    
        for i in number:
            self.ui.Baud_box.addItem(str(i))


    def start(self):
        self.port = self.ui.port_box.currentText()
        self.baudrate = 9600
        Window.start(self.port,self.baudrate)
    
    
class SerialThread(QThread):
    carrier1 = QtCore.pyqtSignal(object)
    carrier2 = QtCore.pyqtSignal(object)
    carrier3 = QtCore.pyqtSignal(object)

    def __init__(self,com,baud,parent = None) -> None:
        super(SerialThread,self).__init__(parent)
        self.port =Port(com=com,baud=baud,end='$',filename="Project")
        self.port.connect()
        self.dict = {
            'C': ["TYP","PKG","CLO","ALT","LAT","LNG","TEP","HUM","BAT","ACX","ACY","ACZ","GYX","GYY","GYZ","PEE","POS"],
            'R': ["TYP","PKG","ALT","LAT","LNG","TEP","BAT","ACX","ACY","ACZ","GYX","GYY","GYZ","PEE","POS"],
            'G': ["TYP", "LAT", "LNG", "ALT", "MGX", "MGY", "MGZ"]
        }

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.pkg = self.port.reading()
            if isinstance(self.pkg, dict):
                if self.pkg["TYP"] == 'C':
                    print("[Cansat]", end='\t')
                    self.pkg1 = self.pkg
                    if float(self.pkg1["LAT"]) != 0 and float(self.pkg1["LNG"]) != 0:
                        self.port.gearthcoord(
                            f"{self.pkg['LNG']},{self.pkg['LAT']},{self.pkg['ALT']}\n")
                    self.carrier1.emit(self.pkg1)
                elif self.pkg["TYP"] == 'R':
                    print("[Rocket]", end ='\t')
                    self.pkg2 = self.pkg
                    self.carrier2.emit(self.pkg2)
                elif self.pkg["TYP"] == 'G':
                    print("[Ground]", end = '\t')
                    self.pkg3 = self.pkg
                    self.carrier3.emit(self.pkg3)
    
    def stop(self):
        self._isRunning = False

class TimerThread(QThread):
    carrier1 = QtCore.pyqtSignal(object)
    carrier2 = QtCore.pyqtSignal(object)

    def __init__(self,parent = None) -> None:
        super(TimerThread,self).__init__(parent)
        self.clock = Clock.RTC()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.carrier1.emit(self.clock.time_pc())
            self.carrier2.emit(self.clock.time_elapsed())

    def stop(self):
        self._isRunning = False


class Controller:
    def __init__(self) -> None:
        self.show_ui()
        self.set_clock()

    def show_ui(self):
        self.ui_main = MainWindow()
        self.ui_main.ui.Can_Batt.setValue(100)
        self.ui_main.ui.Roc_Batt.setValue(100)

    def set_ui(self):
        self.cansat ={
            "PKG": [], "ALT": [], "TEM": [], "HUM": [], "ROT": []}
        self.rocket ={
            "PKG": [], "ALT": [], "TEM": []}

    def start(self,com,baud):
        self.serial = SerialThread(com, baud)
        self.serial.carrier1.connect(self.update_cansat)
        self.serial.carrier2.connect(self.update_rocket)
        self.serial.carrier3.connect(self.update_ground)
        self.serial.start()

    def set_clock(self):
        self.clock = TimerThread()
        self.clock.carrier1.connect(self.update_clock)
        self.clock.carrier2.connect(self.update_elapsed)
        self.clock.start()

    def update_cansat(self,data):
        self.cansat["PKG"].append(int(data["PKG"]))
        self.cansat["ALT"].append(float(data["ALT"]))
        self.cansat["TEM"].append(float(data["TEM"]))
        self.cansat["HUM"].append(float(data["HUM"]))
        self.cansat["ROT"].append(float(data["ROT"]))

        self.ui_main.ui.Can_Alt.setText(str(data["ALT"]))
        self.ui_main.ui.Can_Tem.setText(str(data["TEM"]))
        self.ui_main.ui.Can_Humid.setText(str(data["HUM"]))
        self.ui_main.ui.Can_rotat.setText(str(data["ROT"]))
        self.ui_main.ui.Can_ACCX.setText(str(data["ACX"]))
        self.ui_main.ui.Can_ACCY.setText(str(data["ACY"]))
        self.ui_main.ui.Can_ACCZ.setText(str(data["ACZ"]))
        self.ui_main.ui.Can_GYRX.setText(str(data["GYX"]))
        self.ui_main.ui.Can_GYRY.setText(str(data["GYY"]))
        self.ui_main.ui.Can_GYRZ.setText(str(data["GYZ"]))

        self.plot(self.ui_main.ui.Can_Alt_graph,self.cansat["PKG"],self.cansat["ALT"])
        self.plot(self.ui_main.ui.Can_Tem_graph,self.cansat["PKG"],self.cansat["TEM"])
        self.plot(self.ui_main.ui.Humid_graph,self.cansat["PKG"],self.cansat["HUM"])
        self.plot(self.ui_main.ui.Can_rotat_graph,self.cansat["PKG"],self.cansat["ROT"])
        


    def update_rocket(self,data):
        self.rocket["PKG"].append(int(data["PKG"]))
        self.rocket["ALT"].append(int(data["ALT"]))
        self.rocket["TEM"].append(int(data["TEM"]))

        self.ui_main.ui.Roc_Alt.setText(str(data["ALT"]))
        self.ui_main.ui.Roc_Tem.setText(str(data["TEM"]))
        self.ui_main.ui.Roc_ACCX.setText(str(data["ACX"]))
        self.ui_main.ui.Roc_ACCY.setText(str(data["ACY"]))
        self.ui_main.ui.Roc_ACCZ.setText(str(data["ACZ"]))
        self.ui_main.ui.Roc_GYRX.setText(str(data["GYX"]))
        self.ui_main.ui.Roc_GYRY.setText(str(data["GYY"]))
        self.ui_main.ui.Roc_GYRZ.setText(str(data["GYZ"]))

        self.plot(self.ui_main.ui.Roc_Alt_graph,self.rocket["PKG"],self.rocket["ALT"])
        self.plot(self.ui_main.ui.Roc_Tem_graph,self.rocket["PKG"],self.rocket["TEM"])
        
    def update_both(self,data):
        self.ui_main.ui.T_C_R_peek.setText(str(data["PEE"]))
        self.ui_main.ui.T_C_R_posi.setText(str(data["POS"]))

    def update_ground(self,data):
        pass

    def update_clock(self,data):
        self.ui_main.ui.time.setText(data)

    def update_elapsed(self,data):
        self.ui_main.ui.elapsed.setText(data)

    def plot(self, graph, x, y):
        graph.clear()
        if len(x)>50:
            graph.plot(x[-50:-1],y[-50:-1])
        else:
            graph.plot(x,y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Controller()
    sys.exit(app.exec_())


