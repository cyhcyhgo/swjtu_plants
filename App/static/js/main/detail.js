let x;
let y;
let map, geolocation;

//加载地图，调用浏览器定位服务
function mini_map() {
    map = new AMap.Map('container', {
        resizeEnable: true
    });
    map.plugin('AMap.Geolocation', function () {
        geolocation = new AMap.Geolocation({
            enableHighAccuracy: true, //是否使用高精度定位，默认:true
            timeout: 10000, //超过10秒后停止定位，默认：无穷大
            buttonOffset: new AMap.Pixel(10, 20), //定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
            zoomToAccuracy: true, //定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
            buttonPosition: 'RB'
        });
        map.addControl(geolocation);
        geolocation.getCurrentPosition();
        AMap.event.addListener(geolocation, 'complete', onComplete); //返回定位信息
        AMap.event.addListener(geolocation, 'error', onError); //返回定位出错信息
    });
}


function initial(x1, y1) {
    x = x1;
    y = y1;
}


//解析定位结果
function onComplete(data) {
    console.log(data.position);
    const lat = data.position.getLat();
    const lng = data.position.getLng();

    const walkOption = {
        map: map,
        panel: "panel",
        hideMarkers: false,
        isOutline: true,
        outlineColor: '#ffeeee',
        autoFitView: true
    };
    // 步行导航
    const walking = new AMap.Walking(walkOption);

    //根据起终点坐标规划步行路线
    walking.search([lng, lat], [x, y], function (status, result) {
        // result即是对应的步行路线数据信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_RidingResult
        if (status === 'complete') {
            log.success('步行路线数据查询成功')
        } else {
            log.error('步行路线数据查询失败' + result)
        }
    });
}

//解析定位错误信息
function onError(data) {
    console.log('err');
}

