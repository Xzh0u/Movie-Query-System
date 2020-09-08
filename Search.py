import csv


class MovieItems(object):
    def __init__(self, filename: str):
        self.filename = filename

    # taged movie items
    def getTagedItems(self, tag: dict):
        pass

    # sorted movie items
    def getSortedItems():
        pass

    # all movie items
    def getAllItems(filename: str):
        with open('Movies250.csv') as f:
            a = [{k: v
                  for k, v in row.items()}
                 for row in csv.DictReader(f, skipinitialspace=True)]
        return a


if __name__ == "__main__":
    print(allMovieItems())