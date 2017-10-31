from pyax12.connection import Connection

class MotorManager:
    '''
    Class to manage motor 
    port on Windows should be 'COMX'
    port on Posix should be '/dev/ttyUSBX'
    '''
    def __init__(self, p="/dev/ttyUSB0", baudRate=1000000, scanLimit=20, defaultSpeed=90):
        self.serial_connection = Connection(port=p, baudrate=baudRate)
        self.connected_motor_ids = []
        self.scan_limit = scanLimit
        self.default_speed = defaultSpeed
        self.available_baudrate = '''+------+-----------+------------+
| Data |  Set BPS  | Target BPS |
+------+-----------+------------+
|    1 | 1000000.0 |  1000000.0 |
|    3 |  500000.0 |   500000.0 |
|    4 |  400000.0 |   400000.0 |
|    7 |  250000.0 |   250000.0 |
|    9 |  200000.0 |   200000.0 |
|   16 |  117647.1 |   115200.0 |
|   34 |   57142.9 |    57600.0 |
|  103 |   19230.8 |    19200.0 |
|  207 |    9615.4 |     9600.0 |
+------+-----------+------------+'''
        self.available_baud_ids = [1, 3, 4, 7, 9, 16, 34, 103, 207]

    def terminateConnection(self):
        self.serial_connection.close()
        print("Connection is closed.")

    ###########################
    # Get Connected Motor Ids #
    ###########################

    def getConnectIds(self):
        self.connected_motor_ids = list(self.serial_connection.scan(range(self.scan_limit)))
        print("Available ids are", self.connected_motor_ids)

    ###########
    # Set Ids #
    ###########

    def setNewIdOf(self, motor_id, new_id):
        if motor_id == new_id or new_id < 1 or new_id > 254:
            print("Please use id in range of 1-254 and not duplicated with old id: {0}".format(motor_id))
            return

        self.serial_connection.set_id(motor_id, new_id)
        print("Motor id {0} is changed to id {1}.".format(motor_id, new_id))

    #####################
    # Print Information #
    #####################

    def printAvailableBaudrates(self):
        print(self.available_baudrate)

    def printControlTable(self, motor_id):
        self.serial_connection.pretty_print_control_table(motor_id)

    ####################
    # Position Control #
    ####################

    def setPositionOf(self, motor_id, pos=512, speed=90):
        self.serial_connection.goto(motor_id, pos, speed=speed)
    
    def setPositionAll(self, pos=512, speed=90):
        for motorId in self.connected_motor_ids:
            self.serial_connection.goto(motorId, pos, speed)

    def getPositionOf(self, motor_id):
        return self.serial_connection.get_goal_position(motor_id)

    def getPositionAll(self):
        temp = {}
        for motorId in self.connected_motor_ids:
            temp[motorId] = self.serial_connection.get_goal_position(motorId)

        return temp

    ####################
    # Baudrate Control #
    ####################

    def getBaudrateOf(self, motor_id):
        return self.serial_connection.get_baud_rate(motor_id)

    def getBaudrateAll(self):
        temp = {}
        for motorId in self.connected_motor_ids:
            temp[motorId] = self.serial_connection.get_baud_rate(motorId)

        return temp

    def setBaudrateOf(self, motor_id, baudId=1):
        # check if input baudId is in range
        if baudId not in self.available_baud_ids:
            print("Please use baudId got from 'Data' column below.")
            self.printAvailableBaudrates()
        else:
            self.serial_connection.set_baud_rate(motor_id, baudId, unit="internal")
            print("Motor id {0} baudrate is set to {1}: {2}.".format(motor_id, baudId, round(2000000. / (baudId + 1))))

    def setBaudrateAll(self, baudId=1):
        # check if input baudId is in range
        if baudId not in self.available_baud_ids:
            print("Please use baudId got from 'Data' column below.")
            self.printAvailableBaudrates()
        else:
            for motorId in self.connected_motor_ids:
                self.serial_connection.set_baud_rate(motorId, baudId, unit="internal")
                print("Motor id {0} baudrate is set to {1}: {2}.".format(motorId, baudId, round(2000000. / (baudId + 1))))

    #########
    # Helps #
    #########

    @staticmethod
    def help():
        txt = '''List of methods available.
        ====== Connection ======
        --- Import
        from dxlcli import MotorManager

        --- Instantiate class
        m = MotorManager(p="/dev/ttyUSB0", baudRate=1000000, scanLimit=20, defaultSpeed=90)
        *** USE COMXX on Windows ***

        --- Terminate connection
        m.terminateConnection()

        --- Get connected motor ids
        m.getConnectIds()

        ====== ID settings ======
        m.setNewIdOf(self, motor_id, new_id):

        ====== Printing Information ======
        --- All available baudrates
        m.printAvailableBaudrates()

        --- Motor status table
        m.printControlTable(motor_id)

        ====== Position Control ======
        --- Get
        m.getPositionOf(motor_id)
        m.getPositionAll()

        --- Set
        m.setPositionOf(self, motor_id, pos=512, speed=90)
        m.setPositionAll(self, pos=512, speed=90)

        ====== Baudrate Control ======
        --- Get
        getBaudrateOf(motor_id)
        getBaudrateAll()

        --- Set
        setBaudrateOf(motor_id, baudId=1)
        setBaudrateAll(baudId=1)
        '''

        print(txt)