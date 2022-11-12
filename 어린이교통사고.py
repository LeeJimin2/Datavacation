#!/usr/bin/env python
# coding: utf-8

# In[1]:


from geoband.API import *


# In[2]:


GetCompasData('SBJ_2012_001', '2', '2.오산시_어린이교통사고_격자.geojson')


# In[3]:


from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[4]:


import folium
import json
import geopandas as gpd


# In[5]:


GetCompasData('SBJ_2012_001', '1', '1.오산시_주정차단속(2018~2020).csv')
GetCompasData('SBJ_2012_001', '3', '3.오산시_차량등록현황_격자.geojson')
GetCompasData('SBJ_2012_001', '4', '4.오산시_연령별_거주인구격자(총인구).geojson')
GetCompasData('SBJ_2012_001', '5', '5.오산시_연령별_거주인구격자(유소년).geojson')
GetCompasData('SBJ_2012_001', '6', '6.오산시_연령별_거주인구격자(생산가능인구).geojson')
GetCompasData('SBJ_2012_001', '7', '7.오산시_연령별_거주인구격자(고령).geojson')


# In[6]:


GetCompasData('SBJ_2012_001', '8', '8.오산시_유동인구(2019).csv')
GetCompasData('SBJ_2012_001', '9', '9.오산시_어린이보호구역.csv')
GetCompasData('SBJ_2012_001', '10', '10.오산시_학교위치정보.csv')
GetCompasData('SBJ_2012_001', '11', '11.오산시_초등학교_통학구.geojson')
GetCompasData('SBJ_2012_001', '12', '12.오산시_중학교_학군.geojson')
GetCompasData('SBJ_2012_001', '13', '13.오산시_어린이집_유치원현황.csv')
GetCompasData('SBJ_2012_001', '14', '14.오산시_기상데이터(2010~2019).csv')
GetCompasData('SBJ_2012_001', '15', '15.오산시_무인교통단속카메라.csv')
GetCompasData('SBJ_2012_001', '16', '16.오산시_도로안전표지표준데이터.csv')
GetCompasData('SBJ_2012_001', '17', '17.오산시_횡단보도.geojson')
GetCompasData('SBJ_2012_001', '18', '18.오산시_과속방지턱표준데이터.csv')
GetCompasData('SBJ_2012_001', '19', '19.오산시_신호등.geojson')
GetCompasData('SBJ_2012_001', '20', '20.오산시_CCTV설치현황.csv')
GetCompasData('SBJ_2012_001', '21', '21.오산시_인도.geojson')


# In[7]:


GetCompasData('SBJ_2012_001', '22', '22.오산시_버스정류장.csv')
GetCompasData('SBJ_2012_001', '23', '23.오산시_상세도로망_LV6.geojson')
GetCompasData('SBJ_2012_001', '24', '24.평일_전일,시간대별_오산시_추정교통량_Level6.csv')
GetCompasData('SBJ_2012_001', '25', '25.평일_전일_오산시_혼잡빈도강도_Level6.csv')
GetCompasData('SBJ_2012_001', '26', '26.평일_전일_오산시_혼잡시간강도_Level6.csv')
GetCompasData('SBJ_2012_001', '27', '27.오산시_도로명주소_건물.geojson')
GetCompasData('SBJ_2012_001', '28', '28.오산시_건물연면적_격자.geojson')
GetCompasData('SBJ_2012_001', '29', '29.오산시_체육시설현황.csv')
GetCompasData('SBJ_2012_001', '30', '30.오산시_학원_및_교습소_현황.csv')
GetCompasData('SBJ_2012_001', '31', '31.오산시_법정경계(시군구).geojson')
GetCompasData('SBJ_2012_001', '32', '32.오산시_행정경계(읍면동).geojson')
GetCompasData('SBJ_2012_001', '33', '33.오산시_법정경계(읍면동).geojson')
GetCompasData('SBJ_2012_001', '34', '34.오산시_지적도.geojson')


# In[8]:


import pathlib


# In[9]:


import pandas as pd


# In[10]:


input_path = pathlib.Path('./input')
if not input_path.is_dir():
    input_path.mkdir()


