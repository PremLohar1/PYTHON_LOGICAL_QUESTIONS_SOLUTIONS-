<?php

function neon($num){
  $ans = $num*$num;
  $res=0;
  while($ans>0){
    $res = $res + ($ans%10);
    $ans = intval($ans/10);
  }
  if($num==$res){
    echo "This is Neon Number = ".$num;
  }
  else{
    echo "This is Normal Number = ".$num;
  }
}
neon(9);

?>