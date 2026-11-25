# Self-made simplified model. Run with CadQuery: python WeAct_RP2350B_simplified.py
# Simplified, self-made envelope model of the WeAct RP2350B Core Board on the carrier sockets.
# Dimensions from the board's public pinout/dimension info and the carrier footprint; no vendor CAD geometry used.
import cadquery as cq
A=cq.Assembly(name='WeAct_RP2350B_simplified')
def box(x0,x1,y0,y1,z0,z1): return cq.Workplane().box(x1-x0,y1-y0,z1-z0).translate(((x0+x1)/2,(y0+y1)/2,(z0+z1)/2))
xs=[-18.92+2.54*i for i in range(15)]
rows=[19.05,16.51,-16.51,-19.05]
# carrier female sockets 2x15 (z 0..5.7) and module male-header spacers (z 5.7..8.2)
sock=None; spc=None
for ys in ((15.26,20.30),(-20.30,-15.26)):
    s=box(-20.17,17.89,ys[0],ys[1],0,5.7); sp=box(-20.17,17.89,ys[0],ys[1],5.7,8.2)
    for y in rows:
        if ys[0]<y<ys[1]:
            for x in xs: s=s.cut(box(x-0.5,x+0.5,y-0.5,y+0.5,4.0,5.71))
    sock=s if sock is None else sock.union(s); spc=sp if spc is None else spc.union(sp)
A.add(sock,name='Carrier_Sockets',color=cq.Color(0.16,0.16,0.17))
A.add(spc,name='Header_Spacers',color=cq.Color(0.32,0.32,0.34))
pins=None
for y in rows:
    for x in xs:
        p=box(x-0.26,x+0.26,y-0.26,y+0.26,-2.35,5.05).union(box(x-0.3,x+0.3,y-0.3,y+0.3,5.05,10.6))
        pins=p if pins is None else pins.union(p)
A.add(pins,name='Pins',color=cq.Color(0.93,0.76,0.27))
pcb=cq.Workplane().box(41.38,41.12,1.6).edges('|Z').fillet(1.0).translate((0,0,9.0))
for y in rows:
    for x in xs: pcb=pcb.cut(cq.Workplane().circle(0.5).extrude(2).translate((x,y,8.1)))
A.add(pcb,name='Module_PCB',color=cq.Color(0.10,0.24,0.58))
usb=cq.Workplane('YZ').rect(8.94,3.2).extrude(7.3).edges('|X').fillet(1.4).translate((-20.55,0.06,11.4))
usb=usb.cut(cq.Workplane('YZ').rect(8.2,2.5).extrude(6.0).edges('|X').fillet(1.1).translate((-20.6,0.06,11.4)))
A.add(usb,name='USB_C',color=cq.Color(0.83,0.84,0.87))
A.add(box(-5.0,5.0,-5.0,5.0,9.8,10.67).rotate((0,0,0),(0,0,1),45).translate((2.29,0.06,0)),name='MCU_QFN80',color=cq.Color(0.14,0.14,0.15))
A.add(box(-2.65,2.65,-2.65,2.65,9.8,11.55).rotate((0,0,0),(0,0,1),45).translate((-9.4,-8.51,0)),name='Flash',color=cq.Color(0.20,0.20,0.22))
A.add(box(-1.25,1.25,-1.0,1.0,9.8,10.46).rotate((0,0,0),(0,0,1),45).translate((8.0,8.57,0)),name='Crystal',color=cq.Color(0.86,0.86,0.88))
for (x0,x1,y0,y1) in ((14.8,20.0,4.72,7.97),(14.68,19.88,8.79,12.04),(14.8,20.0,0.41,3.66)):
    body=box(x0,x1,y0,y1,9.8,11.3); cap=box(x0+1.2,x1-1.2,y0+0.6,y1-0.6,11.3,12.3)
    A.add(body,name=f'Button_{y0}',color=cq.Color(0.80,0.81,0.84)); A.add(cap,name=f'Cap_{y0}',color=cq.Color(0.96,0.94,0.88))
A.save('WeAct_RP2350B_simplified.step')
print('ok')
