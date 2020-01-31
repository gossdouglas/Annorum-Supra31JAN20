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


#Access cookies
%cookies = map split(/=/), split(/;/, $ENV{'HTTP_COOKIE'});
while (($key, $value) = each %cookies)	{ 
	if (($key =~ /authenticated/) && ($value eq "yes")) { 
		$authenticated="yes"; 
	}
	$cook .=" $key is $value <br>";  ## for debugging to check on the cookies
	}

#Grab inputs
# &ReadParse(*input, \%cgi_cfn,\%cgi_ct,\%cgi_sfn);
&Read_inputs;

 while (($key, $value) = each %input)	{ ##clean up input
        chomp($value);
		$value =~ s/\`//g; ## remove backtics from input fields
        $value =~ s/\"|\/|\'//g; ## remove quotes from input fields
        $value =~ s/\|//g;  ## another place to remove | from input fields
 }


### Open the database

#connect to database
$databaseUserID = "uuuuu";
$databasePassword = "pppppp";
$myConnection= DBI->connect("DBI:mysql:testme", "$databaseUserID", "$databasePassword") or
	die("Could not make a connection to database: $DBI::errstr");



########## START THE ACTIONS ##########

$action = $input{'action'};

if (($action eq "") && ($ENV{'QUERY_STRING'} =~ /^act_(\w+)(\W|\b)/)){ ## see if action has been sent via Query String
	$action=$1; 
	}

## $grab .= "Now: action $action <br>";

&check_cart_id;

if ($action ne ""){ 
	&$action; 
}
else{ #do this if user got to file without submitting form
	## If we got here then no action has been submitted so the script has been accessed 
	## via direct URL and no action in the Query String part of the URL
## SO WE ASSUME A GENERAL USER IS BROWSING
	&browseFiles;
## This is the old stuff; now the default is "browsing"
#	print "Content-type: text/html\n\n";
#	print "I do not know what you want me to do. <p><a href=\"$login_url\">Try loging in: $login_url </a>\n";
}
#==================================================================================
sub register{
	#Save some trouble by storing input values in variables
	$firstName = $input{'fname'};
	$lastName = $input{'lname'};
	$email = $input{'email'};
	$userID = $input{'userID'};
	$password = $input{'password'};

	if ($firstName =~ /\|/){ 
		&error("Enter a proper first name."); 
	}
	if ($lastName =~ /\|/){ 
		&error("Enter a proper last name."); 
	}
	$email =~ s/\|//g;
	$userID =~ s/\|//g;
	$password =~ s/\|//g;

	$password = crypt($input{'password'},'pw'); #encrypt the password

	$check = "yes"; #used to check if userID is unique

	$usersTable = "USERS"; #Table for users
	$query = $myConnection->prepare("SELECT * FROM $usersTable");
	$result = $query->execute();

	#Checks if userID is unique
	while(my @row = $query->fetchrow_array()){
		if($userID eq $row[3]){
			$check =  "no";
			last;
		}
	}
	$query->finish(); #finish with database

	if($check eq "no"){
		print "Content-type: text/html\n\n";
		print <<"EOF";
			<HTML>
				<HEAD>
					<TITLE>Error</TITLE>
				</HEAD>
				<BODY>
					<H1>User ID is taken please try another one.</H1>
					<a href="$login_url">Back to Registration.</a> 
				</BODY>
			</HTML>
EOF
	}
	else{ #if check = "yes"
		#Path to sendmail
		$mailprog = "/usr/sbin/sendmail -t";

		$user_email = $sender = "$email"; ##set email

		if($user_email =~ /^[\w|\d|\_|\-|\.]+\@selu\.edu$/){ #checks if email is from SELU and is valid
			open (MAIL, "|$mailprog $user_email") || die "Can't open $mailprog!\n";
			print MAIL "To: $user_email\n";
			print MAIL "From: $sender\n";
			print MAIL "Subject: Account Created\n\n";
			print MAIL "First Name: $input{'fname'}\n";
			print MAIL "Last Name: $input{'lname'}\n";
			print MAIL "Email: $input{'email'}\n";
			print MAIL "User ID: $input{'userID'}";
			close (MAIL);
			#close mail

			#Insert intp the database
			$myConnection->do("INSERT INTO $usersTable VALUES (\'$firstName\', \'$lastName\', \'$email\', \'$userID\', \'$password\')");
			
			print "Content-type: text/html\n\n";

			print <<"EOF";
						<HTML>
							<HEAD>
								<TITLE>Registered</TITLE>
							</HEAD>
							<BODY>
								<H1>Registration Complete.</H1>
								<a href="$login_url">Back to Login.</a> 
							</BODY>
						</HTML>
EOF
		}
		else{
			print "Content-type: text/html\n\n";
			print <<"EOF";
					<HTML>
						<HEAD>
							<TITLE>Error!</TITLE>
						</HEAD>
						<BODY>
							<H1>You must have a SELU email to register.</H1>
							<a href="$login_url">Back to Login.</a> 
						</BODY>
					</HTML>
EOF
		}
	}
}
#==================================================================================
sub login{
	#Put whatever the user entered in easier variables to work with
	$userID = $input{'userID'};
	$password = $input{'password'};

	my $check = "no"; #lets user know if login is correct. Always assumes no!

	$password = crypt($input{'password'},'pw'); #encrypt the password to match what's in DB

	#use in a minute
	$usersTable = "USERS";
	$query = $myConnection->prepare("SELECT * FROM $usersTable");
	$result = $query->execute();

	#Checks if userID is unique
	while(my @row = $query->fetchrow_array()){
		if(($userID eq $row[3]) && ($password eq $row[4])){
			#### this happens when the user id and the password match
	 		$check = "yes";
	 		
	 		print "Content-type: text/html\n";
	 		$time = time();
	 		$exptime = $time + 6000; #adds 1 min to current time to expire cookie

			$xptime = gmtime($exptime); #convert time to GMT for cookie
	 		print "Set-Cookie: authenticated=yes\; expires=$xptime\; \n"; ## Sets authentication cookie
	 		print "Set-Cookie: user_id=$userID\; expires=$xptime\; \n\n"; ## Sets user cookie

			# We do not really need two cookies above but we can use as many as we like
		
			print "Cookie has been set as: user_id=$userID\; expires=$xptime\; <br>\n";
			print "<a href=\"$scripturl\?act_repeatme\">Go Check</a> <br>or just wait and you will be redirected.\n";
			$t = 8; ## delay for redirect
			print "<META HTTP-EQUIV=refresh CONTENT=\"$t;URL=$scripturl\?act_repeatme\">\n"; ## redirect to url when cookie is assigned

		 	last; # break loop 
		}
	}
	#print "Content-type: text/html\n\n";
	#print "hello world";
	if($check eq "no"){
		print "Content-type: text/html\n\n";
	
		print <<"EOF";
				<HTML>
					<HEAD>
						<TITLE>Error</TITLE>
					</HEAD>
					<BODY>
						<H1>Incorrect Login.</H1>
						<a href="$login_url">Back to Login.</a>
					</BODY>
				</HTML>
EOF
	}
}
###################################################################################
sub check_authentication {
unless ($authenticated eq "yes"){
	unless (($action eq "login") || ($action eq "register")){
		#If user is not authenticated send to login
		print "Content-type: text/html\n";
#		print "Content-type: text/html\n\n grab: $grab cook $cook END"; exit;
		print "Location: $login_url\n\n";
		exit;
		}
	}
}
###################################################################################
sub check_cart_id {
if ($cart_id eq "") { $cart_id = $cookies{'cart_id'}; }
if ($cart_id eq "") { #### get new cartid
	$cart_id = "cart" . &newFileID;
	$cookies{'cart_id'} = $cart_id;
	print "Set-Cookie: cart_id=$cart_id\; \n"; ## Sets cart ID cookie, header must not be terminated yet
	}
}
###################################################################################
sub Read_inputs {
## This reads all inputs and makes the %input hash
## Replaces the old ReadParse method

$query =  new CGI;
my @allvars = $query->param();
foreach $inparam(@allvars) { 
	$inparam =~ s/\`//g; ## remove backtics from input fields
	$inparam =~ s/\"|\/|\'//g; ## remove quotes from input fields
	$input{$inparam}=$query->param($inparam);
  ##clean up input
       chomp($input{$inparam});
	$input{$inparam} =~ s/\`//g; ## remove backtics from input fields
       $input{$inparam} =~ s/\"|\/|\'//g; ## remove quotes from input fields
       $input{$inparam} =~ s/\|//g;  ## another place to remove | from input fields
 }
}
###################################################################################
sub uploadFile {
	&check_authentication;
	print "Content-type: text/html\n\n";

	#HTML file upload form
	#needs an image field will send email later

		print <<EOT
				<P>
					<center>
						<h4>File Upload Form</h4>
							<form action="$scripturl\?act_do_upload" method="post" enctype="multipart/form-data">
								<table>
									<input type=hidden name="action" value="do_upload">
									<tr>
									<input type=file name="fileToUpload">
									</tr>
									<tr>
										<td>Title</td><td><input type="text" name="title"></td>
									</tr>
									<tr>
										<td>Author</td><td><input type="text" name="author"></td>
									</tr>
									<tr>
										<td>Price</td><td><input type="text" name="price"></td>
									</tr>
									<tr>
										<td>Description</td><td><textarea name="description" rows="7" cols="50">Enter text here</textarea></td>
									</tr>
									<tr>
										<td><input type="submit" value="Submit"></td>
									</tr>
								</table>
							</form>
					</center>
EOT
}
##################################################################################
sub do_upload {
	print "Content-type: text/html\n\n";

	#Get the inputs in easier variables

	$title = $input{'title'};
	$author = $input{'author'};
	$price = $input{'price'};
	$description = $input{'description'};
	$prefix = "xxxx-"; #avoids overwriting existing files
	$folder = "uploaded_files"; #folder for the files'
	$fileTable = "FILES"; #table for database

	my $fileName = $query->param("fileToUpload");
	$CGI::POST_MAX = 1024 * 5000; #max size is 5MB
	my $safe_filename_characters = "a-zA-Z0-9_.-";

	if(!$fileName){
		print "There was a problem uploading your file.";
		exit;
	}

	my ($name, $path, $extension) = fileparse($fileName, '\.[^+.]*' );

	$fileName = $name . $extension;
	$fileName =~ s/^.*\\//g;
	$fileName =~ tr/ /_/;
	$fileName =~ s/[^$safe_filename_characters]//g;
	$fileName = "$prefix\_." . &newFileID . "\.$fileName";

	my $uploadFileHandle = $query->upload("fileToUpload");
	if (-e "$uploadFileHandle") { print " exists "; } else { print " does not exist "; }

	unless(-e "$working_dir\/$folder"){
		mkdir("$working_dir\/$folder", 0777);
	}
copy ($uploadFileHandle, "$working_dir\/$folder\/$fileName"); 
	chmod(0776, "$working_dir\/$folder\/$fileName");

	#####################################################
	#submit data into Database
	$query = $myConnection->prepare("SELECT * FROM $fileTable") or die "could execute prepare";
	$result = $query->execute();
	$query->finish(); #finish with database

	#Insert into the database
	print "$title , $author , $price ,  $description";
	$myConnection->do("INSERT INTO $fileTable VALUES (\'0\',\'$title\', \'$author\', \'$price\', \'$description\', \'$fileName\', \'$fileName\')") or die "could not execute" , $DBI::errstr;
	
	#Button to go back to repeat me
	print <<EOT;
			<P>
				<center>
					<h4>All Finished!</h4>
						<form action="$scripturl" method="post">
							<input type=hidden name="action" value="browseFiles">
							<input type=submit value="Browse">
						</form>
						<form action="$scripturl" method="post">
							<input type=hidden name="action" value="uploadFile">
							<input type=submit value="Upload Another File">
						</form>
			<p>
				</center>
EOT
}
##################################################################################
sub newFileID {
## Find a unique ID for a new file to be stored on the server.
## Here we use a simple method of a counter stored in a local file
## combined with the user's ID


open(FILE, "$working_dir\/FileCount")|| &error("Cannot access FileCount");
&lock(FILE);
my $count = <FILE>;
&unlock(FILE);
close(FILE);
if ($count eq "") { $count = 0; } else { $count++; }

# write back
open(FILE, ">$working_dir\/FileCount")|| &error("Cannot access FileCount");
&lock(FILE);
print FILE "$count\n";
&unlock(FILE);
close(FILE);
my $newID = $count . "_" . $cookies{'user_id'};
return $newID;
}
####################################################################################
sub browseFiles{
	print "Content-type: text/html\n\n";
	$testCounter = 0;
	#get query string inputs
	if (length ($ENV{'QUERY_STRING'}) > 0){
      	$buffer = $ENV{'QUERY_STRING'};
      	@pairs = split(/&/, $buffer);
      	foreach $pair (@pairs){
           ($name, $value) = split(/=/, $pair);
           $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
           $input{$name} = $value; 
      	}
 	}
	
 	$filesTable = "FILES";
	$pageNumber = int($input{'pageNumber'});
	$pageSize = 5;

		$dataStartingValue = $pageNumber * $pageSize;
		$dataEndingValue = $dataStartingValue + 5;

	##	$query = $myConnection->prepare("SELECT * FROM $filesTable LIMIT $pageSize, $dataStartingValue");
		$query = $myConnection->prepare("SELECT * FROM $filesTable");
		$result = $query->execute() or die "Could not execute statement: $DBI::errstr";
	
	$testCounter = 0;
	my $printedsomething = "false";
	while(@row = $query->fetchrow_array()){ 
		$testCounter +=1; 
		if ($testCounter >= $dataEndingValue +1) { last; }
		if ($testCounter < $dataStartingValue +1) { next; }

		print "Page $pageNumber  Item: $testCounter : ";

			$title = $row[1];
			$author = $row[2];
			$price = $row[3];
			$description = $row[4];
			$file_name = $row[5];
			$file_image = $row[6];

		$printedsomething = "true";

		print <<EOT;
			<br>-------------------<br>
			<table><tr><td>$file_image <br><img src="$working_url\/uploaded_files/$file_image" height=50></td>
			<td><ul>
				<li>Title: $title</li>
				<li>Author: $author</li>
				<li>Price: \$$price</li>
				<li>Description: $description</li>
			</ul></td></tr></table><hr width="60%">

EOT

	}  ## end While loop

	$query->finish();
	$myConnection->disconnect();

	if ($printedsomething eq "true") { 
		$pageNumber += 1;
		print "<center><a href=\"$scripturl\?action=browseFiles&pageNumber=$pageNumber\">Next<a></center>";
	} else { print "No more products"; }

print "<p align=right><a href=\"$scripturl\?act_uploadFile\">Upload something of your own</a></p>";

}
#==================================================================================
 sub error 	{
	print "Content-type: text/html\n\n";
	print <<EOT;
			<P>
				<center>
					<h4>Sorry!</h4>
					@_
				</center>
EOT
	exit;
}
############################################################
sub lock	{
	flock (@_, 2);
	seek (@_, 0, 2);
}
############################################################
sub unlock	{
	flock(@_, 8);
}
############################################################
sub repeatme {
	print "Content-type: text/html\n\n";
	print <<EOT;
			<P>
				<center>
					<h4>What do you want to do?</h4>
						<form action="$scripturl" method="post">
							<input type=hidden name="action" value="repeatme">
							<input type=submit value="Call the cgi script again">
						</form>
						<form action="$scripturl" method="post">
							<input type=hidden name="action" value="uploadFile">
							<input type=submit value="Upload a File">
						</form>
						<form action="$scripturl" method="post">
							<input type=hidden name="action" value="browseFiles">
							<input type=submit value="Browse Files">
						</form>
						<center><a href='$scripturl\?act_browseFiles&pageNumber=1'>Browse Files<a></center>
			<p>
			<a href="$scripturl\?act_repeatme">Call the cgi script again<a>
				</center>
cookies: $cook
EOT
	exit;
}
############################################################

