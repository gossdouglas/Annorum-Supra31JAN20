#!/usr/bin/perl
#######################################################
# Example						  
# by Cris Koutsougeras
####################################################### 

$envdocroot = "$ENV{'DOCUMENT_ROOT'}";
$server = 'http://shaggy.netsal.selu.edu/~ckoutsougeras';

# the next line is the PATH to the base directory which holds the working files
$dir = "/home/ckoutsougeras/public_html";

############################################################

if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}

## use the library routine for parsing the input
&ReadParse(*input, \%cgi_cfn,\%cgi_ct,\%cgi_sfn);

### START MAIN PROGRAM #####

print &PrintHeader;

if ($input{'what_to_do'} eq "insert") { &insert; }

if ($input{'what_to_do'} eq "delete") { &delete; }

if ($input{'what_to_do'} eq "demo") { &demo; }

&mkcopy;

print "\&nbsp\;<center>Results in:<P><a href=\"$server/my_db.htm\" target=new>my_db.htm</a><P>I am done";
exit;

##############################################################
##############################################################
sub demo {
open (FILE, "$dir/my_db");
@dblines= <FILE>;
close(FILE);

open (FILE, "$dir/my_demo.html");
@lines= <FILE>;
close(FILE);

foreach (@lines) { $temp = $_;

$_ =~ s/\bTiger\b/$input{'fname'}/g;
$_ =~ s/\bWoods\b/$input{'lname'}/g;
$_ =~ s/\bTiger\b/$input{'Other'}/g;

if ($_ =~ /%%first_name%%/) {
foreach $indb(@dblines) { $_ = $temp;
@parts = split(/\|/, "$indb");

	$_ =~ s/%%first_name%%/$parts[0]/g; 
	$_ =~ s/%%last_name%%/$parts[1]/g; 
	$_ =~ s/%%other%%/$parts[2]/g; 
print "$_ \n";
	}
} else { print "$_ "; }
}
}
##############################################################
sub insert {

if ($input{'fname'} =~ /\|/) { &error("what $input{'fname'}\?  trying my nerves huh\?"); }
if ($input{'lname'} =~ /\|/) { &error("what $input{'lname'}\?  trying my nerves huh\?"); }
$input{'lname'} =~ s/\|//g;
$input{'fname'} =~ s/\|//g;
$input{'Other'} =~ s/\n|\|//sg;

open (FILE, ">>$dir/my_db");

print FILE "$input{'fname'}\|$input{'lname'}\|$input{'Other'}\|\n";

close(FILE);
}
##############################################################
sub delete {
open (FILE, "$dir/my_db");

@dblines= <FILE>;

close(FILE);

open (FILE, ">$dir/my_db");

foreach (@dblines) {
	@parts = split(/\|/, $_);
	unless ($parts[1] =~ /$input{'lname'}/i) { print FILE "$_"; }
#	unless ($parts[1] =~ /^$input{'lname'}$/i) { print FILE "$_"; }
	}

close(FILE);
}
##############################################################
sub error 	{
print <<EOT;
<html>
<head><title>Error!</title>

</head>
<body bgcolor="ffffff">
<center>
Account Administration
<P>
 
<h4>Warning!</h4>
@_
<P>
<br>Thank you!
</center>

EOT
exit;
}
##############################################################
sub mkcopy	{
open (FILE, "$dir/my_db");

@dblines= <FILE>;

close(FILE);

open (FILE, ">$dir/my_db.htm");

foreach (@dblines) { print FILE "$_<br>\n"; }

close(FILE);
}
##############################################################
