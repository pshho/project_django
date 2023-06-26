var htmlMarker1 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/poll/images/cluster-marker-1.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker2 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/poll/images/cluster-marker-2.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker3 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/poll/images/cluster-marker-3.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker4 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/poll/images/cluster-marker-4.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker5 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/poll/images/cluster-marker-5.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
};

// 마커 표시하고 숨기는 함수
function updateMarkers(map, markers) {

    var mapBounds = map.getBounds();
    var marker, position;

    for (var i = 0; i < markers.length; i++) {

        marker = markers[i]
        position = marker.getPosition();

        if (mapBounds.hasLatLng(position)) {
            showMarker(map, marker);
        } else {
            hideMarker(map, marker);
        }
    }
}

// 화면에서 보이는 영역 마커 표시 함수
function showMarker(map, marker) {
    if (marker.getMap()) return;
    marker.setMap(map);
}

// 화면에서 안보일 때 마커 숨기는 함수
function hideMarker(map, marker) {
    if (!marker.getMap()) return;
    marker.setMap(null);
}

var all_markers = [],
    markerGroup1 = [],
    markerGroup2 = [],
    markerGroup3 = [],
    markerGroup4 = [];

// 마커 클러스터링 업데이트 함수
function updateMarkerClustering(markers) {

    // 새로운 MarkerClustering 인스턴스 생성
    markerClustering = new MarkerClustering({
    minClusterSize: 2,
    maxZoom: 18,
    map: map,
    markers: markers,
    disableClickZoom: true,
    gridSize: 150,
    icons: [htmlMarker1, htmlMarker2, htmlMarker3, htmlMarker4, htmlMarker5],
    indexGenerator: [10, 100, 200, 500, 1000],
    stylingFunction: function(clusterMarker, count) {
      $(clusterMarker.getElement()).find('div:first-child').text(count);
    },
    minClusterZIndex: 100,
    maxClusterZIndex: 200
    });
}

