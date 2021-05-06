p1 >> play ("|H3||H4|", )

p1 >> play ("H ", sample=var([4,3]) )



Clock.bpm=130


ju >> keys (amp=1)

print(SynthDefs)


print(Player.get_attributes())

p1 >> play ("|x3| ", amp=1,dur=0, )





p2 >> dirt (amp=1, dur=[1/2,6/8,7/8],)


pumpum=var([0,2,4,6,8])
gt >> sawbass (pumpum, amp=1.4, oct=4)


 


