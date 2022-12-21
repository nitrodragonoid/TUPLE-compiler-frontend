from symbol_table import SymbolTable, Entry

class dfa:
    def __init__(self, dfa, space = False):
        self.states = dfa[0].split()
        self.alphabets = dfa[1].split()
        self.start = dfa[2]
        self.accept = dfa[3].split()
        rest = dfa[4:]
        self.transition = {}
        if space == True:
            for i in rest:
                self.transition[(i[0],i[1])] = i[2]
        else:
            for i in rest:
                pair = i.split()
                self.transition[(pair[0],pair[1])] = pair[2]

    def accepts(self, w: str):
        current = self.start
        for char in w:
            if (current, char) in self.transition.keys():
                current = self.transition[(current,char)]
            else:
                return False
        if current in self.accept:
            return True
        return False



class lexer:
    def __init__(self):
        self.keywords = dfa(["1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33", "a b c d e f g h i j k l m n o p q r s t u v w x y z", "1","4", "1 a 2","2 n 3","3 d 4", "1 b 5", "5 r 6", "6 e 7", "7 a 8", "8 k 4", "1 c 9", "9 o 10", "10 n 11", "11 t 12", "12 i 13", "13 n 14", "14 u 15", "15 e 4", "1 e 16", "16 l 17", "17 s 15", "1 f 18", "18 a 16", "1 f 18", "18 o 19", "19 r 4", "1 i 20", "20 f 4", "1 m 21", "21 o 3", "1 n 22", "22 o 23", "23 t 4", "1 o 24", "24 r 4", "1 t 25", "25 h 26", "26 e 27", "27 n 4", "1 t 25", "25 r 28", "28 u 15", "1 v 29", "29 o 30", "30 i 3", "1 w 31", "31 h 32", "32 i 33", "33 l 15"])
        
        self.identifiers = dfa(["q1 q2", "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 _" , "q1", "q2", "q1 a q2", "q1 b q2", "q1 c q2", "q1 d q2", "q1 e q2", "q1 f q2", "q1 g q2", "q1 h q2", "q1 i q2", "q1 j q2", "q1 k q2", "q1 l q2", "q1 m q2", "q1 n q2", "q1 o q2", "q1 p q2", "q1 q q2", "q1 r q2", "q1 s q2", "q1 t q2", "q1 u q2", "q1 v q2", "q1 w q2", "q1 x q2", "q1 y q2", "q1 z q2", "q2 a q2", "q2 b q2", "q2 c q2", "q2 d q2", "q2 e q2", "q2 f q2", "q2 g q2", "q2 h q2", "q2 i q2", "q2 j q2", "q2 k q2", "q2 l q2", "q2 m q2", "q2 n q2", "q2 o q2", "q2 p q2", "q2 q q2", "q2 r q2", "q2 s q2", "q2 t q2", "q2 u q2", "q2 v q2", "q2 w q2", "q2 x q2", "q2 y q2", "q2 z q2", "q2 A q2", "q2 B q2", "q2 C q2", "q2 D q2", "q2 E q2", "q2 F q2", "q2 G q2", "q2 H q2", "q2 I q2", "q2 J q2", "q2 K q2", "q2 L q2", "q2 M q2", "q2 N q2", "q2 O q2", "q2 P q2", "q2 Q q2", "q2 R q2", "q2 S q2", "q2 T q2", "q2 U q2", "q2 V q2", "q2 W q2", "q2 X q2", "q2 Y q2", "q2 Z q2", "q2 1 q2", "q2 2 q2", "q2 3 q2", "q2 4 q2", "q2 5 q2", "q2 6 q2", "q2 7 q2", "q2 8 q2", "q2 9 q2", "q2 0 q2", "q2 _ q2"])
        
        self.data_type = dfa(["1 2 3 4 5 6 7 8 9 10 11 12 13 14", "a b c d e f g h i j k l m n o p q r s t u v w x y z", "1", "5", "1 b 2", "2 o 3", "3 o 4", "4 l 5", "1 c 6", "6 h 7", "7 a 8", "8 r 5", "1 i 9", "9 n 10", "10 t 5", "1 f 11", "1l l 12", "12 o 13", "13 a 14", "14 t 5"])
        
        self.puntuators = dfa(["1 2", R'{ } ( ) ; [ ] ’ ” , .', "1", "2", "1 { 2", "1 } 2", "1 ( 2", "1 ) 2", "1 ; 2", "1 [ 2", "1 ] 2", "1 ' 2", R'1 " 2', "1 , 2", "1 . 2" ])
        
        self.number = dfa(["q1 q2 q3 q4", "0 1 2 3 4 5 6 7 8 9 - E", "q1", "q2", "q1 0 q2", "q1 1 q2", "q1 2 q2", "q1 3 q2", "q1 4 q2", "q1 5 q2", "q1 6 q2", "q1 7 q2", "q1 8 q2", "q1 9 q2", "q1 - q3", "q3 0 q2", "q3 1 q2", "q3 2 q2", "q3 3 q2", "q3 4 q2", "q3 5 q2", "q3 6 q2", "q3 7 q2", "q3 8 q2", "q3 9 q2", "q2 E q4", "q4 0 q2", "q4 1 q2", "q4 2 q2", "q4 3 q2", "q4 4 q2", "q4 5 q2", "q4 6 q2", "q4 7 q2", "q4 8 q2", "q4 9 q2", "q2 0 q2", "q2 1 q2", "q2 2 q2", "q2 3 q2", "q2 4 q2", "q2 5 q2", "q2 6 q2", "q2 7 q2", "q2 8 q2", "q2 9 q2",])
        
        self.strings = dfa(["1 2 3",R'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 _ { }   ( ) ; [ ] ’ ” , < > = + - ! @ # $ % ^ & * | ? /',"1","3",["1",'"', "2"], ["2", '"', "3"],["2","a","2"],["2","b","2"],["2", "c","2"],["2", "d","2"],["2", "e","2"], ["2","f","2"],["2", "g","2"],["2", "h","2"],["2", "i","2"],["2", "j","2"],["2", "k","2"],["2", "l","2"], ["2","m","2"],["2", "n","2"],["2","o","2"],["2", "p","2"],["2", "q","2"],["2", "r","2"],["2", "s","2"],["2", "t","2"],["2" ,"u","2"],["2", "v","2"],["2", "w","2"],["2", "x","2"],["2", "y","2"],["2", "z","2"],["2","A","2"],["2", "B","2"],["2", "C","2"],["2", "D","2"],["2", "E","2"],["2", "F","2"],["2", "G","2"],["2", "H","2"],["2", "I","2"],["2","J","2"],["2", "K","2"],["2", "L","2"],["2", "M","2"],["2", "N","2"],["2", "O","2"],["2", "P","2"],["2","Q","2"],["2", "R","2"],["2", "S","2"],["2", "T","2"],["2", "U","2"],["2", "V","2"],["2", "W","2"],["2", "X","2"],["2", "Y","2"],["2", "Z","2"],["2","0","2"],["2", "1","2"],["2", "2","2"],["2", "3","2"],["2", "4","2"],["2", "5","2"],["2", "6","2"],["2", "7","2"],["2", "8","2"],["2", "9","2"],["2", "_","2"],["2", "{","2"],["2", "}","2"],["2","(","2"],["2", ")","2"],["2",";","2"],["2","[","2"],["2", "]","2"],["2","’","2"],["2", "”","2"],["2",",","2"],["2", "<","2"],["2", ">","2"],["2","=","2"], ["2","+","2"],["2","-","2"],["2", "!","2"],["2", "@","2"],["2", "#","2"],["2","$","2"],["2", "%","2"],["2", "^","2"],["2", "&","2"],["2", "*","2"],["2", "|","2"],["2", "?","2"],["2", "/","2"],["2", " ","2"],["2", ".","2"]], True)
        
        self.comment = dfa(["1 2 3 4 5",R'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 _ { }   ( ) ; [ ] ’ ” , < > = + - ! @ # $ % ^ & * | ? /',
                            "1","5",["1","/", "3"], ["3", "$", "2"], ["2", "$", "4"], ["4", "/", "5"],
                            ["2","a","2"],["2","b","2"],["2", "c","2"],["2", "d","2"],["2", "e","2"], ["2","f","2"],["2", "g","2"],["2", "h","2"],["2", "i","2"],["2", "j","2"],["2", "k","2"],["2", "l","2"], ["2","m","2"],["2", "n","2"],["2","o","2"],["2", "p","2"],["2", "q","2"],["2", "r","2"],["2", "s","2"],["2", "t","2"],["2" ,"u","2"],["2", "v","2"],["2", "w","2"],["2", "x","2"],["2", "y","2"],["2", "z","2"],["2","A","2"],["2", "B","2"],["2", "C","2"],["2", "D","2"],["2", "E","2"],["2", "F","2"],["2", "G","2"],["2", "H","2"],["2", "I","2"],["2","J","2"],["2", "K","2"],["2", "L","2"],["2", "M","2"],["2", "N","2"],["2", "O","2"],["2", "P","2"],["2","Q","2"],["2", "R","2"],["2", "S","2"],["2", "T","2"],["2", "U","2"],["2", "V","2"],["2", "W","2"],["2", "X","2"],["2", "Y","2"],["2", "Z","2"],["2","0","2"],["2", "1","2"],["2", "2","2"],["2", "3","2"],["2", "4","2"],["2", "5","2"],["2", "6","2"],["2", "7","2"],["2", "8","2"],["2", "9","2"],["2", "_","2"],["2", "{","2"],["2", "}","2"],["2","(","2"],["2", ")","2"],["2",";","2"],["2","[","2"],["2", "]","2"],["2","’","2"],["2", "”","2"],["2",",","2"],["2", "<","2"],["2", ">","2"],["2","=","2"], ["2","+","2"],["2","-","2"],["2", "!","2"],["2", "@","2"],["2", "#","2"],["2", "%","2"],["2", "^","2"],["2", "&","2"],["2", "*","2"],["2", "|","2"],["2", "?","2"],["2", "/","2"],["2", " ","2"],["2", ".","2"]
                            ,["4","a","2"],["4","b","2"],["4", "c","2"],["4", "d","2"],["4", "e","2"], ["4","f","2"],["4", "g","2"],["4", "h","2"],["4", "i","2"],["4", "j","2"],["4", "k","2"],["4", "l","2"], ["4","m","2"],["4", "n","2"],["4","o","2"],["4", "p","2"],["4", "q","2"],["4", "r","2"],["4", "s","2"],["4", "t","2"],["4" ,"u","2"],["4", "v","2"],["4", "w","2"],["4", "x","2"],["4", "y","2"],["4", "z","2"],["4","A","2"],["4", "B","2"],["4", "C","2"],["4", "D","2"],["4", "E","2"],["4", "F","2"],["4", "G","2"],["4", "H","2"],["4", "I","2"],["4","J","2"],["4", "K","2"],["4", "L","2"],["4", "M","2"],["4", "N","2"],["4", "O","2"],["4", "P","2"],["4","Q","2"],["4", "R","2"],["4", "S","2"],["4", "T","2"],["4", "U","2"],["4", "V","2"],["4", "W","2"],["4", "X","2"],["4", "Y","2"],["4", "Z","2"],["4","0","2"],["4", "1","2"],["4", "2","2"],["4", "3","2"],["4", "4","2"],["4", "5","2"],["4", "6","2"],["4", "7","2"],["4", "8","2"],["4", "9","2"],["4", "_","2"],["4", "{","2"],["4", "}","2"],["4","(","2"],["4", ")","2"],["4",";","2"],["4","[","2"],["4", "]","2"],["4","’","2"],["4", "”","2"],["4",",","2"],["4", "<","2"],["4", ">","2"],["4","=","2"], ["4","+","2"],["4","-","2"],["4", "!","2"],["4", "@","2"],["4", "#","2"],["4","$","2"],["4", "%","2"],["4", "^","2"],["4", "&","2"],["4", "*","2"],["4", "|","2"],["4", "?","2"],["4", " ","2"],["2", ".","2"]], True)
        
        self.relationalOp = dfa(["1 2 3 4", "< > = !", "1","2 3", "1 < 2", "1 > 2", "2 = 3", "1 = 4", "1 ! 4", "4 = 3",])
        
        self.arthemeticOp = dfa(["1 2", "+ - * / ^ =", "1", "2", "1 + 2", "1 - 2", "1 * 2", "1 / 2", "1 ^ 2", "1 = 2"])
        
        self.tokkens = []
        self.Tok = []
        self.lines = []
        self.symbol = {}
        self.errors = list()
        self.par = list()
        
    def scan(self, text):
        current = 0
        text += " "
        id = 1
        line = 1
        self.lines = []
        self.errors = []
        for i in range(len(text)):
            inp = text[current:i]
            accept = False
            if i<len(text)-1:
                if text[i:i+1] == "\n":
                    line += 1
            if self.comment.accepts(inp):
                current = i
                accept = True
            elif self.strings.accepts(inp):
                accept = True
                if len(inp) == 3:
                    self.tokkens.append("<character>".format(inp))
                    self.Tok.append("character".format(inp))
                    self.lines.append(line)
                    self.par.append(inp)
                else:
                    self.tokkens.append("<literal>".format(inp))
                    self.Tok.append("literal".format(inp))
                    self.par.append(inp)
                    self.lines.append(line)
                current = i
                
            elif inp == " " or inp == "\n" or inp == "\t":
                accept = True
                # if inp == "\n":
                #     line += 1
                current = i
            elif self.puntuators.accepts(inp):
                accept = True
                self.tokkens.append("<{0}>".format(inp))
                self.Tok.append("{0}".format(inp))
                self.lines.append(line)
                self.par.append(inp)
                current = i
            elif self.keywords.accepts(inp) and not self.keywords.accepts(text[current:i+1]):
                accept = True
                if inp == "void":
                    self.tokkens.append("<dt>")
                    self.Tok.append("dt")
                    self.par.append(inp)
                    self.lines.append(line)
                else:
                    self.tokkens.append("<{0}>".format(inp))
                    self.Tok.append("{0}".format(inp))
                    self.par.append(inp)
                    self.lines.append(line)
                current = i
            elif self.data_type.accepts(inp) and not self.data_type.accepts(text[current:i+1]):
                accept = True
                self.tokkens.append("<dt>")
                self.Tok.append("dt")
                self.par.append(inp)
                self.lines.append(line)
                self.par.append(inp)
                current = i
            elif self.identifiers.accepts(inp) and not self.identifiers.accepts(text[current:i+1]):
                accept = True
                if inp not in self.symbol.keys():
                    self.symbol[inp] = id
                    id += 1
                    self.tokkens.append("<id>")
                    self.Tok.append("id")
                    self.par.append(inp)
                    self.lines.append(line)
                else:
                    self.tokkens.append("<id>")
                    self.Tok.append("id")
                    self.par.append(inp)
                    self.lines.append(line)
                current = i
            elif self.relationalOp.accepts(inp) and not self.relationalOp.accepts(text[current:i+1]):
                accept = True
                self.tokkens.append("<{0}>".format(inp))
                if inp == "=":
                    self.Tok.append("{0}".format(inp))
                    self.par.append(inp)
                else:
                    self.Tok.append("{0}".format("relop"))
                    self.par.append(inp)
                self.lines.append(line)
                current = i
            elif self.arthemeticOp.accepts(inp) and not self.arthemeticOp.accepts(text[current:i+1]) and (text[current:i+1] != "/$"):
                accept = True
                self.tokkens.append("<{0}>".format(inp))
                self.Tok.append("{0}".format(inp))
                self.par.append(inp)
                self.lines.append(line)
                current = i
            elif self.number.accepts(inp) and not self.number.accepts(text[current:i+1]):
                accept = True
                self.tokkens.append("<id>".format(inp))
                self.Tok.append("id".format(inp))
                self.par.append(inp)
                self.lines.append(line)
                current = i
            if i == len(text) - 1 and accept == False:
                self.errors.append("Lexical error found at line number {0}".format(line))
           
        return self.tokkens
        
    def tokenize(self,file):
        f = open(file, "r")
        txt = str(f.read())
        tokkens = self.scan(txt)
        out = open(file+".out","w+")
        for i in tokkens:
            out.write(i)
        sym = open(file+".sym","w+")
        for i in self.symbol:
            t = str(i)+":"+str(self.symbol[i])+"\n"
            sym.write(t)
        return self.errors

