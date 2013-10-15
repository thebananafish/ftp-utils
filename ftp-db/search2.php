<?php

try {
	//uses pdo to connect to db, 
	$database_connect = 'mysql:host=localhost;dbname=databasename';
	$PDO = new PDO($database_connect, 'databaseusername', 'password');
	}
catch(PDOException $e)
{
		echo "Mysql Connection Error, please refresh the page";
}
 
$term = $_POST['term'];
 
 
$sql = "select * from files where File_Name like '%$term%'";

//prepared statement to prevent from sql_injection
$preparedStatement = $PDO->prepare($sql);

//execute statement
$preparedStatement->execute();

$result = $preparedStatement->fetchAll(PDO::FETCH_ASSOC);

if(!$result){
    die("Failed to find any search results");
}

foreach($result as $row)
{
	echo 'File Location: '.$row['FILE_ROOT'];
    echo '<br/> File Name: '.$row['FILE_NAME'];
    echo '<br/> File Size in bytes: '.$row['FILE_SIZE'];
    echo '<br/> Upload Date '.$row['FILE_DATE'];
    echo '<br/><br/>';
}
 
echo '***END of SEARCH REPORT***';
?>
