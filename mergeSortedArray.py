class Sol:
    def merge_sorted_array(self,list1,lit2):
        list1=list1+list2
        l=(len(list1))
        while(l>0):
            m=list1.index(max(list1[:l]))
            list1[m],list1[l-1]=list1[l-1],list1[m]
            l-=1
        return list1

if __name__ == '__main__':
    list1=[1,2,3]
    list2=[2,5,6]
    p1=Sol()
    print(p1.merge_sorted_array(list1,list2))
