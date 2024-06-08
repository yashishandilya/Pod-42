class Solution:
  # subtract rules: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
  def intToRoman(self, num: int) -> str:
    # I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
    # Take a number: 3999: 3 units of M (MMM), 
    # MMM(3000)CM(900)XC(90)IX(9)
    # 3598: 3000 - MMM
    #        500 - D
    #         90 - XC
    #          8 - VIII
    # divide by highest 'possible' number
    divison = 0
    digits=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),....]
    
    for i in range(len(digits)):
      values,symbol=digits[]
