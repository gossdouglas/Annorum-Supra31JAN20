#!/bin/perl
use strict;
use warnings;
use CGI::Carp;    # send errors to the browser, not to the logfile
use CGI;

my $cgi = CGI->new();    # create new CGI object
my $userID = $cgi->param('userID');
my $password = $cgi->param('password');

print "Content-Type: text/html\n\n";

print "hello world.";

#my $usernames_passwords = 'C:\xampp\htdocs\cmps394\data\usernames_passwords.txt';
my $usernames_passwords = '../data/usernames_passwords.txt';
#my $usernames_passwords = 'usernames_passwords.txt';

if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}



#read user name and password from the text file
open(FH, '<', $usernames_passwords) or die $!;
my $index=0;
while(<FH>){ #read the file until the end
   
my @userData=split(',', $_); #place the current line into an array split by a comma
my $lineUserName=@userData[0];
my $lineUserPassword=@userData[1];

   if ($userID eq @userData[0]){    		 
        print "@userData[0] logged in with a password of @userData[1] at index $index of the database.<br><br>";
   }
   $index++;
}

close(FH);
