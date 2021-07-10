class DnaSequence:
    define_string = "ACGTacgt"

    def __init__(self, string):
        try:
            for i in string:
                try:
                    assert i in DnaSequence.define_string
                except Exception as e:
                    print("error sequence is not valid", e)
        except Exception as e:
            print("error", e)
        self.string = string

    def insert(self, char, index):
        try:
            if index >= len(self.string):
                return "index out of range"
            else:
                if char not in (DnaSequence.define_string):
                    return "not a valid character"
        except Exception as e:
            print("error", e)
            return self.string[:index] + char + self.string[index:]

    def assignment(self, other):
        try:
            if type(other) == DnaSequence:
                matched_list = [characters in DnaSequence.define_string for characters in other.string]
                for i in matched_list:
                    if not i:
                        return "not valid values in string"
                self.string = other.string
            else:
                for i in other:
                    if not i:
                        return "not valid values in string"
                self.string = other

        except Exception as e:
            print("error", e)
        return

    def __eq__(self, other):
        if self.string == other.string:
            return True
        return False

    def __ne__(self, other):
        if self.string != other.string:
            return True
        return False

    def __getitem__(self, item):
        return self.string[item]

    def __len__(self):
        return len(self.string)

    def __str__(self):
        return self.string

# if __name__ == '__main__':
#     a=DnaSequence("AAAA")
#     b=DnaSequence("CCCCC")
#     print(a!=(b))
