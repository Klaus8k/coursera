from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser


# with open('1.txt','r') as f:
#     sourse = f.read().encode('utf-8')
sourse = input()
class Depth:

    depth = 0
    point = {}

    def start(self, tag, attrib):
        # print(attrib['color'])
        self.depth += 1
        if attrib['color'] in self.point.keys():
            self.point[attrib['color']] += self.depth
        else: self.point[attrib['color']] = self.depth

    def end(self, tag):
        self.depth -= 1

    def close(self):
        return self.point

target = Depth()
parser = XMLParser(target=target)

parser.feed(sourse)

x = parser.close()
print(x['red'],x['green'],x['blue'])







# {'color': 'yellow'}