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

<body>
	<form action="execute.php" method="GET">
	<h1>Book Inventory</h1>
	<hr>	
	<div class="flex-container">
		<div class="flex_col1"></div>
  		<div class="flex_col2">Select Operation:&nbsp </div>
  		<div class="flex_col3"><select name="operation" style="width: 100%">
					<option value="add">Add</option>
					<option value="delete">Delete</option>
					<option value="search">Search</option>
				</select>
		</div>
		<div class="flex_col4"></div>
	</div><hr>
	<h1>Book Fields, % for wildcard</h1><hr>		
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Title:&nbsp;</div><div class="flex_col3"><input type="text" name="title" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Author:&nbsp;</div><div class="flex_col3"><input type="text" name="author" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">ISBN:&nbsp;</div><div class="flex_col3"><input type="text" name="isbn" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Publisher:&nbsp;</div><div class="flex_col3"><input type="text" name="publisher" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">
			<div class="flex_col1"></div>
			<div class="flex_col2">Year:&nbsp;</div><div class="flex_col3"><input type="text" name="year" style="width: 100%"></div>	
			<div class="flex_col4"></div>			
		</div>
	
		<div class="flex-container">	
			<input type="submit" value="Execute"> 			
        </div>
	<hr>
	
	<div class="flex-container">
		<div class="flex_col1"><a href="assmt4.html">&nbsp;Main Page.</a></div>	
        <div class="flex_col2"></div>
        <div class="flex_col3"></div>
        <div class="flex_col2">>View all DB records.</div>		
	</div>
	</form>
    <h1>View all records in the DB from this  page.</h1><hr>
<table>
	<th>Title</th><th>Author</th><th>ISBN</th><th>Publisher</th><th>Year</th>
<?php
// begin show all records
	extract( $_POST );
		//$connection = "";
		//$database = "goss_assmt_4";
		//$table = "Inventory";
		$select = '*';
	
		$connection = "";
		$servername = "localhost";
		$username = "goss";
		$password = "w0148941";
		$database = "goss_assmt_4";
		$table = "Inventory";

	// build SELECT query (specifies table as well)
	//select and show all records from the table
         $query = "SELECT " . $select . " FROM $table";
	
	// Connect to MySQL
         if ( !( $connection = mysql_connect( $servername, $username, $password )))
            die( "Could not connect to database" );
   
         //print("Now open a database <br>");
		 // open the particular database
         if ( !mysql_select_db( $database, $connection ) )
            die( "Could not open the database" );
   
         //print("Now query the database<br>");
		 // query the database
         if ( !( $result = mysql_query( $query, $connection ) ) ) {
            print( "Could not execute query! <br />" );
            die( mysql_error() );
         }
    
	// fetch each record in result set
            for ( $counter = 0; 
               $row = mysql_fetch_row( $result );
               $counter++ ){

               // build table to display results
               print( "<tr>" );

               foreach ( $row as $key => $value ) 
                  print( "<td>$value</td>" );

               print( "</tr>" );
            }

            mysql_close( $database );
        //$ttl_records++;	
    //}
    print "</table>";	
    print "<h4 class=message>";
    //print $ttl_records;
	print $counter;
    print " records are currently in the database.";
    print "</h4>";

?>
</table>
</body>
</html>