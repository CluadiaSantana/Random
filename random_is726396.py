import os
import nacl.utils

class randomPynacl():
    def __init__(self, bytes):
        self._bytes = bytes
        self._buf= nacl.utils.random(self._bytes)
    
    def changeBits(self,bytes):
        self._bytes = bytes
    
    def Random(self):
        self._buf= nacl.utils.random(self._bytes)

    def PrintRandom(self):
        for number in self._buf:
            print(f'{hex(number)[2:]}',end = " ")

if __name__ == "__main__":
    random=randomPynacl(256)
    random.PrintRandom()