# In[11]:


for path in list(input_path.glob('*.csv')) + list(input_path.glob('*.geojson')):
    print(path)


# In[12]:


df_01=pd.read_csv("1.오산시_주정차단속(2018~2020).csv")
df_02=gpd.read_file("2.오산시_어린이교통사고_격자.geojson")


# In[13]:


df_03=gpd.read_file('3.오산시_차량등록현황_격자.geojson')
df_04=gpd.read_file('4.오산시_연령별_거주인구격자(총인구).geojson')
df_05=gpd.read_file('5.오산시_연령별_거주인구격자(유소년).geojson')
df_06=gpd.read_file('6.오산시_연령별_거주인구격자(생산가능인구).geojson')
df_07=gpd.read_file('7.오산시_연령별_거주인구격자(고령).geojson')
df_08=pd.read_csv('8.오산시_유동인구(2019).csv')
df_09=pd.read_csv('9.오산시_어린이보호구역.csv')
df_10=pd.read_csv('10.오산시_학교위치정보.csv')


# In[14]:


df_11=gpd.read_file('11.오산시_초등학교_통학구.geojson')
df_12=gpd.read_file('12.오산시_중학교_학군.geojson')
df_13=pd.read_csv('13.오산시_어린이집_유치원현황.csv')
df_14=pd.read_csv('14.오산시_기상데이터(2010~2019).csv')
df_15=pd.read_csv('15.오산시_무인교통단속카메라.csv')
df_16=pd.read_csv('16.오산시_도로안전표지표준데이터.csv')
df_17=gpd.read_file('17.오산시_횡단보도.geojson')
df_18=pd.read_csv('18.오산시_과속방지턱표준데이터.csv')
df_19=gpd.read_file('19.오산시_신호등.geojson')
df_20=pd.read_csv('20.오산시_CCTV설치현황.csv')
df_21=gpd.read_file('21.오산시_인도.geojson')


# In[15]:


df_22=pd.read_csv('22.오산시_버스정류장.csv')
df_23=gpd.read_file('23.오산시_상세도로망_LV6.geojson')
df_24=pd.read_csv('24.평일_전일,시간대별_오산시_추정교통량_Level6.csv')
df_25=pd.read_csv('25.평일_전일_오산시_혼잡빈도강도_Level6.csv')
df_26=pd.read_csv('26.평일_전일_오산시_혼잡시간강도_Level6.csv')
df_27=gpd.read_file('27.오산시_도로명주소_건물.geojson')
df_28=gpd.read_file('28.오산시_건물연면적_격자.geojson')
df_29=pd.read_csv('29.오산시_체육시설현황.csv')
df_30=pd.read_csv('30.오산시_학원_및_교습소_현황.csv')
df_31=gpd.read_file('31.오산시_법정경계(시군구).geojson')
df_32=gpd.read_file('32.오산시_행정경계(읍면동).geojson')
df_33=gpd.read_file('33.오산시_법정경계(읍면동).geojson')
df_34=gpd.read_file('34.오산시_지적도.geojson')


# In[17]:


json = DeleteDuplicates(inputFeatures = 'geoband:tl_scco_sig',saveFileName="json/result_accident.json")
gdf = gpd.read_file("2.오산시_어린이교통사고_격자.geojson")


# In[16]:


df_04 = df_04.rename(columns = {"val":"val_total"})
df_05 = df_05.rename(columns = {"val":"val_junior"})
df_06 = df_06.rename(columns = {"val":"val_work"})
df_07 = df_07.rename(columns = {"val":"val_senior"})
df_28 = df_28.rename(columns = {"val":"val_building"})


# In[17]:


df_pop =pd.merge(pd.merge(pd.merge(pd.merge(
    df_04[['gid','geometry','val_total']], df_05[['gid', 'val_junior']]),
                                   df_06[['gid','val_work']]),
                          df_07[['gid','val_senior']]),
                df_02[['gid','accident_cnt']])


# In[43]:


