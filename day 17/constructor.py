class Point:
    # constructor
    def __init__(self,longtitude,latitude):
        self.__longtitude=longtitude
        self.__latitude=latitude
        # print('Object was created')
    # respresent of the classs

    def setLontitude(self,long):
        self.__longtitude=long
    
    def getLontitude(self):
        return self.__longtitude
        
    def __str__(self):
        return f"Point object with Longitutde:{self.longtitude}, Latitude {self.latitude}"
    
    # def __eq__(self,object):
    #     return self.__longtitude == object.__longtitude
        
    
    def getLocation(self):
        print(f'Locatioin of point of long {self.longtitude} and lat is {self.latitude}')
        
        
point = Point(1.23,2.239829)

# point.setLontitude(123)
# print(point.getLontitude())

# print(point.__longtitude)

another = Point(1.23,2.239829)


# print(another)

# print(point.getLontitude().__eq__(another.getLontitude()))

# print(point.__eq__(another))

# print(point.longtitude)
# print(point.__latitude)
# point.getLocation()

