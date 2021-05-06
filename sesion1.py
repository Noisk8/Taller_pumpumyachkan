p1 >> play ("|H3||H4|", )

p1 >> play ("H ", sample=var([4,3]) )


ko >> play ("(pum)<pum>[asim]<tria>", dur=.5)



Clock.bpm=130


ju >> keys (amp=3,room=.1, mix=.1, dur=.5, delay=0, )

print(SynthDefs)


print(Player.get_attributes())

p1 >> play ("|X2| ", amp=1,dur=.5, )


nh >> play (" |o1|", amp=1, dur=2/2,room=.4, mix=.5 )



p2 >> dirt (amp=1, dur=[1/2,6/8,7/8],)


pumpum=linvar([0,1,2,3,6,8])
gt >> sawbass (pumpum, amp=1.4, oct=5, hpf=linvar([1100,200,0]),)


ji >> bass (dur=PDur(3,8), lpf=linvar([100,500,1222]), chop=1)

vr >> play (" |~3|", dur=1/2, chop=0, amp=1.2 )



 

kl >> play ("|x2| ", amp=1.5)

jk >> play (" |o2|", dur=2/2, bpm=90)


j2 >> bass (pumpum, dur=PDur(3,8), tremolo=0, bpm=80)


hu >> soprano(vib=0, dur=8)

uo >> prophet (dur=8,amp=2, pan=[0,2])



