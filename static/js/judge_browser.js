var browserRedirect = function () {
  /* 判断是pc端还是移动端  网上有很多，我只用其中一种演示*/
  var sUserAgent = navigator.userAgent.toLowerCase();
  var bIsIpad = sUserAgent.match(/ipad/i) == "ipad";
  var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os";
  var bIsMidp = sUserAgent.match(/midp/i) == "midp";
  var bIsUc7 = sUserAgent.match(/rv:1.2.3.4/i) == "rv:1.2.3.4";
  var bIsUc = sUserAgent.match(/ucweb/i) == "ucweb";
  var bIsAndroid = sUserAgent.match(/android/i) == "android";
  var bIsCE = sUserAgent.match(/windows ce/i) == "windows ce";
  var bIsWM = sUserAgent.match(/windows mobile/i) == "windows mobile";
  /* 根据不同的客户端引入样以及加载页面 */
  if (bIsIpad || bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM) {
    document.write('<link href="/static/css/myblog_mobile.css" rel="stylesheet" type="text/css" /> ');
  } else {
    document.write('<link href="/static/css/myblog.css" rel="stylesheet" type="text/css" /> ')
  }
};
browserRedirect();




