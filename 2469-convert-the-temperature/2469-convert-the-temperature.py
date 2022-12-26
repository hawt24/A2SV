class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        kelvin=celsius+273.15
        fah=celsius*1.8+32
        ans.append(kelvin)
        ans.append(fah)
        return ans
        