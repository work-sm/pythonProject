from skyfield.api import EarthSatellite
from skyfield.api import Topos
from skyfield.api import load

# stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
# satellites = load.tle_file(stations_url, reload=True)
# print('Loaded', len(satellites), 'satellites')
#
# by_number = {sat.model.satnum: sat for sat in satellites}
# satellite = by_number[25544]
# print(satellite)

ts = load.timescale()
line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)
print(satellite)
print(satellite.epoch.utc_jpl())

t = ts.utc(2014, 1, 21, 22, 23, 4)
days = t - satellite.epoch
print('{:.3f} days away from epoch'.format(days))

# 地心坐标系 位置
geocentric = satellite.at(t)
print(geocentric.position.km)

# 星下点
subpoint = geocentric.subpoint()
print('Latitude:', subpoint.latitude)
print('Longitude:', subpoint.longitude)
print('Elevation (m):', int(subpoint.elevation.m))

# 卫星的高度超过地平线以上指定的度数
# 纬度：北纬为正数，南纬为负数。北纬（N）南纬（S）
# 经度：东经为正数，西经为负数。东经（E）西经（W）
bluffton = Topos('34.23053 N', '108.93425 E')
t1 = ts.utc(2014, 1, 23)
t2 = ts.utc(2014, 1, 24)
t, events = satellite.find_events(bluffton, t1, t2, altitude_degrees=30.0)
for ti, event in zip(t, events):
    name = ('rise above 30°', 'culminate', 'set below 30°')[event]
    print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)

# 卫星相对于观察者位置
t = ts.utc(2014, 1, 21, 22, 23, 4)
difference = satellite - bluffton
topocentric = difference.at(t)
alt, az, distance = topocentric.altaz()
if alt.degrees > 0:
    print('The ISS is above the horizon')

print(alt)
print(az)
print(int(distance.km), 'km')
