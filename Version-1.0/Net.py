# my import
import Attribute


class NET(Attribute.ATTRIBUTE):
    def __init__(self):
        super(NET, self).__init__()
        self.__net_start = {'cord': self.__create_net_cord(), 'status': self.__create_net_status()}
        self._net = self.__net_start.copy()

    # --- get ---
    def get(self):
        """*** Get a net of 'cord' and 'status' ***"""
        return self._net
    # -----------

    # --- create net ---
    def __create_net_cord(self):
        """*** Creating a net of coordinates ***"""
        x, y = self.line_size, self.head_size + self.line_size - 1
        net_cord = []
        for row in range(self._row_net):
            net_cord.append([])
            for col in range(self._col_net):
                net_cord[row].append({'x': x + col * self.block_size + self.block_margin * (col + 1),
                                      'y': y + row * self.block_size + self.block_margin * (row + 1)})
        return net_cord

    def __create_net_status(self):
        """*** Creating a status net ***"""
        net_status = []
        for row in range(self._row_net):
            net_status.append([])
            for col in range(self._col_net):
                net_status[row].append('-')
        return net_status
    # ------------------