df_pop['val_total'] = df_pop['val_total'].fillna(0)
df_pop['val_senior'] = df_pop['val_senior'].fillna(0)
df_pop['val_work'] = df_pop['val_work'].fillna(0)
df_pop['val_junior'] = df_pop['val_junior'].fillna(0)
df_pop[df_pop['val_total']!=0]


# In[18]:


df_pop['coordinates'] = df_pop['geometry'].apply(multipolygon_to_coordinates)

lat_min=[]
lat_max=[]
lon_min=[]
lon_max=[]
for i in range(len(df_pop)):    
    lon_min.append(df_pop['coordinates'][i][1][0])
    lon_max.append(df_pop['coordinates'][i][3][0])
    lat_min.append(df_pop['coordinates'][i][0][1])
    lat_max.append(df_pop['coordinates'][i][2][1])

df_pop['lon_min'] = lon_min
df_pop['lon_max'] = lon_max
df_pop['lat_min'] = lat_min
df_pop['lat_max'] = lat_max


# In[18]:


import shapely
def line_string_to_coordinates(line_string): 
    if isinstance(line_string, shapely.geometry.linestring.LineString): 
        lon, lat = line_string.xy 
        return [[x, y] for x, y in zip(lon, lat)] 
    elif isinstance(line_string, shapely.geometry.multilinestring.MultiLineString): 
        ret = [] 
        for i in range(len(line_string)): 
            lon, lat = line_string[i].xy 
            for x, y in zip(lon, lat): 
                ret.append([x, y])
        return ret 

def multipolygon_to_coordinates(x): 
    lon, lat = x[0].exterior.xy 
    return [[x, y] for x, y in zip(lon, lat)] 

def polygon_to_coordinates(x): 
    lon, lat = x.exterior.xy 
    return [[x, y] for x, y in zip(lon, lat)] 


def to_coordinates(x): 
    try: 
        lon, lat = x[0].exterior.xy 
    except:
        lon, lat = x.exterior.xy 
    return [[x, y] for x, y in zip(lon, lat)] 


# In[19]:


from shapely.geometry import Polygon, Point

df_pop_list = []
df_pop_list2 = []
for i in df_pop['geometry']:
    cent = [[i[0].centroid.coords[0][0],i[0].centroid.coords[0][1]]]
    df_pop_list.append(cent)
    df_pop_list2.append(Point(cent[0]))
df_pop['coord_cent'] = 0
df_pop['geo_cent'] = 0
df_pop['coord_cent']= pd.DataFrame(df_pop_list) # pydeck을 위한 coordinate type
df_pop['geo_cent'] = df_pop_list2 # geopandas를 위한 geometry type


# In[35]:


is_accident = df_pop['accident_cnt']>0
accident = df_pop[is_accident]
print(accident.shape)
print()
accident


# In[21]:


df_pop =pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(
    df_04[['gid','geometry','val_total']], df_05[['gid', 'val_junior']]),
                                   df_06[['gid','val_work']]),
                          df_07[['gid','val_senior']]),
                df_02[['gid','accident_cnt']]),
                          df_03[['gid','car_cnt']]),
                 df_28[['gid','val_building']])


# In[26]:


df_pop['val_total'] = df_pop['val_total'].fillna(0)
df_pop['val_senior'] = df_pop['val_senior'].fillna(0)
df_pop['val_work'] = df_pop['val_work'].fillna(0)
df_pop['val_junior'] = df_pop['val_junior'].fillna(0)
df_pop['val_building']=df_pop['val_building'].fillna(0)
df_pop[df_pop['val_total']!=0]


# 

# 

# In[24]:


df1 = df_23
df1['coordinate'] = df1['geometry'].buffer(0.001).apply(polygon_to_coordinates) 
df1 = pd.DataFrame(df1)
df1['정규화도로폭'] = df1['width'].apply(int) / df1['width'].apply(int).max()


# In[30]:


df_24_time8 = df_24[df_24['시간적범위']==8]


# In[59]:


df_23_ =[]
for i in df_23.link_id:
    df_23_.append([i,(df_24_time8[df_24_time8['상세도로망_LinkID'].apply(str).str.contains(i)])])
