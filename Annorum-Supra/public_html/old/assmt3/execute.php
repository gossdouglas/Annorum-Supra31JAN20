<!DOCTYPE html>
<html>
<style>
	.flex-container {
  	display: flex;
  	background-color: DodgerBlue;
	
	margin: auto;
  	width: 40%;
  	//border: 1px solid #73AD21;
	padding-top: 3px;
	padding-bottom: 3px;
	justify-content: center;
}
	div{
		border: 0px solid #73AD21;
	}
	.flex_col1{
		width:25%
	}
	.flex_col2{
		width:25%;
		text-align: right
	}
	.flex_col3{
		width:25%
	}
	.flex_col4{
		width:25%
	}
	h1{
		text-align: center;
		padding-top: 0px;
		padding-bottom: 0px;
		margin: 0px;
        background-color: white;
	}
	h4.message{
		text-align: center;
		padding-top: 0px;
		padding-bottom: 0px;
		margin: 0px;
        background-color: white;
	}
	hr{
	height:1px; 
	border:none; 
	color:#000; 
	background-color:#000; 
	width:40%; 
	text-align:center; 
	margin: 5 auto;
    }
    table{
		text-align: center;
		margin:0 auto;
    	border: 1px solid black;
		width:40%;
    }
	td{
		text-align: left;
		margin:0 auto;
    	border: 1px solid black;
		
    }
	th{
		border: 1px solid black;
	}
	
</style>

<?php
//begin pulling in html tags
$operation=$_GET["operation"];
$title=$_GET["title"];
$author=$_GET["author"];
$isbn=$_GET["isbn"];
$publisher=$_GET["publisher"];
$year=$_GET["year"];

//end pulling in html tags
?>

<body>
	<form action="execute.php" method="GET">
	<h1>Book Inventory</h1>
	<hr>	
	<div class="flex-container">
		<div class="flex_col1"></div>
  		<div class="flex_col2">Select Operation:&nbsp </div>
  		<div class="flex_col3"><select name="operation" style="width: 100%">
		  			<option value='<?php echo $operation?>' selected='selected'><?php echo $operation?></option>
					<option value="add">Add</option>
					<option value="delete">Delete</option>
					<option value="search">Search</option>
				</select>
		</div>
		<div class="flex_col4"></div>
	</div><hr>
	<h1>Book Fields</h1><hr>		
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Title:&nbsp;</div><div class="flex_col3"><input type="text" name="title" value="<?php print $title; ?>" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">			<div class="flex_col1"></div>
			<div class="flex_col2">Author:&nbsp;</div><div class="flex_col3"><input type="text" name="author" value="<?php print $author; ?>" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">ISBN:&nbsp;</div><div class="flex_col3"><input type="text" name="isbn" value="<?php print $isbn; ?>" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Publisher:&nbsp;</div><div class="flex_col3"><input type="text" name="publisher" value="<?php print $publisher; ?>" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Year:&nbsp;</div><div class="flex_col3"><input type="text" name="year" value="<?php print $year; ?>" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">	
			<input type="submit" value="Execute"> 			
        </div>
	</form><hr>
	
	<div class="flex-container">
			<div class="flex_col1"><a href="http://localhost/cmps294/Assmt%203/assmt_3.html">Main Page.</a></div>
			<div class="flex_col2"></div>	
			<div class="flex_col3"></div>	
			<div class="flex_col4"><a href="db_contents.php">View all DB records.</a></div>		
	</div>
	<table>
	<th>Title</th><th>Author</th><th>ISBN</th><th>Publisher</th><th>Year</th>

<?php
//begin add record
if ($_GET["operation"] =="add" ) {
    
    $myfile = fopen("database.txt", "a") or die("Unable to open file!");

    $txt = "$title%$author%$isbn%$publisher%$year\r\n";//each field bounded by %
    fwrite($myfile, $txt);
	fclose($myfile);
	print "<h4 class=message> $txt written to the database. </h4>";
	$fields= explode('%',"$txt");
	print "<tr><td>$fields[0]</td><td>$fields[1]</td><td>$fields[2]</td><td>$fields[3]</td><td>$fields[4]</td></tr>";
}
//end add record
?>

<?php
// begin search records
if ($_GET["operation"] =="search" ) {
 
	$myfile = fopen("database.txt","r");
	$lines = explode("\n", file_get_contents('database.txt'));
	fclose($myfile);
	print "<h4 class=message> Your search results are below. </h4>";
	foreach ($lines as $value) {
		$fields= explode('%',$value);
		if($fields[0]==$title||$fields[1]==$author||$fields[2]==$isbn||$fields[3]==$publisher||$fields[4]==$year){
		print "<tr><td>$fields[0]</td><td>$fields[1]</td><td>$fields[2]</td><td>$fields[3]</td><td>$fields[4]</td></tr>";
		}
	}
	//print "</table>";	
}
//end search records
?>

<?php
// begin delete records
if ($_GET["operation"] =="delete" ) {

	if($title!=NULL){
		$title_to_delete=$title;
	}else{$title_to_delete=".*";
	}

	if($author!=NULL){
		$author_to_delete=$author;
	}else{$author_to_delete=".*";
	}

	if($isbn!=NULL){
		$isbn_to_delete=$isbn;
	}else{$isbn_to_delete=".*";
	}

	if($publisher!=NULL){
		$publisher_to_delete=$publisher;
	}else{$publisher_to_delete=".*";
	}

	if($year!=NULL){
		$year_to_delete=$year;
	}else{$year_to_delete=".*";
	}
 
	$myfile = fopen("database.txt","r");
	$lines = explode("\n", file_get_contents('database.txt'));
	fclose($myfile);

	foreach ($lines as $value){
		if (preg_match("/$title_to_delete%$author_to_delete%$isbn_to_delete%$publisher_to_delete%$year_to_delete/", $value)){
			$delete[]=$value;
			//print_r($delete);
		}else{
			$keep[]=$value;
		}
	}
	
print "<h4 class=message>The records that have been deleted are shown below. </h4>";
	foreach ($delete as $value) {
		//print "$value <br>";		
		$fields= explode('%',"$value");
		print "<tr><td>$fields[0]</td><td>$fields[1]</td><td>$fields[2]</td><td>$fields[3]</td><td>$fields[4]</td></tr>";
		}
	
print "</table>";

print "<h4 class=message>The records that have been retained are shown below. </h4>";
print "<table>";

	$myfile = fopen("database.txt", "w") or die("Unable to open file!");

	foreach ($keep as $value) {
	//print "$value <br>";
	$txt = "$value\r\n";
	fwrite($myfile, $txt);
	$fields= explode('%',"$value");
	print "<tr><td>$fields[0]</td><td>$fields[1]</td><td>$fields[2]</td><td>$fields[3]</td><td>$fields[4]</td></tr>";
	}
	fclose($myfile);
print "</table>";

	}//end delete records	

?>
</table>
</body>
</html>