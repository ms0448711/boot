<?php
date_default_timezone_set('Singapore');
// Coded by : AriestaSakitHati
/*

How to use

1. search google how to run php in cmd
2. open cmd
3. type php (this file path) (your maillist file path) (word of mail you want to filter)
   ex : php c:\code\filter.php c:\list\mail.txt yahoo
4. enter _|
5. the result location : c:\users\...\002-FILTER.txt

*/

function isEmail($email) {
	if( !preg_match("/^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,3})$/i", $email) )
		return false;
	return true;
}

function inStr($s, $as){
    $s = strtoupper($s);
    if(!is_array($as)) $as=array($as);
    for($i=0;$i<count($as);$i++) if(strpos(($s),strtoupper($as[$i]))!==false) return true;
    return false;
}

function check($email, $find){
	if(inStr(explode('@', $email)[1], $find)){
		
		$log = fopen("002-FILTER.txt","a");
		fwrite($log, "".$email."\n");
		fclose($log);			
		
		return array (
			"msg"=>"YES"
		);
		
	}else{
		return array (
			"msg"=>"NO"
		);
	}
}

$listpath = $argv[1];
$empass_list = file_get_contents($listpath);
$empass_list_array = file($listpath);
$empass = explode(PHP_EOL, $empass_list);
$empass_list_lenght = count($empass_list_array);

$find = $argv[2];

for($i=0; $i<$empass_list_lenght; $i++){
	$timeServer = date("G:i:s");
	$anu = $i+1;
	echo "[".$timeServer."] - "."[".$anu."|".$empass_list_lenght."] ".$empass[$i]." ->";
	if(isEmail($empass[$i])){
		echo check($empass[$i], $find)["msg"]."\n";
	}else{
		echo " This is not valid email \n";
	}
}

?>