# -*- coding = utf-8 -*-
# @Time : 10/21/2023 1:57 AM
# @Author : Lauren
# @File : Number Station.py
# @Software : PyCharm

class Printer:
    def on_message_complete(self, message):
        print(message)


class Decoder:
    def __init__(self, printer):
        self.printer = printer
        self.startFlag = False
        self.hmap = {}
        self.stringBuilder = []
        self.P = Printer()

    def process_sample(self, sequence, character):
        if self.startFlag:
            if character == "-":
                self.startFlag = False
                self.stringBuilder = []
                self.hmap["e"] = sequence
                for k in range(self.hmap["s"] + 1, self.hmap["e"] + 1):
                    if k not in self.hmap:
                        break
                    else:
                        self.stringBuilder.append(self.hmap[k])
                if self.stringBuilder:
                    self.P.on_message_complete("".join(self.stringBuilder))
                self.hmap["s"] = sequence

            else:
                self.hmap[sequence] = character

        else:
            if character == "-":
                self.hmap["s"] = sequence
                self.startFlag = True

            else:
                self.hmap[sequence] = character