df_23_ = pd.DataFrame(df_23_).fillna(0)
df_23_.columns = ["link_id", "교통량"]
df_23_24_time8=pd.merge(df1, df_23_, on = 'link_id')

df_23_24_time8.iloc[df_23_24_time8["교통량"].sort_values(ascending=False).index].reindex().head()


# In[48]:


df_23_ = []
for i in df_23.link_id:
    df_23_.append([i,sum(df_25[df_25['상세도로망_LinkID'].apply(str).str.contains(i)].혼잡빈도강도)])
    
df_23_ = pd.DataFrame(df_23_).fillna(0)
df_23_.columns = ["link_id", "혼잡빈도강도합"]
df_23_25=pd.merge(df1, df_23_,on = 'link_id' )


# In[49]:


df_23_25.iloc[df_23_25["혼잡빈도강도합"].sort_values(ascending=False).index].reindex().head()


# In[51]:


df_23_ = []
for i in df_23.link_id:
    df_23_.append([i,sum(df_26[df_26['상세도로망_LinkID'].apply(str).str.contains(i)].혼잡시간강도)])
    
df_23_ = pd.DataFrame(df_23_).fillna(0)
df_23_.columns = ["link_id", "혼잡시간강도합"]
df_23_26=pd.merge(df1, df_23_,on = 'link_id' )


# In[52]:


df_23_26.iloc[df_23_26["혼잡시간강도합"].sort_values(ascending=False).index].reindex().head()


# In[27]:


df_24['시간적범위'].value_counts()


# In[30]:


import numbers
import math


# In[35]:


df_20['CCTV 유형코드'].value_counts()


# In[17]:


Ccctv = df_20['CCTV 유형코드']=='C'
CCTV = df_20[Ccctv]
print(CCTV.shape)
print()


# In[19]:


CCTV


# In[45]:


df_01['행정구역'].value_counts()


# In[13]:


df_01_1=df_01[df_01['행정구역'].str.contains('경기도 오산시')]
df_01_1


# In[16]:


df_01_1['행정구역'].value_counts()


# In[42]:


df_09_1=df_09[df_09['시설명'].str.contains('예인유치원')]
df_09_1


# In[24]:


cctv = df_09['CCTV설치대수']>0
CCTV = df_09[cctv]
print(CCTV.shape)
print()
CCTV


# In[27]:


CCTV['보호구역도로폭'].value_counts()


# In[28]:


CCTV['CCTV설치대수'].value_counts()


# In[30]:


cctv_max= df_09['CCTV설치대수']==1
CCTV_max = CCTV[cctv_max]
print(CCTV_max.shape)
print()
CCTV_max


# In[35]:


df_14


# In[38]:


df_14['일강수량(mm)'].value_counts()


# In[44]:


df_18


# In[49]:


df_18_1= df_18['과속방지턱높이']==10
df_18_01 = df_18[df_18_1]
print(df_18_01.shape)
print()
df_18_01


# In[51]:


df_18_2= df_18_01['보차분리여부']=="N"
df_18_02 = df_18_01[df_18_2]
print(df_18_02.shape)
print()
df_18_02


# In[52]:


df_18_3= df_18_01['연속형여부']=="N"
df_18_03 = df_18_01[df_18_3]
-print(df_18_03.shape)
print()
df_18_03


# In[57]:


df_21


# In[58]:


df_21['QUAL'].value_counts()


# In[59]:


df_21['BYYN'].value_counts()


# In[60]:


df_21['KIND'].value_counts()


# In[67]:


df_26['시군구명'].value_counts()


# In[ ]:


df_01


# In[24]:


import pandas as pd
import folium
from folium.plugins import MarkerCluster, MiniMap
import geopandas as gpd
import geojson
import json


# In[23]:


latitude = 37.164045
longitude = 127.051602


# In[27]:


m = folium.Map(location=[latitude, longitude], zoom_start=12)#, tiles='color_map')
gdf = gpd.read_file('32.오산시_행정경계(읍면동).geojson')
gdf = gdf.to_crs(epsg='4326')
converted_json = gdf.to_json()

