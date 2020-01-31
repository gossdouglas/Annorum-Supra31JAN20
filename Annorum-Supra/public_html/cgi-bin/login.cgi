#!/bin/perl
# use strict;
# use warnings;
# #use CGI::Carp;    # send errors to the browser, not to the logfile
# use CGI;
# use CGI::Cookie;
# use CGI::Carp qw (fatalsToBrowser);

use warnings;
use DBI;
use DBD::mysql;
use CGI;
use CGI::Carp qw (fatalsToBrowser);#important for time?
use File::Basename;
use File::Copy;
use CGI::Cookie;

my $cgi = CGI->new();    # create new CGI object
my $userID = $cgi->param('userID');
my $password = $cgi->param('password');

#my $usernames_passwords = 'C:\xampp\htdocs\cmps394\data\usernames_passwords.txt';
my $usernames_passwords = '../data/usernames_passwords.txt';
#my $usernames_passwords = 'usernames_passwords.txt';

%cookies = map split(/=/), split(/; /,$ENV{'HTTP_COOKIE'});

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
my $lineUserRole= $userData[2];

   if ($userID eq $userData[0]){ #the user exists...   		 
        
	if ($password eq $userData[1]){#and the password for that user matches the password stored in the database...
		       								
				my $userIDCookie = CGI::Cookie->new(-name    =>  'userID',#let's set cookies for userID
                         -value   =>  [$userData[0]],
                         -expires =>  '+12h');#cookie expires after 2 minutes
				my $authenticatedCookie = CGI::Cookie->new(-name    =>  'authenticated',#let's set cookies for userID
                         -value   =>  ['yes'],
                         -expires =>  '+12h');#cookie expires after 2 minutes
				my $superUserCookie = CGI::Cookie->new(-name    =>  'role',#let's set cookies for role
                         -value   =>  [$userData[2]],
                         -expires =>  '+12h');#cookie expires after 2 minutes
								
				print "Set-Cookie: $userIDCookie\n";
				print "Set-Cookie: $authenticatedCookie\n";
				print "Set-Cookie: $superUserCookie\n\n";#complete the header with \n\n

				%cookies = map split(/=/), split(/; /,$ENV{'HTTP_COOKIE'});
				print %cookies; print "\n";
				print "Cookie userID: "; print $cookies{"userID"}; print "\n";
				print "Cookie authenticated: "; print $cookies{"authenticated"}; print "\n";
			
				($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime();						

				print "User $userData[0] has been authenticated as a $lineUserRole .\n";				
				$suffix= $hour.$min.$sec."_".$yday;
				open( my $fh, '<', $usernames_passwords ) or die "Can't open $usernames_passwords: $!";
							
                last; ### no need to continue the loop
		}else {

		print "Check user name and password.";
		

		
		}

   }
   $index++;
}

close(FH);


