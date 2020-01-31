<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>assmt_3</title>
</head>
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
	
	.grid-container {
  	display: grid;
	grid-template-columns: auto auto auto;
  	background-color: #2196F3;
  	padding: 10px;
	}
	
	.grid-item {
  	background-color: rgba(255, 255, 255, 0.8);
  	border: 1px solid rgba(0, 0, 0, 0.8);
  	padding: 20px;
  	font-size: 30px;
  	text-align: center;
	}
	div{
		//border: 1px solid #73AD21;
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
	}
	hr{
	height:1px; 
	border:none; 
	color:#000; 
	background-color:#000; 
	width:40%; 
	text-align:center; 
	margin: 5 auto;}
	table{
    border: 1px solid black;
    }
	
</style>

<?php
//begin pulling in html tags
$entered_name=$_GET["entered_name"];
$car_selected=$_GET["car_selected"];
//$cars=array("ducati","ferrari","ford","gt","lambo","aventador","mclaren","mustang","pagani")

//end pulling in html tags
?>
	
<?php
//begin add record
   
    $myfile = fopen("database.txt", "a") or die("Unable to open file!");

    $txt = "$entered_name%$car_selected\r\n";//each field bounded by %
    fwrite($myfile, $txt);
	fclose($myfile);
	//print "<h4 class=message> $txt written to the database. </h4>";
	//$fields= explode('%',"$txt");
	//print "<tr><td>$fields[0]</td><td>$fields[1]</td><td>$fields[2]</td><td>$fields[3]</td><td>$fields[4]</td></tr>";

//end add record
?>

<body>
	<form action="execute.php" method="GET">
	<h1></h1>
	<hr>
	
	<div class="flex-container">
		<div class="flex_col1"></div>
  		<div class="flex_col2">Enter a name:&nbsp </div>
  		<div class="flex_col3"><input type="text" name="entered_name" value="default" style="width: 100%"></div>
		<div class="flex_col4"></div>
	</div><hr>
	<h1></h1><hr>
		
		<div class="grid-container">
			<div class="grid-item">
				<input type="submit" name="car_selected" value="ducati"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/DucatiDiavel.jpg); border: solid 0px #000000; width: 375px; height: 227px; color: transparent" />
			</div>
					
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="ferrari"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/FerrariTestarossa.jpg); border: solid 0px #000000; width: 375px; height: 160px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="ford"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/Ford.jpg); border: solid 0px #000000; width: 375px; height: 231px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="gt"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/FordGT.jpg); border: solid 0px #000000; width: 375px; height: 154px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="lambo"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/Lamborghini.jpg); border: solid 0px #000000; width: 375px; height: 165px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="aventador"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/LamborghiniAventador.jpg); border: solid 0px #000000; width: 375px; height: 206px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="mclaren"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/McLaren720S.jpg); border: solid 0px #000000; width: 375px; height: 175px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="mustang"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/Mustang.jpg); border: solid 0px #000000; width: 375px; height: 178px; color: transparent" />
			</div>
			
  			<div class="grid-item">
				<input type="submit" name="car_selected" value="pagani"
    			style="background-image: url(http://ck.csit.selu.edu/~ck/cars/Pagani_Zonda1999.jpg); border: solid 0px #000000; width: 375px; height: 154px; color: transparent" />
			</div>
			
		</div>	
	<table>
	<th>Name</th><th>Ducati</th><th>Ferrari</th><th>Ford</th><th>GT</th><th>Lambo</th><th>Aventador</th><th>McLaren</th><th>Mustang</th><th>Pagani</th>
		
<?php
// begin display statistics

	$myfile = fopen("database.txt","r");
	$lines = explode("\n", file_get_contents('database.txt'));
	fclose($myfile);
	print "<h4 class=message> Your results are below. </h4>";
	foreach ($lines as $value) {
		$fields= explode('%',$value);
		if (!isset($stats[$fields[1]][$fields[0]])){
			$stats[$fields[1]][$fields[0]]=1;
			print $fields[0]." has clicked "."$fields[1] ".$stats[$fields[1]][$fields[0]]. " times. <br>";
		} else{
			$stats[$fields[1]][$fields[0]]++;
			print $fields[0]." has clicked "."$fields[1] ".$stats[$fields[1]][$fields[0]]. " times. <br>";
		}
		
		//print "<tr><td>$fields[1]</td><td>$fields[0]</td></tr>";
		
	}
print $stats['ducati']['default'];
//end display statistics
?>
		
</table>
</body>
</html>