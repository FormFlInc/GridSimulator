from node.NodeP import NodeP
import random

class Prd_nuck(NodeP):
    def __init__(self,meta,_id, ligne_pwr,datalog):
        self.max_power = float(meta['power'])
        self.prior = 2
        self.start_time = float(meta['t1'])
        self.end_time = float(meta['t2'])
        self.cost = float(meta['cost'])
        super().__init__( _id, ligne_pwr,datalog)
        
    def update(self,t):

        if self.enable: 
            price = self.cost*self.max_power
            puissance = self.getCurPower(t)

        else:
            puissance = self.getCurPower(t)
            price = 0

        self.datalog.update_datalog(self._id,puissance,price,t)
        return puissance,0

    def disable_prod(self,t):
        if self.enable:
            temp_t = t - self.enableAtTime
            if temp_t > self.start_time:
                self.enable = False
                self.disableAtTime = t
                return self._id

        return -1

    def enable_prod(self,t):
        if self.enable == False:
            temp_t = t - self.disableAtTime
            if temp_t > self.end_time:
                self.enable = True
                self.enableAtTime = t
                return self._id
        
        return -1

    def getCurPower(self,t):
        if self.enable and self.userEnable:
            temp_t = t-self.enableAtTime #get relatif time
            if (temp_t <= self.start_time):
                return (temp_t*(self.max_power/self.start_time))
            else :
                return self.max_power
        elif self.userEnable:
            temp_t = t-self.disableAtTime
            if (temp_t <= self.end_time):
                return (self.max_power-temp_t*(self.max_power/self.end_time))
            else :
                return 0
        else:
            return 0