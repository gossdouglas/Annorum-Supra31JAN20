#!/bin/perl
use strict;
use warnings;
use CGI::Carp;    # send errors to the browser, not to the logfile
use CGI;

print "Content-Type: text/html\n\n";
#print "Im here ";

my $cgi = CGI->new();    # create new CGI object
my $userID = $cgi->param('userID');
my $password = $cgi->param('password');

#print "I got userID $userID and password $password <p>\n\n";

#my $usernames_passwords = 'C:\xampp\htdocs\cmps394\data\usernames_passwords.txt';
my $usernames_passwords = '../data/usernames_passwords.txt';
#my $usernames_passwords = 'usernames_passwords.txt';

## You are not using the cgi-lib so you don't need this block
if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}



#read user name and password from the text file
open(FH, $usernames_passwords) or die('Cannot open FH');
my $index=0;
while(<FH>){ #read the file until the end
chomp($_);   
my @userData=split(',', $_); #place the current line into an array split by a comma
my $lineUserName= $userData[0];
my $lineUserPassword= $userData[1];

#print "checking against lineUserName $lineUserName and lineUserPassword $lineUserPassword <p>\n";

   if ($userID eq $userData[0]){    		 
        #print "$userData[0] trying to log in with a password: $password to match: $userData[1] at index $index of the database.<br><br>";
	if ($password eq $userData[1]){
		#print "$password is equal to $userData[1]";
                #print "User $userData[0] is authenticated here. Do what you need to do for setting a cookie";
				print "User $userData[0] has been authenticated.";
							
                last; ### no need to continue the loop
					}else {
		#print "$password is not equal to $userData[1]";}
		print "User $userData[0] has not been authenticated.  Check user name and password.";}

   }
   $index++;
}

close(FH);
