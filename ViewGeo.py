import folium
from pandas import DataFrame
from pandas import ExcelFile


def markGeo() :
    rows = [x.split(" Conn")[0].split(",") for x in open("./file", "r").read().split("\n")]
    locations = []
    # 새로운 지도 객체 생성
    map_osm1 = folium.Map(location=[x.split(":")[1].strip() for x in rows[0]], zoom_start='17')
    for row in rows:
        r = [x.split(":")[1].strip() for x in row]

        # HTML을 사용한 팝업
        # popup_html = folium.Popup("<font color='green' style='white-space: nowrap'><b>임시항적기록</b></font>", parse_html=False)
        
        # 마커 객체 생성
        marker1 = folium.Marker(r, 
                                popup='출발지:ETRI',    # 팝업명
                                icon=folium.Icon(color='red')) #color='red', icon='아이콘'
        
        marker1.add_to(map_osm1)  # 마커 객체를 지도에 추가함
        
    map_osm1                  # 지도 표시하기

    map_osm1.save('geo_result.html')


if __name__ == "__main__":
    markGeo()