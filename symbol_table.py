class SymbolTable:
    def __init__(self):
        self.sTable  = list()

    def lookup(self, name, type, scope):
        '''
        -> Checks if the identifier already exists in the Symbol Table or not 
        -> Returns a boolean value to show if the identifier exists or nor
        '''
        if len(self.sTable) == 0:
            return False

        for entry in self.sTable:
            if (entry.name == name) and (entry.type == type) and (entry.scope == scope):
                return True
        return False

    def enter(self, name, type, size, scope):
        '''
        -> Creates an entry in the Symbol Table when declared, after checking for redeclerations
        -> In that entry, the name, type, size and scope of entry is declared
        '''
        entry = Entry(name, type, size, scope)
        self.sTable.append(entry)

    def return_type(self, name, scope):
        '''
        -> It checks and verifies the type on both ends and returns the correct type
        -> The scope is an integer value that would increase as the depth increases for each variable or statement
        '''
        if len(self.sTable) != 0:
            for entry in self.sTable:
                if entry.name == name:
                    if (entry.scope != scope and entry.scope == 0) or (entry.scope == scope):
                        return entry.type
            return None

    def st_generator(self) -> None:
        '''
        -> This is used to display the symbol table and ensure that the entries are created successfully
        '''
        for entry in self.sTable:
            print("Name: ", entry.name)
            print("Type: ", entry.type)
            print("Size: ", entry.size)
            print("Scope: ", entry.scope)

class Entry:
    '''
    -> The entry class will be used to create an entry in the Symbol Table
    '''
    def __init__(self, name, type, size, scope):
        self.name = name
        self.type = type
        self.size = size
        self.scope = scope



