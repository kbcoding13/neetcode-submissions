class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = "0"
        products = []
        def helper_sum(num1: str, num2: str) -> str:
            return str(int(num1) + int(num2))
            
        def helper_product(num1:str, digit:str, zeroes:str) -> str:
            return str(int(num1) * int(digit)) + zeroes

        if len(num2) > len(num1):
            num1, num2 = num2, num1

        zeroes = ""
        for i in range(len(num2) - 1, -1, -1):
            product = helper_product(num1, num2[i], zeroes)
            products.append(product)
            zeroes += "0"
        
        for i in range(len(products)):
            res = helper_sum(res, products[i])
        
        return res

        