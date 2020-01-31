#!/bin/perl
use strict;
use warnings;
use CGI::Carp;    # send errors to the browser, not to the logfile
use CGI;

print "Content-Type: text/html\n\n";
print "Im here ";

my $cgi = CGI->new();    # create new CGI object
my %input;

my $upload_dir = "/home/goss/public_html/data";
my $max_size = 30_000;


print "yo <p>\n\n";
print $upload_dir;

## You are not using the cgi-lib so you don't need this block
if (-e "./cgi-lib.pl")	{
	require "./cgi-lib.pl";	
}
else	{
	print "Content-type: text/html\n\n";
	print "Sorry, I cannot find a needed library\n";
	exit;
}

for my $key ( $cgi->param() ) {
	$input{$key} = $cgi->param($key);
}

if ( $input{upload_demo} =~ /\.(exe|asp|php|jsp|cgi|pl|aspx|config|asax|asa)$/ ) {
	die  "Invalid file extension. No executable file types permitted";
}

if ( length($input{upload_demo}) > 0  ) {

	#We are uploading a file with a name other than ""
	#get rid of the leading directories

	( my $file_name = $input{upload_demo} ) =~ s/.*\\//;
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