class CFG():
    def __init__(self, V, T, R, S):
        self.V = list(V)
        self.T = list(T)
        self.R = dict(R)
        self.S = str(S)
            
    
    def FIRST(self,v): #for variables
        firstSet  = set()
        for i in self.R[v]:
            if len(i) > 0:
                firstSet.add(i[0])
        return firstSet
    
    def FIRST_T(self,v): #for terminals
        firstSet  = set()
        for i in self.R[v]:
            if len(i) > 0:
                firstSet.add(i[0])
        return firstSet
    
    def FOLLOW(self,v):
        followSet = set()
        
        for i in self.V:
            for j in self.R[i]:
                if v in j:
                    ind  = j.index(v)
                    if ind + 1 == len(j):
                        followSet.add[self.FOLLOW(i)]
                    elif j[ind+1] in self.V:
                        followSet.add(self.FIRST(j[ind+1]))
                    else:
                        followSet.add(self.FIRST_T(j[ind+1]))                
        return followSet
    
class Parser():
    
    def __init__(self):
        #TODO: add all the grammar
        self.G = CFG(["Program","ParamList","PList", "Stmts","A","S","DecStmts","List","OptionalAssign","AssignStmt","Expr","ForStmt","Type","IfStmt","OptionalElse","ReturnStmt","E'","T","T'","F"], 
                     ["dt","id","(",")","{","}",",","E",";","=","for","relop","++","if","else","return","+","*","-","/"], 
                     {"Program":[["dt","id","(","ParamList",")","{","Stmts","}"]],
                      "ParamList":[["dt","id","PList"],["E"]],
                      "PList":[[",","dt","id","PList"],["E"]],
                      "Stmts":[["S"]],
                      "S":[["dt","id","OptionalAssign","List","S"],
                           ["id","=","Expr",";","S"],
                           ["for","(","Type","id", "Expr",";","Expr","relop","Expr",";","id","++",")","{","Stmts","}","S"],
                           ["if","(","Expr","relop","Expr",")","{","Stmts","}","OptionalElse","S"],
                           ["return","Expr",";","S"],
                           ["E"]], 
                      "DecStmts":[["dt","id","OptionalAssign","List"]],
                      "OptionalAssign":[["=","Expr",";"],["E"]],
                      "AssignStmt":[["id","=","Expr",";"]],
                      "Expr":[["T","E'"]],
                      "E'":[["+","T","E'"],["-","T","E'"],["E"]],
                      "T":[["F","T'"]],
                      "T'":[["*","F","T'"],["/","F","T'"],["E"]],
                      "F":[["(","Expr",")"],["id"]],
                      "ForStmt":[["for","(","Type","id", "Expr",";","Expr","relop","Expr",";","id","++",")","{","Stmts","}"]],
                      "Type":[["dt"],["E"]],
                      "IfStmt":[["if","(","Expr","relop","Expr",")","{","Stmts","}","OptionalElse"]],
                      "OptionalElse":[["else","{","Stmts","}"],["E"]],
                      "ReturnStmt":[["return","Expr",";"]]
                      }, 
                     "Program")
        self.trace = list()
        self.pointer = 0
        self.string = list()
        self.symTab = SymbolTable()
        self.parallel = list()
        
    def A(self,id,dt,size = 1,scope = 1):
        if self.symTab.lookup(id, dt, scope) == False:
            self.symTab.enter(id,dt,size,scope)
        # pass
    # enter(self, name, type, size, scope)
    
    def B(self):
        pass
    
    def C(self):
        pass
    
    def D(self):
        pass
    
    def E(self,operator1,operator2, operand,scope = 1):
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == ">":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "<":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "==":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == ">=":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "<=":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == ">":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "<":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "==":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == ">=":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "<=":
            return True 
        if self.symTab.return_type(operator1, scope) == "str" and self.symTab.return_type(operator2, scope) == "str" and operand == "==":
            return True 
    
        
    
    def F(self,operator1,operator2, operand,scope = 1):
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "+":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "-":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "*":
            return True 
        if self.symTab.return_type(operator1, scope) == "int" and self.symTab.return_type(operator2, scope) == "int" and operand == "/":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "+":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "-":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "*":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "/":
            return True 
        if self.symTab.return_type(operator1, scope) == "float" and self.symTab.return_type(operator2, scope) == "float" and operand == "+":
            return True 
        
        
    def G(self):
        pass
        

    def Program(self,pointer):
        A = str("Program")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "ParamList":
                        pointer = self.ParamList(pointer)
                    if X == "Stmts":
                        pointer = self.Stmts(pointer)
                elif X == self.string[pointer]:
                    if X == "id":
                        self.A(self.parallel[pointer-1],self.parallel[pointer])
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count +=1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    
    def ParamList(self,pointer):
        A = str("ParamList")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "PList":
                        pointer = self.PList(pointer)
                        
                elif X == self.string[pointer]:
                    if X == "id":
                        self.A(self.parallel[pointer-1],self.parallel[pointer])
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    
    def PList(self,pointer):
        A = str("PList")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "PList":
                        pointer = self.PList(pointer)
                        
                elif X == self.string[pointer]:
                    if X == ";":
                        self.A(self.parallel[pointer-2],self.parallel[pointer-1])
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def Stmts(self,pointer):
        A = str("Stmts")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "S":
                        pointer = self.S(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def S(self,pointer):
        A = str("S")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "DecStmts":
                        pointer = self.DecStmts(pointer)
                    if X == "AssignStmt":
                        pointer = self.AssignStmt(pointer)
                    if X == "ForStmt":
                        pointer = self.ForStmt(pointer)
                    if X == "IfStmt":
                        pointer = self.IfStmt(pointer)
                    if X == "ReturnStmt":
                        pointer = self.ReturnStmt(pointer)   
                    if X == "S":
                        pointer = self.S(pointer)
                        
                elif X == self.string[pointer]:
                    if X == "id":
                        self.A(self.parallel[pointer-1],self.parallel[pointer])
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def DecStmts(self,pointer):
        A = str("DecStmts")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "OptionalAssign":
                        pointer = self.OptionalAssign(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def List(self,pointer):
        A = str("List")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "OptionalAssign":
                        pointer = self.OptionalAssign(pointer)
                    if X == "List":
                        pointer = self.List(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def OptionalAssign(self,pointer):
        A = str("OptionalAssign")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "Expr":
                        pointer = self.Expr(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def AssignStmt(self,pointer):
        A = str("AssignStmt")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "Expr":
                        pointer = self.Expr(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count +=1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def Expr(self,pointer):
        A = str("Expr")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "T":
                        pointer = self.T(pointer)
                    if X == "E'":
                        pointer = self.E_(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def E_(self,pointer):
        A = str("E'")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0 
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "T":
                        pointer = self.T(pointer)
                    if X == "E'":
                        pointer = self.E_(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count +=1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def T(self,pointer):
        A = str("T")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count =0
            for X in P:
                if X in self.G.V:
                    if X == "F":
                        pointer = self.F(pointer)
                    if X == "T''":
                        pointer = self.T_(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count +=1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def T_(self,pointer):
        A = str("T'")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "F":
                        pointer,lexeme1 = self.F(pointer)
                    if X == "T'":
                        pointer,lexeme2 = self.T_(pointer)
                        self.E(self, lexeme1,lexeme2 ,"*")
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count +=1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer, lexeme1
    
    def F(self,pointer):
        A = str("F")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "Expr":
                        pointer,lexeme = self.Expr(pointer)
                        
                elif X == self.string[pointer]:
                    if X == "id":
                        lexeme = self.parallel[pointer]
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count  += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return (pointer, lexeme)
    
    def ForStmt(self,pointer):
        A = str("ForStmt")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "Type":
                        pointer = self.Type(pointer)
                    if X == "Expr":
                        pointer = self.Expr(pointer)
                    if X == "Stmts":
                        pointer = self.Stmts(pointer)
                        
                elif X == self.string[pointer]:
                    if X == ";":
                        self.E(self.parallel[pointer-3],self.parallel[pointer-1],self.parallel[pointer-2])
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def Type(self,pointer):
        A = str("Type")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    pass
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def IfStmt(self,pointer):
        A = str("IfStmt")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "Expr":
                        pointer = self.Expr(pointer)
                    if X == "Stmts":
                        self.Stmts(pointer)
                    if X == "OptionalElse":
                        pointer = self.OptionalElse(pointer)
                        
                elif X == self.string[pointer]:
                    if X == ")":
                        self.E(self.parallel[pointer-3],self.parallel[pointer-1],self.parallel[pointer-2])
                    
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def OptionalElse(self,pointer):
        A = str("OptionalElse")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X == "E":
                    continue
                if X in self.G.V:
                    if X == "Stmts":
                        pointer = self.Stmts(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer +=  1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
    
    def ReturnStmt(self,pointer):
        A = str("ReturnStmt")
        # print(A,":",self.string[pointer])
        for P in self.G.R[A]:
            count = 0
            for X in P:
                if X in self.G.V:
                    if X == "Expr":
                        pointer = self.Expr(pointer)
                        
                elif X == self.string[pointer]:
                    self.trace.append("matched <{0}>".format(self.string[pointer]))
                    pointer += 1
                    count += 1
                    if pointer == len(self.string):
                        print("accepted")
                        return True
                else:
                    pointer -= count
                    break
        return pointer
                    
    def recdes(self,string,lines,errors,par):
        
        self.trace = []
        self.string = string
        self.parallel = par
        p = self.Program(0)

        if p == 0:
            errors.append("Syntax error found at line number {0}".format(lines[len(self.trace)-1]))
        
        else:
            print("accepted")
            
        return errors
        


inpString = r'dt id ( dt id ) { }'
inpString2 = r'dt id / dt id ) { }'

def Parse(file):
    Lexer = lexer()
    Lexer.tokenize(file)

    parser = Parser()

    err = parser.recdes(Lexer.Tok,Lexer.lines,Lexer.errors,Lexer.par)
    out = open(file+".tr","w+")
    for i in parser.trace:
        out.write(i+"\n")
    out = open(file+".err","w+")
    for i in err:
        out.write(i+"\n")
    
Parse("tpl-tests/test01.tpl")
# Parse("tpl-tests/test02.tpl")
# Parse("tpl-tests/test03.tpl")
# Parse("tpl-tests/test04.tpl")

