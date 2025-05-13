class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def is_bulky(self):
        volume = self.width * self.height * self.length
        return volume >= 1_000_000 or max(self.width, self.height, self.length) >= 150

    def is_heavy(self):
        return self.mass >= 20

    def get_category(self):
        bulky = self.is_bulky()
        heavy = self.is_heavy()

        if bulky and heavy:
            return "REJECTED"
        elif bulky or heavy:
            return "SPECIAL"
        else:
            return "STANDARD"
def main():
    packages = [
        Package(100, 100, 100, 10),
        Package(200, 200, 200, 30),
        Package(50, 50, 50, 5),
        Package(150, 150, 150, 25),
        Package(10, 10, 10, 15)
    ]

    for package in packages:
        print(f"Package: {package.width}x{package.height}x{package.length}, Mass: {package.mass}kg - Category: {package.get_category()}")
if __name__ == "__main__":
    main()
# The code defines a Package class with methods to determine if a package is bulky or heavy based on its dimensions and mass.