#!/bin/perl

use warnings;
use DBI;
use DBD::mysql;
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use File::Copy;

if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}

#define some general use variables
$user_dir = "goss";
$assgn_dir = "cmps394";
$working_dir = "/home/$user_dir/public_html/$assgn_dir";
$working_url = "http://ck.csit.selu.edu/\~$user_dir/$assgn_dir";
$entry_page ="login_view.html";
$std_page = "login_viewLoggedin.html";
$login_url = "http://ck.csit.selu.edu/\~$user_dir/$assgn_dir/$entry_page";
$loggedin = "http://ck.csit.selu.edu/\~$user_dir/$assgn_dir/$std_page";
$scripturl = "http://ck.csit.selu.edu$ENV{'SCRIPT_NAME'}";


print "yo";
