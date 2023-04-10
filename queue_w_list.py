class Queue:
    def __init__(self):
        self._elements = list()
        self.length =0
    
    def q_pop(this):
        if(this.length):
            this.length-=1
            return this._elements.pop()
        
    def q_push(this, element):
        this._elements.insert(0,element)
        this.length+=1

    def q_peek(this):
        return this._elements[-1]
    
    def __str__(this):
        return str(this._elements)
