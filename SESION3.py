p1 >> loop ('Radio communications between Yuri Gagarin, Sergei Korolev and Ground Control-Wyrj0ibxt8c', 1, dur=60)

p2 >> loop ('SAMPLE1', 8, dur=3)

p3 >> loop ('SAMPLE1', 6, dur=2)




pumpum = var([0,-4,-5,1,2,3,4,-3,-1])

resistencia = linvar([.3, 1.4, 1.6])

colombia = linvar ([20, 300, 40])



p4 >> loop ('SAMPLE1', 4, dur=.5, amp=resistencia.r)



hu >> fuzz (pumpum, hpf= colombia, amp=resistencia )

ff >> blip (pumpum, amp=resistencia, oct=6, hpf=colombia )



notas =P[0,3,5,7,8,9]

awante = P[1,1,1,4,4,4,]

ir >> dirt (notas.reverse(), chop=awante.rotate())

# https://foxdot.org/docs/pattern-functions/

hy >> dirt (dur=PDur(5,8),sus=PStep(1, 2), chop=PSum(1, 4), hpf=colombia,amp= resistencia)


df >> play ("te [ee] ee", sample=PRand(2), amp=2, dur=.5 )
yu >> play ("|x4| ")













