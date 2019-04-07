<?php
define('DB_HOST', 'tbsdbinstance.ctlrgvtx2zlb.ap-south-1.rds.amazonaws.com');
define('DB_PORT', 3306);
define('DB_LOGIN', 'grofers');
define('DB_PASS', 'password');
define('DB_NAME', 'grofers');
define('DB_TNAME', 'grofers');
define('DB_KEYNAME', 'custom_key');//since "key" is SQL reserved keyword
define('DB_VALNAME', 'value');

$conn=null;

function dbconn()
{
	global $conn;
	$servername = DB_HOST;
	$port = DB_PORT;
	$username = DB_LOGIN;
	$password = DB_PASS;
	$db = DB_NAME;
	// Create connection
	$conn = new mysqli($servername, $username, $password, $db, $port);

	// Check connection
	if ($conn->connect_error) {
	die('{error:"1",result:""}');
	}
};

function dbdisconn()//for disconnecting database
{
	global $conn;
	$conn->close();
};

function set_key($key,$value)
{
	dbconn();
	global $conn;
    $count_sql="SELECT count(".DB_KEYNAME.") FROM '".DB_TNAME."'' WHERE '".DB_KEYNAME."'='".$key."'";
	$insert_sql="insert into '".DB_TNAME."' ('".DB_KEYNAME."','".DB_VALNAME."')values ('".$key."','".$value."')";
	$update_sql="UPDATE '".DB_TNAME."' SET '".DB_VALNAME."'='".$value."' WHERE '".DB_KEYNAME."'='".$key."'";
    $row = $conn->query($count_sql);
	if (($row->fetch_assoc())['count('.DB_KEYNAME.')']==1){
        $conn->query($update_sql);
    }
	else{
        $conn->query($insert_sql);
    }
	dbdisconn();
	echo ('{error:"1",result:"'.$value.'"}');
};

function get_key($key)
{
    $sql="SELECT '".DB_VALNAME."' FROM '".DB_TNAME."'' WHERE '".DB_KEYNAME."'='".$key."'";
	dbconn();
	global $conn;
	$row = $conn->query($sql);
    dbdisconn();
    return ($row->fetch_assoc())[DB_KEYNAME];
};