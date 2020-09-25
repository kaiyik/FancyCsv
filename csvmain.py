import unittest


class FancyText:
    InputString = str()

    def __init__(self, inputstring):
        for character in inputstring:
            if character.isalpha() is False:
                if character != ' ':
                    raise TypeError

        self.InputString = inputstring
    
    def converStringToUpperCase(self):
        print(self.InputString.upper())
        return self.InputString.upper()
    
    def convertStringToAlternateUpperLowerCase(self):
        output = str()
        lowerCaseIsTrue = True
        for character in self.InputString:
            if lowerCaseIsTrue is True:
                output += character.lower()
                lowerCaseIsTrue = False
            else:
                output += character.upper()
                lowerCaseIsTrue = True
        print(output)
        return output
    
    def convertStringToCSV(self):
        output = str()
        for character in self.InputString:
            output += character
            output += ','
        output = output[:-1]
        f = open("csvfile.csv", "w")
        f.write(output)
        f.close()
        print("CSV created!")
        return output


class TextTestCase(unittest.TestCase):
    def setUp(self):
        self.text = FancyText('hello world')
    
    def test_ConvertStringToUpperCase(self):
        output = self.text.converStringToUpperCase()
        for character in output:
            if character.isalpha() is True:
                assert character.isupper() is True
    
    def test_convertStringToAlternateUpperLowerCase(self):
        output = self.text.convertStringToAlternateUpperLowerCase()
        lowercaseIsTrue = True
        for character in output:
            if character.isalpha() is True:
                if lowercaseIsTrue is True:
                    assert character.isupper() is False
                    lowercaseIsTrue = False
                else:
                    assert character.isupper() is True
                    lowercaseIsTrue = True
            else:
                lowercaseIsTrue = not lowercaseIsTrue
    
    def test_convertStringToCSV(self):
        self.text.convertStringToCSV()
        with open('csvfile.csv', 'r') as file:
            data = file.read()
        noComma = True
        for character in data:
            if noComma is False:
                assert character == ','
            noComma = not noComma


def InputWHileTrue():
    print('Enter Alphabet Or ' ' Space Only')
    while True:
        try:
            inputtext = input()
            FancyObj = FancyText(inputtext)
            break
        except TypeError:
            print('Enter Alphabet Or ' ' Space Only')
    return FancyObj


FancyObj = InputWHileTrue()
FancyObj.converStringToUpperCase()
FancyObj.convertStringToAlternateUpperLowerCase()
FancyObj.convertStringToCSV()
unittest.main()
