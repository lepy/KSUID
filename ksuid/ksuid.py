from datetime import date
import datetime
import os
import time
# constants


# Used instead of zero(January 1, 1970),, so that the lifespan of KSUIDs will be considerably longer
epochTime = 1400000000
timeStampLength = 4 # number  bytes storing the timestamp
bodyLength = 16 # Number of bytes consisting of the UUID




class KSUID():

    def __init__(self):
        payload = os.urandom(bodyLength) # generates the payload
        currTime = int(time.time())
        # Note, this code may throw an overflow exception, far into the future
        byteEncoding = int(currTime-epochTime).to_bytes(4, byteorder='big')
        print(byteEncoding)
        self.__uid = list(byteEncoding) + list(payload)
        
        
    def getDatetime(self):
        """ getDatetime() returns a python date object which represents the approximate time
        that the ksuid was created """
        
        unixTime = self.getTimestamp()
        return date.fromtimestamp(unixTime)
        
        
        

    def getTimestamp(self):
        """ Returns the value of the timestamp, as a unix timestamp"""
        
        unixTime = int.from_bytes(self.__uid[:timeStampLength], byteorder='big')
        return unixTime + epochTime

    # Returns the payload without the unix timestamp
    def getPayload(self):
        """ Returns the value of the payload, with the timestamp encoded portion removed
        Returns:
             list : An array of integers, that represent the bytes used to encode the UID """
        
        return self.__uid[timeStampLength:]

    def toString(self):
        """ A function to return the UID as a sequence of numbers """
        
        byteString = ""
        for val in self.__uid:
            for dig in str(val):
                byteString += str(ord(dig))
        return byteString


        

