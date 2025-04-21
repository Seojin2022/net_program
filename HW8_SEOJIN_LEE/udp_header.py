import struct

class Udphdr:
    def __init__(self, srcPort, dstPort, length, checksum):
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.srcPort, self.dstPort, self.length, self.checksum)

    def unpack_Udphdr(self, packet):
        self.srcPort, self.dstPort, self.length, self.checksum = struct.unpack('!HHHH', packet)

    def getSrcPort(self):
        return self.srcPort

    def getDstPort(self):
        return self.dstPort

    def getLength(self):
        return self.length

    def getChecksum(self):
        return self.checksum



udp = Udphdr(5555, 80, 1000, 0xFFFF)

packed = udp.pack_Udphdr()
print(packed)  

unpacked = struct.unpack('!HHHH', packed)
print(unpacked) 

udp2 = Udphdr(0, 0, 0, 0)
udp2.unpack_Udphdr(packed)
print(f"Source Port:{udp2.getSrcPort()} Destination Port:{udp2.getDstPort()} Length:{udp2.getLength()} Checksum:{udp2.getChecksum()}")