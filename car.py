class Car:
    def __init__(self,company,model,year,color):
        self.company = company
        self.model = model
        self.year = year
        self.color = color

    def manufacturing(self):
        print('This '+self.model+' in '+self.company+' is manufacturing.')

    def not_manufacturing(self):
        print('This car is not manufacturing anymore.')
