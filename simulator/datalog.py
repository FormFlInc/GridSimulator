class Datalog:
    def __init__(self,db,id_sim):
        self.datalog = {"PWR":0,"price":0,"CO2":0}
        self.db = db
        self.id_sim = id_sim

    def update_datalog(self,_id,power,price,t):
        CO2=0
        self.db.sendUpdate(self.id_sim,_id,t,power,price,CO2)

    def update_data(self,_id,power,price,CO2,t):
        self.db.sendUpdate(self.id_sim,_id,t,power,price,CO2)

    def update_log(self,_id,time,name):

        if (name == 'disable_cons'):
            message = '[{}] Blackout on the node {} at {}h'.format(time,_id,time%24)
            self.db.sendUpdateMessage(self.id_sim,_id,time,message)
        
        elif (name == 'disable_prod'):
            message = '[{}] Overload! shutdown the node {} at {}h'.format(time,_id,time%24)
            self.db.sendUpdateMessage(self.id_sim,_id,time,message)

        elif (name == 'enable_cons'):
            message = '[{}] Enable consumer node {} at {}h'.format(time,_id,time%24)
            self.db.sendUpdateMessage(self.id_sim,_id,time,message)

        elif (name == 'enable_prod'):
            message = '[{}] Enable production node {} at {}h'.format(time,_id,time%24)
            self.db.sendUpdateMessage(self.id_sim,_id,time,message)

        elif (name == 'negBill'):
            message = '[{}] Not enough power for the circuit at {}h'.format(time,time%24)
            self.db.sendUpdateMessage(self.id_sim,_id,time,message)
        
        elif (name == 'posBill'):
            message = '[{}] To much power for the circuit at {}h'.format(time,time%24)
            self.db.sendUpdateMessage(self.id_sim,_id,time,message)

        elif (name == 'USERACTION'):
            message = '[{}] *******************DISABLE OR ENABLE : {} -> {} at {}h*******************'.format(time,_id[0],_id[1],time%24)
            self.db.sendUpdateMessage(self.id_sim,_id[0],time,message)
        else:
            pass