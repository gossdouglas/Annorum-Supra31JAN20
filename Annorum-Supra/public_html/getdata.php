<?php

//mysqli_connect("localhost","my_user","my_password","my_db");//example from w3 schools
//$connect = mysqli_connect("localhost", "root", "", "goss_cmps394_ajax");//for my pc mysql server
$connect = mysqli_connect("localhost", "goss", "w0148941", "goss_cmps394_ajax");//for slu mysql server
$output = '';
if(isset($_POST["query"]))
{
 $search = mysqli_real_escape_string($connect, $_POST["query"]);
 $query = "
  SELECT * FROM table1
  WHERE name LIKE '".$search."%'
 ";
}
else
{
 $query = "
  SELECT * FROM table1 ORDER BY name
 ";
}

$result = mysqli_query($connect, $query);
if(mysqli_num_rows($result) > 0)
{
 $output .= '
 <div class="row">
 <table class="table"> 
     <thead> 
         <tr> 
             <th>#</th> 
             <th>First Name</th> 
             <th>Gender</th> 
             <th>Role</th> 
             <th>ID</th> 
         </tr>                         
     </thead> 
 ';
 while($row = mysqli_fetch_array($result))
 {
  $output .= '
   <tr>
   <th scope="row"></th> 
    <td>'.$row["name"].'</td>
    <td>'.$row["gender"].'</td>
    <td>'.$row["role"].'</td>
    <td>'.$row["id"].'</td>
   </tr>
  ';
 }
 echo $output;
}
else
{
 echo 'No such first name exists.';
}

?>
