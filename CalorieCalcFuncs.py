import pandas as pd
preference = (input("Type Bulk, Cut, or Maintain")).lower()
weight = int(input("Type In Your Weight: "))


class body:
    def __init__(self, weight,preference):
        self.weight = weight
        self.preference = preference
def maintain(self):
    if preference == "maintain":
        Goal = []
        Target = []
        Maintinence_Cals = []
        Protein = []
        Carbs = []
        Fat = []
        x = weight * 14
        pro = round((x * .4)/4)
        c = round((x * .4)/4)
        f = round((x * .2)/9)
        Goal.append("Maintenence")
        Maintinence_Cals.append(x)
        Protein.append(pro)
        Carbs.append(c)
        Fat.append(f)
        Target.append(0)
        columns = ["Goal", "Calories", "Protein", "Carbs", "Fat"]
        df = pd.DataFrame(list(zip(Goal, Maintinence_Cals, Protein, Carbs, Fat)), columns=columns)
def bulk(self):
        Goal = []
        Target = []
        Maintinence_Cals = []
        Protein = []
        Carbs = []
        Fat = []
        lbsperweek = []
        x = (weight * 14) + 500
        pro = round((x * .35)/4)
        c = round((x * .45)/4)
        f = round((x * .15)/9)
        Goal.append("Bulking")
        lbsperweek.append(1)
        Maintinence_Cals.append(x)
        Protein.append(pro)
        Carbs.append(c)
        Fat.append(f)
        Goal.append("Bulking")
        lbsperweek.append(2)
        x = (weight * 14) + 1000
        pro = round((x * .35) / 4)
        c = round((x * .45) / 4)
        f = round((x * .15) / 9)
        Maintinence_Cals.append(x)
        Protein.append(pro)
        Carbs.append(c)
        Fat.append(f)
        columns = ["Goal","PoundsPerWeek", "Calories", "Protein", "Carbs", "Fat"]
        df = pd.DataFrame(list(zip(Goal, lbsperweek, Maintinence_Cals, Protein, Carbs, Fat)), columns=columns)
        print(df)
def cut(self):
        Goal = []
        Maintinence_Cals = []
        Protein = []
        Carbs = []
        Fat = []
        lbsperweek = []
        x = (weight * 14) - 500
        pro = round((x * .5) / 4)
        c = round((x * .2) / 4)
        f = round((x * .3) / 9)
        Goal.append("Cutting")
        lbsperweek.append(1)
        Maintinence_Cals.append(x)
        Protein.append(pro)
        Carbs.append(c)
        Fat.append(f)
        Goal.append("Cutting")
        lbsperweek.append(2)
        x = (weight * 14) - 1000
        pro = round((x * .5) / 4)
        c = round((x * .2) / 4)
        f = round((x * .3) / 9)
        Maintinence_Cals.append(x)
        Protein.append(pro)
        Carbs.append(c)
        Fat.append(f)
        columns = ["Goal", "PoundsPerWeek", "Calories", "Protein", "Carbs", "Fat"]
        df = pd.DataFrame(list(zip(Goal, lbsperweek, Maintinence_Cals, Protein, Carbs, Fat)), columns=columns)
        print(df)


Subject = body(weight,preference)

funct_dict = {"maintain":maintain, "bulk":bulk,"cut":cut}

funct_dict[preference](Subject)



