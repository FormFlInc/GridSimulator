
class Node:
    def __init__(self, _id , ligne_pwr, datalog):
        self._id = _id
        self.ligne_power = ligne_pwr
        self.childs = []
        self.enable = True
        self.userEnable = True
        self.datalog = datalog

    def __str__(self):
        return str(self._id) + " - " + str(type(self))+ " - "+str(self.enable)+" - "+str(self.userEnable)

    def callUpdate(self,t):
        
        return self.update(t)
        

    def update(self,t):


        bill = self.getCurPower(t)
        nbrTry = 0
        tested_strat = []
        while abs(bill) > self.ligne_power and nbrTry < 15:
            print("***************LIGNE POWER EXCEDEED***************")
            print("ID : ",self._id)
            print("LIGNE PWR : ", self.ligne_power," BILL :",abs(bill))
            print(tested_strat)
            
            nbrTry+=1
            print("TRY  : ",nbrTry,"START BILL : ",bill)
            if bill > 0: #si on produit trop

                strat = [("minimize_prod",(bill,t)),("disable_prod",t)]

                res = self.tryStrat(strat,tested_strat,False,t)
                if res != -1:
                    tested_strat.append(res)

            elif bill < 0: #si on consome trop
        
                strat = [("minimize_cons",bill),("disable_cons",t)]
                res = self.tryStrat(strat,tested_strat,True,t)
                if res != -1:
                    tested_strat.append(res)

            else:
                break
        
            bill = self.getCurPower(t)
             
        int_c = int_p = 0

        for child in self.childs :
            int_np,int_nc = child.callUpdate(t)
            int_p += int_np
            int_c += int_nc

        return int_p,int_c

            #function that find all the node wich have the selected attribute
    
    def sendMsg(self,node_id,time,strat):
        return self.datalog.update_log(node_id,time,strat)

    def tryStrat(self,strat,excepts,needReverse,t):

        for s in strat:
            node_id = self.tryAttribute(s[0],s[1],excepts,needReverse)
            print("      - strat : ",s, "node : ",node_id)
            if node_id != -1:
                self.sendMsg(node_id,t,s[0])
                return (s[0],node_id)
        
        return -1

    def tryAttribute(self,attr,param,excepts,needReverse):
        target_node = self.getNodeArray(attr,needReverse)
        node_id = -1
    
        for child in target_node:
            if child.userEnable:
                alreadytry = False
                
                if len(excepts)>0:
                    for ex in excepts:
                        if ex[0] == attr and child._id == ex[1]:
                            alreadytry = True
                
                if alreadytry == False:
                    attr_func = getattr(child,attr)
                    node_id = attr_func(param)
                    if node_id != -1:
                        return node_id

        return -1

    def getNodeArray(self,attr,needReverse):
    
        target_node = []
        temp_node = []

        for child in self.childs:
           
            if child.prior == 100:          #check if it's a node
                temp_node += child.getNodeArray(attr,needReverse)
            elif(hasattr(child,attr)):      #check if we have the correct attribute
                target_node.append(child)

        result_node = target_node + temp_node

        #we need to sort by prior
        return sorted(result_node, key=lambda x: x.prior, reverse=needReverse)

    def setUserEnable(self,node_id,en,time):
        if self._id == node_id:
            self.userEnable = en
            
            for child in self.childs:
                child.setUserEnable(child._id,en,time)

            return self._id
        else:
            for child in self.childs:
                node = child.setUserEnable(node_id,en,time)
                if node != -1:
                    self.datalog.update_log((node,en),time,"USERACTION")    
                    return node
        
        return -1