for i in range(len(my_json2)):
    m.choropleth(
        geo_data = my_json2[i],
        name='인구수',
        key_on='properties.emd_cd',
        fill_color='YlGn',
        fill_opacity=0,
        line_opacity=1,
        color = 'blue',
        overlays=True
    )
    for key in m._children:
        if key.startswith('color_map'):
            del(m._children[key])
mc = MarkerCluster()

for row in df_32.itertuples():
    mc.add_child(folium.Marker(location = [row.latitude, row.longitude], popup=row.station_name + str(row.nums)))
    m.add_child(mc)

m


# In[24]:


m = folium.Map(location=[37.16,127.051],zoom_start=12)
for i in range(len(df_31)):
    geo= folium.GeoJson(df_31.geometry[i])
    popup = folium.Popup(str(i))
    popup.add_to(geo)
    geo.add_to(m)


# In[25]:


m


# In[42]:


df_18


# In[44]:


a = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_18)):
    lat = df_18.loc[i,'lat']
    lng = df_18.loc[i,'lng']
    folium.Marker([lat,lng]).add_to(z)
z


# In[25]:


df_18 = df_18.rename(columns = {"설치위치_경도":"lng"})
df_18 = df_18.rename(columns = {"설치위치_위도":"lat"})


# In[74]:


df_09


# In[26]:


df_09 = df_09.rename(columns = {"보호구역_경도":"lng"})
df_09 = df_09.rename(columns = {"보호구역_위도":"lat"})


# In[28]:


b = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_09)):
    lat = df_09.loc[i,'lat']
    lng = df_09.loc[i,'lng']
    folium.Circle([lat,lng],radius=100, color='red').add_to(m)
m


# In[20]:


df_pop['coordinates'] = df_pop['geometry'].apply(multipolygon_to_coordinates)

lat_min=[]
lat_max=[]
lon_min=[]
lon_max=[]
lat = []
lng = []

for i in df_pop.index:    
    lon_min.append(df_pop['coordinates'][i][1][0])
    lon_max.append(df_pop['coordinates'][i][3][0])
    lat_min.append(df_pop['coordinates'][i][0][1])
    lat_max.append(df_pop['coordinates'][i][2][1])
    lat.append(df_pop['coord_cent'][i][1])
    lng.append(df_pop['coord_cent'][i][0])

df_pop['lon_min'] = lon_min
df_pop['lon_max'] = lon_max
df_pop['lat_min'] = lat_min
df_pop['lat_max'] = lat_max
df_pop['lat'] = lat
df_pop['lng'] = lng


# In[28]:


df_pop


# In[28]:


f = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in accident.index:
    lat = accident.loc[i,'lat']
    lng = accident.loc[i,'lng']
    folium.Circle([lat,lng],radius=50, color='blue').add_to(m)
m


# In[132]:


df_15


# In[27]:


df_15 = df_15.rename(columns = {"설치위치_경도":"lng"})
df_15 = df_15.rename(columns = {"설치위치_위도":"lat"})


# In[46]:


c = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_15)):
    lat = df_15.loc[i,'lat']
    lng = df_15.loc[i,'lng']
    folium.Marker([lat,lng]).add_to(z)
z


# In[135]:


df_16


# In[47]:


d = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_16)):
    lat = df_16.loc[i,'lat']
    lon = df_16.loc[i,'lon']
    folium.Marker([lat,lon]).add_to(z)
z


# In[48]:


df_20


# In[28]:


df_20 = df_20.rename(columns = {"설치위치_경도":"lng"})
df_20 = df_20.rename(columns = {"설치위치_위도":"lat"})


# In[49]:


e = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_20)):
    lat = df_20.loc[i,'lat']
    lng = df_20.loc[i,'lng']
    folium.Marker([lat,lng]).add_to(z)
z


# In[20]:


df_29


# In[29]:


df_29 = df_29.rename(columns = {"설치위치_경도":"lng"})
df_29 = df_29.rename(columns = {"설치위치_위도":"lat"})


# In[26]:


g = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_29)):
    lat = df_29.loc[i,'lat']
    lng = df_29.loc[i,'lng']
    folium.Circle([lat,lng],radius=100, color='orange').add_to(g)
