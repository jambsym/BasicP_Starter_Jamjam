member=input("สมาชิกของคุณ :")
money=float(input("จำนวนรวมที่สั่งอาหาร :"))
date=int(input("วันที่สั่งซื้อ :"))
total = money

if member=="Gold":
   if money>=1000 :
      total -= money* 0.15
      