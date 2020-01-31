<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
   <body style = "font-family: arial,sans-serif">

      <p>Hi there...<p>


<?php $myFile = "./testfile.txt";
if (file_exists($myFile)) { print "$myFile does exist <p>\n "; } else { print "$myFile does NOT exist <p>\n "; } 

$fh = fopen($myFile, 'a') or die("can't open $myFile <br>");
$stringData = "Here is some data\n";
fwrite($fh, $stringData);        // write the above string into the file
fwrite($fh, "and here is some more \n--------\n");     // write some more stuff into the file
fclose($fh);
 ?>

Ok, I am all done.<br>Is this cool or what?

   </body>
</html>

