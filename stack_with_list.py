class Stack:
    def __init__(self):
        self._elements = list()
        self.length =0
    
    def st_pop(this):
        if(this.length):
            this.length-=1
            return this._elements.pop()
        
    def st_push(this, element):
        this._elements.append(element)
        this.length+=1

    def st_peek(this):
        return this._elements[-1]
    
    def __str__(this):
        return str(this._elements)
