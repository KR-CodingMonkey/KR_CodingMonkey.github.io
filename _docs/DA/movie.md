---
title: 영화 관객수 예측 모델 개발
tags: 
 - Data analysis
 - Dacon
 - movie
 - RandomForestRegressor
description: 영화 관객수 예측 모델 개발 
permalink: docs/DA/movie
---

# (문화)영화 관객수 예측 모델 개발

영화 관객수를 예측해 보세요.

- title : 영화의 제목
- distributor : 배급사
- genre : 장르
- release_time : 개봉일
- time : 상영시간(분)
- screening_rat : 상영등급
- director : 감독이름
- dir_prev_bfnum : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화에서의 평균 관객수(단 관객수가 알려지지 않은 영화 제외)
- dir_prev_num : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화의 개수(단 관객수가 알려지지 않은 영화 제외)
- num_staff : 스텝수
- num_actor : 주연배우수
- box_off_num : 관객수

**데이터 셋**: [영화 관객수 데이터](https://dacon.io/competitions/open/235536/data)

<script type="text/javascript">
function calcHeight() {
//find the height of the internal page
var the_height= document.getElementById('handmotion').contentWindow. document.body.scrollHeight;
//change the height of the iframe
document.getElementById('handmotion').height= the_height; top.location.href = "#";
}

</script>
<iframe id="movie" src="{{ site.baseurl }}/docs/DA/notebooks/hand" frameborder="0" width="100%" marginwidth="0" marginheight="0" scrolling="no" style="border: 0px" onload="calcHeight(),window.scrollTo(0,0)" height="1">movie</iframe>