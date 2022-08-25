class IndianFilmIndustry:
    def __init__(self, industry, language):
        self.industry = industry
        self.language = language

    def __str__(self):
        return "Industry : " + self.industry + "\nLanguage : " + self.language

    def print_wishes(self):
        return "All the very best!"


class Sandalwood(IndianFilmIndustry):
    def classname(self):
        return "Class name is Sandalwood"


class Kodava(Sandalwood):
    def info(self):
        return "This is just an info"


kfi = Kodava("Sandalwood", "Kodava")
print(kfi)
print(kfi.print_wishes())
print(kfi.classname())
print(kfi.info())