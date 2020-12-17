class Node:
    def __init__(self, _id , max_pwr):
        self._id = _id
        self.ligne_power = max_pwr
        self.childs = []
        self.enable = True
        self.simpleType = "n"
    
    def firstUpdate(self,datalog,t):
        int_p = 0
        int_c = 0

        for child in self.childs :
            int_np,int_nc = child.update(datalog,t)
            int_p += int_np
            int_c += int_nc
        

        bill = int_p-int_c

        if int_p > int_c: #si on produit trop

            #try to sale
            node_id = self.trySale(bill)

            #try to slow prod
            if node_id == -1:    
                node_id = self.minimize_prod(bill)

            #try to dissip power
            if node_id == -1:       
                node_id = self.max_dissp(bill)

            #try to shutdown prod
            if node_id == -1:       
                node_id = self.disable_prod(bill)

        elif int_c > int_p:
            #try to max prod
            node_id = self.maximize_prod(bill)
            #cut a building
            if node_id == -1:
                node_id = self.disable_cons(bill)

            
    def disable_cons(self,target):
        prior_type = [Cns_diss,Cns_sale,Cns_town,Cns_enter]
        node_id = -1
        int_count = 0
        while(node_id == -1) or (int_count == len(prior_type)):
            node_id = self.disable_by_type(prior_type[int_count],target)
            int_count += 1

        return node_id
    
    def disable_prod(self,target):
        prior_type = [Prd_buy,Prd_nuck,Prd_wind,Prd_gaz]
        node_id = -1
        int_count = 0
        while(node_id == -1) or (int_count == len(prior_type)):
            node_id = self.disable_by_type(prior_type[int_count],target)
            int_count += 1

        return node_id

    def maximize_prod(self,target):
        return 0

    def minimize_prod(self,target):
        return 0

    def minimize_cons(self,node_type,target):
        return 0

    def trySale(self,target):
        return 0

    def max_dissp(self,target):
        return 0

    def update(self,datalog,t):

        int_p = 0
        int_c = 0

        for child in self.childs :
            int_np,int_nc = child.update(datalog,t)
            int_p += int_np
            int_c += int_nc

        bill = int_p - int_c

        if abs(bill) > self.ligne_power: #on depasse calbe
            if bill < 0:        #désactive un consomateur
                node_id = self.disable_cons(self.ligne_power - bill)

                #datalog.update_datalog(node_id,puissance,price,temps)
            else:               #désactive un producteur
                prior_type = [Prd_buy,Prd_nuck,Prd_wind,Prd_gaz]
                node_id = -1
                int_count = 0
                while(node_id == -1):
                    node_id = self.disable_by_type(prior_type[int_count],self.ligne_power - bill)
                    int_count += 1

        return int_p,int_c

    def disable_by_type(self,node_type,atleat):
        node_child = []
        node_corType = []
        for child in self.childs :
            if isinstance(child,node_type):
                node_corType.append(child)
            elif isinstance(child,Node):
                node_child.append(child)

        value = -1
        for child in node_child:
            value = child.disable_by_type(self,node_type)
            if value == 1:
                return child.id

        if len(node_corType) == 0:
            return -1

        int_min = 1000000
        node_MinPwrNode = ""
        for child in node_corType:
            if child.max_power < int_min:
                int_min = child.max_power
                node_MinPwrNode = child

        node_MinPwrNode.enable = False
        return child.id