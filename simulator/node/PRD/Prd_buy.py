from node.node import Node

class Prd_buy(Node):
    def __init__(self,meta,_id, max_pwr):
        self.meta = meta
        self.max_power = int(self.meta['power'])
        super().__init__( _id, max_pwr)
        

    def update(self,datalog,t):

        cost = int(self.meta['cost'])

        price = cost*puissance
        puissance = puissance
        temps = t

        datalog.update_datalog(self._id,puissance,price,temps)