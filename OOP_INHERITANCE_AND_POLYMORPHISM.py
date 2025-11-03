class Agent:
    
    total_agents = 0
    
    def __init__(self, code_name:str, clearance_level:int):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1
        
    def report(self):
        return f"Agent {self.code_name}, reporting. Clearance Level:{self._clearance_level}"
        
    def getter_clearance_level(self):
        return self._clearance_level
        
    def seetter_clearance_level(self,value):
        if 1 < self._clearance_level < 10:
            self._clearance_level = value
        return self._clearance_level
    
    @staticmethod
    def get_total_agents():
       return Agent.total_agents
    
    
class Mission:
    
    def __init__(self, mission_name:str, target_location:str, assigned_agent:Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent
        
    def brief(self):
        print("Mission:{}, Target:{}, Agent:{}".format(self.mission_name,self.target_location,self.assigned_agent.code_name))
        
        
class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level, region):
        super().__init__(code_name, clearance_level)
        self.region = region
    
    def report(self):
        return super().report() + f"region:{self.region}"
        

class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, specialty):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty
    
    def report(self):
        return super().report() + self.specialty
    
    
a = Agent("OIF",1)
print(a.get_total_agents())


def polymor(l):
    for i in l:
        print(i.report())
            
l_polymor = []
l_polymor.append(Agent("Pinchas",1))
l_polymor.append(FieldAgent("Evyatar Ben Any",2, "Rechovot")) 
l_polymor.append(CyberAgent("Ariel",3 ," Makot")) 
polymor(l_polymor)