g


# In[31]:


df_30


# In[30]:


df_30 = df_30.rename(columns = {"시설위치_경도":"lng"})
df_30 = df_30.rename(columns = {"시설위치_위도":"lat"})


# In[32]:


h = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_30)):
    lat = df_30.loc[i,'lat']
    lng = df_30.loc[i,'lng']
    folium.Circle([lat,lng],radius=100, color='green').add_to(h)
h


# In[33]:


df_02


# In[34]:


df_02['accident_cnt'].value_counts()


# In[31]:


z = folium.Map(location=[37.16,127.05],zoom_start=12)

for i in accident.index:
    lat = accident.loc[i,'lat']
    lng = accident.loc[i,'lng']
    
    color = 'red'
    if accident.loc[i,'accident_cnt'] == 2:
        color = "orange"
    if accident.loc[i,'accident_cnt'] == 3:
        color = "yellow"
    if accident.loc[i,'accident_cnt'] == 4:
        color = "green"
    if accident.loc[i,'accident_cnt'] == 5:
        color = "blue"
    if accident.loc[i,'accident_cnt'] == 6:
        color = "purple"
    if accident.loc[i,'accident_cnt'] == 7:
        color = "black"
    if accident.loc[i,'accident_cnt'] == 10:
        color = "white"
    
    folium.CircleMarker([lat,lng],color=color,radius = 5, popup = [lat, lng]).add_to(z)
z


# In[33]:


import folium
from folium.plugins import MarkerCluster


# In[39]:


df_09


# In[34]:


map = folium.Map(location=[37.16,127.05],zoom_start=12)
marker_cluster = MarkerCluster().add_to(map)

for i in accident.index:
    lat = accident.loc[i,'lat']
    lng = accident.loc[i,'lng']
    folium.Marker(
        location = [lat,lng],
        icon = folium.Icon(color = 'red', icon = 'ok'),
    ).add_to(marker_cluster)
map


# In[59]:


j = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in accident.index:
    lat = accident.loc[i,'lat']
    lng = accident.loc[i,'lng']
    folium.Circle([lat,lng],radius=50, color='blue').add_to(m)
m


# In[31]:


k = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_09)):
    lat = df_09.loc[i,'lat']
    lng = df_09.loc[i,'lng']
    folium.Circle([lat,lng],radius=300, color='red').add_to(m)
m


# In[32]:


k = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_09)):
    lat = df_09.loc[i,'lat']
    lng = df_09.loc[i,'lng']
    name = df_09.loc[i, '시설명']
    folium.Circle([lat,lng],radius=300, color='grey', popup = [name, lat]).add_to(z)
z


# In[36]:


accident


# In[39]:


accident.sort_values("accident_cnt", ascending = False)


# In[40]:


df_09


# In[ ]:





# In[52]:


k = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_09)):
    lat = df_09.loc[i,'lat']
    lng = df_09.loc[i,'lng']
    folium.Circle([lat,lng],radius=300, color='grey', popup = [lat, lng]).add_to(z)
z


# In[63]:


map = folium.Map(location=[37.16,127.05],zoom_start=12)
marker_cluster = MarkerCluster().add_to(map)

for i in accident.index:
    lat = accident.loc[i,'lat']
    lng = accident.loc[i,'lng']
    folium.Marker(
        location = [lat,lng],
        icon = folium.Icon(color = 'red', icon = 'ok'),
    ).add_to(map)
map


# In[41]:


j = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in accident.index:
    lat = accident.loc[i,'lat']
    lng = accident.loc[i,'lng']
    folium.Circle([lat,lng],radius=50, color='blue').add_to(k)
k


# In[43]:


n = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_15)):
    lat = df_15.loc[i,'lat']
    lng = df_15.loc[i,'lng']
    folium.Marker([lat,lng]).add_to(k)
k


# In[45]:


o = folium.Map(location=[37.16,127.05],zoom_start=12)
for i in range(len(df_18)):
    lat = df_18.loc[i,'lat']
    lng = df_18.loc[i,'lng']
    folium.Marker([lat,lng]).add_to(k)
k


# 
