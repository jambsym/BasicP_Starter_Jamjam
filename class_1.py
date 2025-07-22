x=int(input("ระยะทาง :"))
m1=10
m2=15
m3=25
m4=35
m5=45
v=0.07
if 5<=x<=50 :
     print("ราคา 10")
     print("Vat7%",v*m1)
     print("ราคารวมVat",m1 + (m1*v))
elif 51<=x<=100:
     print("ราคา : 15")
     print("Vat7%",v*m2)
     print("ราคารวมVat :",m2 + (m2*v))
elif 101<=x<=300:
     print("ราคา 25 :")
     print("Vat7%",v*m3)
     print("ราคารวมVat :",m3 + (m3*v))
elif 301<=x<=500:
     print("ราคา 35 :")
     print("Vat7%",v*m4)
     print("ราคารวมVat :",m4 + (m4*v))
elif x>500:
     print("ราคา 45 :")
     print("Vat7%",v*m5)
     print("ราคารวมVat :",m5 + (m5*v))
else :
     print("ส่งฟรี")