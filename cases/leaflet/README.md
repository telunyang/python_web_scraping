# Leaflet.js - 對手機平台友善的互動式地圖開放源始碼函式庫 (JavaScript Library)
[官方網站](https://leafletjs.com/)

## 1. 基礎用法

### 1.1 建立一專案資料夾，並在資料夾中建立 html 網頁 (以 VS code 為例)
- 建立資料夾，例如 **gis**，並將 **gis** 資料夾拖入 vs code，或是以 vs code 開啟資料夾視窗。
- 建立 html 檔，例如 **index.html**。
- 開啟 index.html，輸入 **!**，提示文字出現選，選擇「!」，自動建立 html 樣版。
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

### 1.2 按下 Tutorials 連結，選擇 Leaflet Quick Start Guide
- 放置 Leaflet CSS (CDN) 檔案在 index.html 的 `</head>` 之前：
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.2/dist/leaflet.css" integrity="sha256-sA+zWATbFveLLNqWO2gtiw3HL/lh1giY/Inf1BJ0z14=" crossorigin="" />
```
- 放置 Leaflet JavaScript (CDN) 檔案在 `</body>` 之前：
```html
<script src="https://unpkg.com/leaflet@1.9.2/dist/leaflet.js" integrity="sha256-o9N1jGDZrf5tS+Ft4gbIK7mYMipq9lqpVJ91xHSyKhg=" crossorigin=""></script>
```
- 放置 `<div id="map"></div>` 到 `<body>` 之後：
```html
<div id="map"></div>
```
- 放置 `<style>#map { height: 640px; }</style>` 到 `</head>` 之前：
```css
<style>
#map { height: 640px; }
</style>
```

### 1.3 按下 Overview 超連結，透過 JavaScript 程式碼，產生地圖
- 在 Leaflet JavaScript (CDN) 的 `</script>` 之後，加入以下程式碼：
```javascript
<script>
var map = L.map('map').setView([25.0339145, 121.5412233], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([25.0339145, 121.5412233]).addTo(map)
    .bindPopup('自訂訊息<br>可以放 HTML')
    .openPopup();
</script>
```

### 2. 需要安裝 flask、requests
```bash
$ pip install -U Flask requests
```

## 3. 範例資料來源
- [Cafe Nomad：咖啡廳遊牧民族 ](https://cafenomad.tw/)
  - [開發人員 API 文件](https://cafenomad.tw/developers)
    - [API v1.2](https://cafenomad.tw/developers/docs/v1.2)：以 taipei 的資料為例 -  [預覽 JSON](https://cafenomad.tw/api/v1.2/cafes/taipei)


## 4. 範例程式
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- leaflet css 設定 -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    
    <!-- 自訂 css -->
    <style>
        table, thead, th, tbody, tr, td {
            border: 1px solid;
        }

        #map { height: 480px; }
    </style>
</head>
<body>
    <button id="btn_request">取得臺北市咖啡廳列表</button>

    <div id="map"></div>

    <table>
        <thead>
            <tr>
                <th>id</th>
                <th>city</th>
                <th>name</th>
                <th>address</th>
                <th>url</th>
                <th>socket</th>
                <th>latitude</th>
                <th>longitude</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>

    <!-- leaflet JS cdn -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    
    <!-- 自訂 js -->
    <script>
    //引入地圖
    let map = L.map('map').setView([25.0339145, 121.5412233], 13);

    //初始化地圖圖層(預設)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    //設定圖層群組
    let layerGroup = null;
    let arrLayers = [];
    
    // 按鈕事件，取得 Web API 的回傳資料
    document.querySelector('button#btn_request').addEventListener('click', function(event){
        /**
         * 非同步傳輸的工具 - fetch
         * 透過 ajax (xml http request) 技術，
         * 做到不切換頁面也能請求資料/取得回應的方法
         * 
         * 參考網頁:
         * 1. 鐵人賽：ES6 原生 Fetch 遠端資料方法
         * https://www.casper.tw/javascript/2017/12/28/javascript-fetch/
         */
        fetch('http://localhost:5000/taipei',{
            method: "GET"
        }).then(function(response){
            /**
             * response.text() - 純文字 or html
             * response.blob() - 通常用於 base64 編碼後的 img 內容
             * response.json() - 若回傳的格式為 json 文字，自動轉成物件 (Object)
             */
            return response.json();
        }).then(function(arr){
            //刪除先前的 markers
            if( layerGroup != null && map.hasLayer(layerGroup) ) {
                layerGroup.clearLayers();
                map.removeLayer(layerGroup);

                //變數初始化
                layerGroup = null;
                arrLayers = [];
            }

            // 取得 tbody 元素
            let tbody = document.querySelector('table > tbody');

            // 清空 tbody 底下既有元素，如 tr td 等
            tbody.innerHTML = '';

            // 將回傳資料動態生成在網頁上
            for(let o of arr){
                //輸出對應的 html tag
                let tr = document.createElement("tr");
                tr.innerHTML = `<td>${o['id']}</td>
                                <td>${o['city']}</td>
                                <td>${o['name']}</td>
                                <td>${o['address']}</td>
                                <td><a href="${o['url']}" target="_blank">連結</a></td>
                                <td>${o['socket']}</td>
                                <td>${o['latitude']}</td>
                                <td>${o['longitude']}</td>`;
                tbody.appendChild(tr);

                //建立 markers
                let marker = L.marker([o['latitude'], o['longitude']])
                .bindPopup(`${o['name']}<br><a href="${o['url']}" target="_blank">連結</a>`);

                //自訂事件
                marker.addEventListener('click', function(event){
                    console.log(o);
                });

                //將 markers 各別放到空陣列 arrLayers 當中
                arrLayers.push(marker);
            }

            //迴圈執行完畢後，將 arrLayers 放到 layerGroup 當中
            layerGroup = L.layerGroup(arrLayers);

            //將 layerGroup 放到 map 當中
            layerGroup.addTo(map);
        });
    });
    </script>
</body>
</html>
```

## 4. 相關影片
[Leaflet.js - Web 互動式地圖](https://www.youtube.com/playlist?list=PLV4FeK54eNbwNaCoJomI1jhvgm-A-vOsz)