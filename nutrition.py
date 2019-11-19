class Nutrition():

    def __init__(self, weight, height, age, body_fat, activity_level=0):

        self.activity_level = activity_level
        self.weight = weight
        self.height = height
        self.age = age
        self.body_fat = body_fat
        self.macro_cals = {}
        self.macro_grams = {}

        self.calc()


    def calc(self):
        """ call this function to find new vals"""
        self.BMR = self.calc_BMR(self.weight, self.height, self.age, self.body_fat, )
        self.TDEE = self.estimate_needed_daily_cals(self.BMR, self.activity_level)
        self.macro_cals = self.get_macros(self.TDEE)
        self.macro_grams = self.get_macro_grams(self.macro_cals)
        self.macro_prices = self.get_macro_prices(self.macro_grams)
        self.one_week_cost = self.get_cost_for_one_week(self.macro_prices)

    def calc_BMR(self, weight, height, age, body_fat, ):
        """
            where:

            W is body weight in kg
            H is body height in cm
            A is age
            F is body fat in percentage

            for males only"""

        BMR0 = 10 * weight + 6.25 * height - 5 * age + 5
        BMR1 = 13.397 * weight + 4.799 * height - 5.677 * age + 88.362
        BMR2 = 370 + 21 * (1 - body_fat) * weight
        return (BMR0 + BMR1 + BMR2) / 3

    def estimate_needed_daily_cals(self, BMR, activity_level=0):
        """ details at https://www.k-state.edu/paccats/Contents/PA/PDF/Physical%20Activity%20and%20Controlling%20Weight.pdf"""
        TDEE = 0

        if activity_level == 0:
            print('sedentary')
            TDEE = BMR * 1.2
        elif activity_level == 1:
            TDEE = BMR * 1.375
        elif activity_level == 2:
            TDEE = BMR * 1.55
        elif activity_level == 3:
            TDEE = BMR * 1.725
        elif activity_level == 4:
            TDEE = BMR * 1.9

        return TDEE

    def get_macros(self,TDEE):
        """ gets how many calories should come from which macro """
        macros = ['protein', 'carbs', 'fats']
        percents = [0.2, 0.65, 0.15]

        macros_cals = {}

        for macro,percent in zip(macros,percents):
            macros_cals[macro] = TDEE*percent

        return macros_cals

    def get_macro_grams(self,macros_cals):
        """ reveals how many grams are present for each macro """
        macros_grams = {}
        for key,val in macros_cals.items():
            cal_per_g = 4
            if key == 'fats':
                cal_per_g = 9

            macros_grams[key] = val/cal_per_g

        return macros_grams

    def get_macro_prices(self,macros_grams):
        """

        prices are from:
        protein: price of ground beef
        carbs: price of rice
        fats: price of vegetable oil



        """

        macros_price = {}
        for key,val in macros_grams.items():
            price_per_macro_gram = 0
            if key == 'protein':
                price_per_macro_gram = 0.0016800000000000003
            elif key == 'carbs':
                price_per_macro_gram = 0.04760000000000001
            elif key == 'fats':
                price_per_macro_gram = 0.0014880000000000002

            macros_price[key] = val*price_per_macro_gram

        return macros_price


    def get_cost_for_one_week(self,macros_price):
        cost = 0

        for key,val in macros_price.items():
            cost += val*7

        return cost


nutrition = Nutrition(74.8427,188,26,0.07,activity_level=1)
print(nutrition.TDEE)
print(nutrition.macro_prices)
print(nutrition.one_week_cost)

