<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
   <body style = "font-family: arial,sans-serif">

      <p>Hi again...<p>


<?php $myFile = "./testfile.txt";
if (file_exists($myFile)) { print "$myFile does exist <p>\n "; } else { print "$myFile does NOT exist <p>\n "; } 

$lines = file($myFile); // Read the contents of myFile as an array. Creates array "$lines"
print "ok GOTIT <br>";

foreach ($lines as $line_num => $line) {
    echo "Line #<b>{$line_num}</b> : $line <br>\n";
}

// So far we have just listed the contents of testfile.txt
// Now we will augment it by changing any string that starts with H 
// by replacing H and its following character with "Th"
// Why? Just for the heck of it :)

$fh = fopen($myFile, 'a') or die("can't open $myFile <br>");
foreach ($lines as $line_num => $line) {
    $xx = preg_replace("/^H./", "The", $line);
    fwrite($fh, "$xx \n");
    print "wrote $xx FROM $line <br>";
}
fclose($fh);

die("DONE");
 ?>

Ok, I am all done (but this will not be printed because it should die above.

   </body>
</html>

