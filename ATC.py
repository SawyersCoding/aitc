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

class ATC:
    def __init__ (self, airport_manager, weather):
        self.airport_manager = airport_manager
        self.weather = weather

        

        
        


    def go_ahead (self, plane_id):
        next_position = self.airport_manager.next_position(plane_id)



        if(self.airport_manager.node_clear(plane_id, next_position) == True):
            go_ahead = True

        else:
            go_ahead = False

        return go_ahead
    

    def needs_deIcing (self, plane_id):
        near_a = self.airport_manager.is_plane_between("A", "A'", plane_id)
        if(near_a) and (weather.icy == True):
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


        

        



    

    





    
    
