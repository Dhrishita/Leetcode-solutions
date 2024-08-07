class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        
        below_20=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine", "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens=["", "","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty", "Ninety"]
        
        def pasta(num: int)->str:
            if num<20:
                d=below_20[num]
            elif num<100:
                d=tens[num//10]+" "+below_20[num%10]
            elif num<1000:
                d=pasta(num//100)+" Hundred "+pasta(num%100)
            elif num<1000000:
                d=pasta(num//1000)+" Thousand "+pasta(num%1000)
            elif num<1000000000:
                d=pasta(num//1000000)+" Million "+pasta(num%1000000)
            else:
                d=pasta(num//1000000000)+" Billion "+pasta(num%1000000000)
                
            return d.strip()
        return pasta(num)


        