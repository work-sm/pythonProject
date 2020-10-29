import ephem

# http://rhodesmill.org/pyephem/quick.html
me = ephem.Observer()
me.lon, me.lat, me.elevation = '108.5000', '34.5000', 800.0
line1 = "BEIDOU G1"
line2 = "1 36287U 10001A   18194.84994825 -.00000297  00000-0  00000-0 0  9999"
line3 = "2 36287   1.4745   3.9768 0004214 156.8560 216.8921  1.00270561 31144"
sat = ephem.readtle(line1, line2, line3)

me.date = '2018/7/14'  # ephem.now()
sat.compute(me)

print(sat.az * 180.0 / 3.1416)  # 卫星的方位角
print(sat.alt * 180.0 / 3.1416)  # 卫星的仰角
print(sat.range_velocity)  # 卫星相对于观察者的运动速率，为正，表示卫星正在远离观察者

ephwy = ephem.readdb("C/1995 O1 (Hale-Bopp),e,89.0083,283.3220,130.5617,179.4002,0.0004102,0.99494219,0.0000,03/29.7186/1997,2000,g -2.0,4.0")
ephwy.compute('2018/7/14')
print(ephwy.name)
print("%s %s" % (ephwy.ra, ephwy.dec))
print("%s %s" % (ephem.constellation(ephwy), ephwy.mag))
