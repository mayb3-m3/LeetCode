class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        for i in range(children, -1, -1):
            rem_money = money - i*8
            rem_child = children - i
            if rem_money == 0:
                if rem_child:  #no money but child
                    continue
                return i
            elif rem_money < 0:
                continue
            else:
                if rem_money == 4 and rem_child == 1:
                    continue
                if rem_money < rem_child or rem_child == 0: #less money than child / no child but money
                    continue
                return i  
        return -1
