#HOMEWORK

#1
"""
1․ Գրել MyList class,
որը կունենա գրեթե բոլոր այն մեթոդները և ֆունկցիոնալությունը,
որը ունի list class-ը առանց ժառանգելու։
"""

class MyList:
    def __init__(self,lst):
        self._is_list(lst)
        self.lst=lst
    @staticmethod
    def _is_list(lst):
        if not isinstance(lst,list):
            raise TypeError("lst must be list")
        if lst is None:
            lst=[]

    def __getitem__(self, item):
        return self.lst[item]
    def __setitem__(self, key, value):
        self.lst[key]=value
    def __delitem__(self, key):
        del self.lst[key]
    def len(self):
        return len(self.lst)
    def append(self,value):
        return self.lst.append(value)
    def clear(self):
        self.lst=[]
        return self.lst
    def copy(self,lst2):
        lst2=self.lst
        return lst2
    def count(self,item):
        count_of_item=0
        for i in self.lst:
            if i == item:
                count_of_item+=1
        return count_of_item
    def extend(self,lst2):
        self.lst+=lst2
        return self.lst
    def index(self,value):
        if value not in self.lst:
            raise ValueError(f"{value} is not in a list")
        for i in range(len(self.lst)):
            if self.lst[i]==value:
                return value
    def insert(self,index,value):
        l=len(self.lst)
        if index>=l:
            self.lst.append(value)
        else:
            self.lst.append(None)
            for i in range(l-1,index-1,-1):
                self.lst[i+1]=self.lst[i]
            self.lst[index]=value

        return self.lst
    def pop(self,index=-1):
        return self.lst.pop(index)
    def remove(self,value):
        for i in range(len(self.lst)):
            if self.lst[i] ==value:
                del self.lst[i]
                break
    def reverse(self):
        lst2=[]
        for i in range(len(self.lst)-1,-1,-1):
            lst2.append(self.lst[i])
        return lst2
    def sort(self):
            # if len(self.lst)<=1:
            #     return self.lst
            # pivot=self.lst[0]
            # less=[i for i in self.lst[1:] if i<pivot]
            # more=[i for i in self.lst[1:] if i>pivot]
            # equal=[i for i in self.lst[1:] if i==pivot]
            # return sort(less) + equal + sort(more)
        for i in range(0,len(self.lst)):
            for j in range(0,len(self.lst)-i-1):
                if self.lst[j]>self.lst[j+1]:
                    self.lst[j],self.lst[j+1]=self.lst[j+1],self.lst[j]
        return self.lst

    def __repr__(self):
            return str(self.lst)



s=MyList([1,2,3,4,5,5])
print(s.count(5))
print(s.count(6))
print(s[0])
s[0]=6
print(s)
del s[0]
print(s)
s.append(10)
print(s)
print(s.clear())
s.append(5)
s.append(6)
s.append(7)
print(s)
s2=MyList([1,2,3])
s3=MyList([4,5,6])
s4=MyList([1,2,3,4,2,5])
print(s2.extend(s3))
print(s3.insert(2,5))
print(s3.insert(4,7))
print(f"s3 = {s3}")
print(s3.pop(-2))
s4.remove(2)
print(s4)
s4.insert(1,2)
print(s4.reverse())
print(s4.sort())
