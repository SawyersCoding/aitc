import random


class weather:
    def __init__ (self):
        pass



    def set_weather(self, weather, icy):

        self.weather = weather
        self.icy = icy


            

    





#w = weather()
#w.set_weather(4, True)
#print(w.icy)
#on notify 


# is there a plane at node .. is there a plane between nodes
#respond to the plane instead of receive its info

#So the methods I want to call the airport manager for are the following:
#next_position(plane_id)
#node_clear(plane_id, next_position)
# if destination is 1 or 2 do not have to check go ahead
#planes that are leaving 1 or 2 
#list of responses already given, if go ahead to A, then cannot be allowed to 

class ATC:
    def __init__ (self, airport_manager, weather):
        self.airport_manager = airport_manager
        self.weather = weather
        self.approved = []



        

        
        


    def go_ahead (self, plane_id):
        next_position = self.airport_manager.next_position(plane_id)


        if(self.airport_manager.node_clear(plane_id, next_position) == True):
            go_ahead = True

        else:
            go_ahead = False

        return go_ahead
    

    def needs_deIcing (self, plane_id):
        near_a = self.airport_manager.is_plane_between("A", "A'", plane_id)
        if(near_a) and (self.weather.icy == True):
            return True
        else:
            return False



    #clear for landing
    #clear for takeoff
    #take plane id take a' its okay 
    # if there is a plane at A', if the plane at A' has more than 1 tic
    def clear_for_landing(self):

        plane_near_landing = self.airport_manager.ticks_between("A'", "TAKE_OFF")
        plane_near = False
        for i in plane_near_landing:
            if (i > 0):
                plane_near = True
        
        return not plane_near
    

    def clear_for_takeoff(self):

        plane_in_danger_zone = self.airport_manager.ticks_between("D", "C")
        plane_in_zone = False
        for i in plane_in_danger_zone:
            if (i > 0):
                plane_in_zone = True

        return not plane_in_zone
    

    def decision_tree(self, plane_id, destination):
        location = self.airport_manager.get_position(plane_id)
        # print("APPROVED: ", self.approved)	

        if(self.weather != 5):
            if (self.needs_deIcing(plane_id)):
                return "ICE"
            
            elif(destination == "1"):
                return destination
            
            elif (destination == "2"):
                return destination

            elif(destination in self.approved):
                print("HIT: " + location)
                return location

            elif ((self.airport_manager.get_position == "SKY") and self.clear_for_landing()):
                return destination
        
            elif ((destination == "TAKE_OFF") and self.clear_for_takeoff()):
                return destination
    
            elif (self.go_ahead(plane_id)):
                self.approved.append(destination)
                return destination
            
            else:
                return location
        else:
            return location
        
    def clear_list(self):
        self.approved.clear()
        return
        


        


       


        
        
        






