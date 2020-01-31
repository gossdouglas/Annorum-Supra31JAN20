<?php 
   // Program to demo a cookie
   
   extract( $_POST );
   if ($myname != "") { setcookie( "myName", $myname, time() + (60*5) ); }  //set cookie; expires in 3 minutes

   if ($erase == "yes") { setcookie( "myName", "xxxxx", time() - 5 ); } //set cookie to a past time

   // Grab the name of this file so we can submit to it regardless of what it is called
   $script = $_SERVER['SCRIPT_NAMEjjj']; 

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns = "http://www.w3.org/1999/xhtml">
   <head>
      <title>Cookie Example</title>
   </head>

   <body style = "font-family: arial, sans-serif">
      <p align=center>Hello there 
<?php 
   if ($_COOKIE[myName] != "") { 
	print "$_COOKIE[myName], how are you?<p>"; 
	print <<<EOT1
      <form action = "$script"  method = "post"  style = "font-size: 10pt; text-align: center;">
Would you like to erase the cookie?<br>
Yes <input type = "radio" name = "erase" value="yes"><br>
No <input type = "radio" name = "erase" value="no" checked><br>
         <input type = "submit" value = "Continue" 
            style = "background-color: #F0E86C; color: navy;
            font-weight: bold" /><p>
      </form>

EOT1;

} 
	else { print <<<EOT2
I don't believe we have met before. What is your name? <p align=center>
      <form action = "$script"  method = "post"  style = "font-size: 10pt; text-align: center;">
Enter your name here:<br>
         <input type = "text" name = "myname"><br>

         <input type = "submit" value = "Write Cookie" 
            style = "background-color: #F0E86C; color: navy;
            font-weight: bold" /><p>
      </form>

EOT2;
}


?>

      <p>Click <a href = "<?php echo "$script" ?>">here</a>
         to refresh this page.</p>
      
      <!-- print superglobals -->
      <br>Here are the cookie and post hashes:<br><span style = "color: blue">$_COOKIE:</span> 
         <?php print "$_COOKIE[myName]"; ?><br>
      
      <span style = "color: blue">$_POST:</span> 
         <?php print implode("  ", $_POST); ?><br>
      <p align=center>
Play with the controls of this script and use the "refresh" link in-between to see what happens to 
variables and the output. Trace the code and make sure that you understand why the script behaves 
as observed and which part of the code makes it behave as it does. Note that when the cookie is 
set, it is set to expire after 3 minutes.
   </body>
</html>