$(window).on('load', function() {
    $.ajax({
        type: 'get',
        url: "../map_convert/",
        dataType: 'json',
        success: function(data) {

            // 마커 및 마커 이벤트 생성 함수
            function createMarker(lat, lng, iconUrl, text) {
                var marker = new naver.maps.Marker({
                    position: new naver.maps.LatLng(lng, lat),
                    map: map,
                    icon: {
                    url: iconUrl,
                    size: new naver.maps.Size(50, 50),
                    origin: new naver.maps.Point(0, 0),
                    anchor: new naver.maps.Point(25, 50)
                    }
                });

                naver.maps.Event.addListener(marker, 'click', function() {
                    // 정보창 생성
                    var infoWindow = new naver.maps.InfoWindow({
                        content: text, // 정보창에 표시할 내용
                        anchorSize: {width:5, height:5},
                        borderWidth: 1,
                        pixelMargin: "10px",
                    });

                    // 마커에 정보창 표시
                    infoWindow.open(map, marker);
                });

                return marker;
            };

            for (var i=0; i<data.length; i++) {

                var lat;
                var lng;
                var iconUrl;
                var marker;
                var text;

                switch (data[i].bdusa) {
                    case '연립다세대':
                        iconUrl = "/static/poll/images/icon2.png";
                        lat = data[i].lat;
                        lng = data[i].lng;
                        text = data[i].bdnm;
                        marker = createMarker(lat, lng, iconUrl, text);
                        markerGroup1.push(marker);
                        all_markers.push(marker);
                        break;
                    case '아파트':
                        iconUrl = "/static/poll/images/icon4.png";
                        lat = data[i].lat;
                        lng = data[i].lng;
                        text = data[i].bdnm;
                        marker = createMarker(lat, lng, iconUrl, text);
                        markerGroup2.push(marker);
                        all_markers.push(marker);
                        break;
                    case '오피스텔':
                        iconUrl = "/static/poll/images/icon3.png";
                        lat = data[i].lat;
                        lng = data[i].lng;
                        text = data[i].bdnm;
                        marker = createMarker(lat, lng, iconUrl, text);
                        markerGroup3.push(marker);
                        all_markers.push(marker);
                        break;
                    case '단독다가구':
                        iconUrl = "/static/poll/images/icon1.png";
                        lat = data[i].lat;
                        lng = data[i].lng;
                        marker = createMarker(lat, lng, iconUrl, text);
                        markerGroup4.push(marker);
                        all_markers.push(marker);
                        break;
                    default:
                        break;
                }
            };

            // 마커 클러스터링 업데이트
            updateMarkerClustering(all_markers);

            // updateMarkers 스크롤 시 함수 실행
            naver.maps.Event.addListener(map, 'zoom_changed', function() {
                updateMarkers(map, all_markers);

            });

            naver.maps.Event.addListener(map, 'dragend', function() {
                updateMarkers(map, all_markers);
            });

        },
        error: function() {
            console.log('에러')
        }
    });

    $('form').on('submit', function(e) {
        e.preventDefault();
        var value = $('#map_address').val();

        $.ajax({
            type: "get",
            url: "../search2/",
            dataType: "json",
            data: {q:value},
            success: function(data) {
                if(data.items.length > 0) {
                    searchAddressToCoordinate(data.items[0].address, data.items[0].title);
                }else {
                    searchAddressToCoordinate(value, value);
                }

                $('#map_address').val('');
            },
            error: function() {
                console.log('확인 불가');
            }
        })

    })

    // 주소로 지도 검색
    function searchAddressToCoordinate(address, title) {
        naver.maps.Service.geocode({
            query: address
        }, function (status, response) {
            if (status === naver.maps.Service.Status.ERROR) {
                return alert('접속 실패!');
            }

            if (response.v2.meta.totalCount === 0) {
                return alert('찾지 못했습니다.');
            }

            var htmlAddresses = [],
                item = response.v2.addresses[0],
                point = new naver.maps.Point(item.x, item.y);

            map.setCenter(point);
        });
    }

    // 지도 실행시 처음 위치
    function initGeocoder() {
        searchAddressToCoordinate('서울 강남구 테헤란로5길 24 장연빌딩', '강남 그린컴퓨터아카데미');
    }

    // 지도 실행시 지정한 처음 위치 불러옴
    initGeocoder();
})

// 지도 마우스 커서 포인트
map.setCursor('pointer');

// 지도의 현재 위치 찾는 코드
naver.maps.Event.once(map, 'init', function () {
    var customControl = new naver.maps.CustomControl(locationBtnHtml, {
        position: naver.maps.Position.RIGHT_CENTER
    });

    // 커서 스타일 설정
    customControl.getElement().style.cursor = 'pointer';

    customControl.setMap(map);

    naver.maps.Event.addDOMListener(customControl.getElement(), 'click', function () {

        function onSuccessGeolocation(position) {
            var location = new naver.maps.LatLng(position.coords.latitude,
                position.coords.longitude);

            map.setCenter(location); // 얻은 좌표를 지도의 중심으로 설정합니다.
            map.setZoom(14); // 지도의 줌 레벨을 변경합니다.

        }

        function onErrorGeolocation() {
            var center = map.getCenter();

        }

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(onSuccessGeolocation, onErrorGeolocation);
        } else {
            var center = map.getCenter();
        }

    });
});

$(document).ready(function() {
    // 미리 만든 4개의 배열
    var markerGroups = {
        group1: markerGroup1,
        group2: markerGroup2,
        group3: markerGroup3,
        group4: markerGroup4
    };

    $('.map_grouping input[type="radio"]').click(function() {
        var selectedMarkerGroupId = this.value;

        // 선택된 마커 그룹 배열 가져오기
        var selectedMarkerGroup = markerGroups[selectedMarkerGroupId];

        // 현재 상태 확인
        var isMarkersVisible = selectedMarkerGroup.some(function(marker) {
            return marker.getVisible();
        });

        // 선택된 마커 그룹의 마커 보이기/숨기기 토글
        selectedMarkerGroup.forEach(function(marker) {
            marker.setVisible(!isMarkersVisible);
        });

    });

})



