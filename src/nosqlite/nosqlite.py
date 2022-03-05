import json

class NoSQLite:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r+')
        self.jsonData = json.load(self.file)

    def reload(self):
        self.file = open(self.filename, 'r+')
        self.jsonData = json.load(self.file)

    def writeOut(self):
        self.file.seek(0)
        self.file.write(json.dumps(self.jsonData))
        self.file.truncate()
        self.file.close()
        self.reload()
    
    def create_table(self, tableName):
        if tableName in self.jsonData:
            return False
        else:
            self.jsonData[tableName] = []
            self.writeOut()
            return True

    def insert(self, data, table):
        if table in self.jsonData:
            self.jsonData[table].append(data)
        else:
            self.jsonData[table] = [data]
        self.writeOut()

    def delete(self, data, table):
        for item in self.jsonData[table]:
                for sk, _ in data.items():
                    if item[sk] == data[sk]:
                        self.jsonData[table].remove(item)
                        self.writeOut()
                        return item
    
    def update(self, data, newData, table):
        for v, item in enumerate(self.jsonData[table]):
                for sk, _ in data.items():
                    if item[sk] == data[sk]:
                        self.jsonData[table][v] = newData
                        self.writeOut()
                        return True
        return False

    def find(self, search, table):
        found = []
        for item in self.jsonData[table]:
            mf = False
            for sk, _ in search.items():
                if sk in item:
                    if item[sk] == search[sk]:
                        mf = True
                    elif item[sk] != search[sk] and mf:
                        mf = False
                        break
            if mf:
                found.append(item)
        return found