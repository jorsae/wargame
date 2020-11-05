<?php
    $request = '';
    foreach($argv as $value){
            $request = $value;
    }

    echo "REQUEST: " . $request . "\r\n";
    if(strstr($request, "iloveyou")){
            echo "strstr: true \r\n";
    }
    else{
            echo "strstr: false \r\n";
    }

    if($request > 10){
            echo "$request > 10: true \r\n";
    }
    else{
            echo "$request > 10: false \r\n";
    }

    if(strstr($request,"iloveyou") && ($request > 10 )){
        echo "<br>The credentials for the next level are:<br>";
        echo "<pre>Username: natas24 Password: <censored></pre>";
    }
    else{
        echo "<br>Wrong!<br>";
    }
?> 