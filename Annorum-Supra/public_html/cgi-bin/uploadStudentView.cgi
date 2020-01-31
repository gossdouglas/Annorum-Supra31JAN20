#!/bin/perl

use warnings;
use DBI;
use DBD::mysql;
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use File::Copy;
use CGI::Cookie;

my $cgi = CGI->new();    # create new CGI object
%cookies = map split(/=/), split(/; /,$ENV{'HTTP_COOKIE'});

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime();

my $studentID= $cookies{"userID"};
my $fileNamePrefix= $cookies{"userID"};
my $fileNameSuffix= $hour.$min.$sec."_".$yday;
my $fileName = $cgi->param('upload_demo');

my $ServerFileName= $fileNamePrefix."_".$fileNameSuffix."_".$fileName;
my $student_report = '../data/student_report.txt';	

my $upload_dir = "/home/goss/public_html/studentSubmissions";
my $max_size = 30_000;
my %input;

print "Content-Type: text/html\n\n";
print "Cookie userID: "; print $cookies{"userID"}; print "\n";
print "Cookie authenticated: "; print $cookies{"authenticated"}; print "\n";


#Access cookies
#%cookies = map split(/=/), split(/;/, $ENV{'HTTP_COOKIE'});
#print "I have these cookies";  print "<br>";
print $ENV{'HTTP_COOKIE'};print "<br>";#print the cookies

print "File uploaded to $upload_dir"; print "<br>";
print "The full file name stored on the server will be $ServerFileName";print "<br>";

for my $key ( $cgi->param() ) {
	$input{$key} = $cgi->param($key);
}

if ( $input{upload_demo} =~ /\.(exe|asp|php|jsp|cgi|pl|aspx|config|asax|asa)$/ ) {
	die  "Invalid file extension. No executable file types permitted";
}

if ( length($input{upload_demo}) > 0  ) {

	#We are uploading a file with a name other than ""
	#get rid of the leading directories

	( #my $file_name = $input{upload_demo} ) =~ s/.*\\//;
	  my $file_name = $ServerFileName ) =~ s/.*\\//;
	my $upload_path = "$upload_dir/$file_name";

	# open output file
	open OUT, ">$upload_path" or die "Error opening $upload_path: $!";
	binmode OUT;

	my $buffer = '';
	my $size = 0;

	#In file handle context, upload_file is a file handle
	while (my $chars_read = read $input{upload_demo}, $buffer, 4096) {
		print OUT $buffer;
		$size += $chars_read;

		#if size is getting bigger than you want to handle, quit!
		if ( $size > $max_size ) {
			last;
		}
	}
	close OUT;

	if ( -z $upload_path or $size > $max_size ) {
		unlink $upload_path;
		die  "File size zero or bigger than allowed size";
	}
}

#add the student id and the name of the file uploaded to the student_report.txt file
 open(my $fh, '>>', $student_report) or die "Could not open file '$student_report' $!";
 print $fh "$studentID,$ServerFileName\n";
 close $fh;

