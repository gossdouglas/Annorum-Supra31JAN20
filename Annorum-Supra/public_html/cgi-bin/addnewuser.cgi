#!/bin/perl
##!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI::Carp;    # send errors to the browser, not to the logfile
use CGI;

my $cgi = CGI->new();    # create new CGI object
my $userID = $cgi->param('userID');
my $password = $cgi->param('password');
my $role = $cgi->param('role');

#my $usernames_passwords = 'C:\xampp\htdocs\cmps394\data\usernames_passwords.txt';
my $usernames_passwords = '../data/usernames_passwords.txt';
#my $usernames_passwords = 'usernames_passwords.txt';


print "Content-Type: text/html\n\n";

#print "hello world.";

if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}

print "User ID is, $userID <br>";
print "password is, $password <br><br>";
print "role is $role <br><br>";

#add new user name and password to the text file
 open(my $fh, '>>', $usernames_passwords) or die "Could not open file '$usernames_passwords' $!";
 print $fh "$userID,$password,$role\n";
 close $fh;

print "done\n";




