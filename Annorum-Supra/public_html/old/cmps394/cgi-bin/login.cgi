##!"C:\xampp\perl\bin\perl.exe"
#!/bin/perl
use strict;
use warnings;
use CGI::Carp;    # send errors to the browser, not to the logfile
use CGI;

my $cgi = CGI->new();    # create new CGI object

my $userID = $cgi->param('userID');
my $password = $cgi->param('password');

 my $usernames_passwords = 'C:\xampp\htdocs\cmps394\data\usernames_passwords.txt';

#print $cgi->header('text/html');

if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}

print "Content-Type: text/html\n\n";
print "User ID is, $userID <br>";
print "password is, $password <br><br>";


#add new user name and password to the text file
# open(my $fh, '>>', $usernames_passwords) or die "Could not open file '$usernames_passwords' $!";
# print $fh "$userID,$password\n";
# close $fh;

#read user name and password from the text file
open(FH, '<', $usernames_passwords) or die $!;
my $index=0;
while(<FH>){ #read the file until the end
   
my @userData=split(',', $_); #place the current line into an array split by a comma
my $lineUserName=@userData[0];
my $lineUserPassword=@userData[1];

   print "$_ is in index $index <br>"; 
   print "The entered user id is "; print $userID; print "<br>";
   print "The user name is "; print @userData[0]; print "<br>";
   print "The password is "; print @userData[1]; print "<br>"; 

   #if ($userID == @userData[0]){
   if ($userID == $lineUserName){    
   #if ($userID == "yo"){
        print "submitted user id $userID and userData[0] $lineUserName match.<br><br>";
   }
   if ($userID != $lineUserName){
    #if (5 != 5+5){
       print "not this user.<br><br>";
   }
   $index++;
}

close(FH);
print "done\n";
