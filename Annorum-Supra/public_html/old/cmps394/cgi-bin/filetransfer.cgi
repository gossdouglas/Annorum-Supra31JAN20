#!/bin/perl

### Uploads a file (document) to the server
### It uses CGI to process inputs; so the previous method for handling inputs (Readparse from cgi-lib) cannot be used
### The uploaded file MUST be provided through a form field: file=file2upload and enctype=multipart/form-data

## Use the CGI package to upload files to the server.
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
use File::Basename;

my $query = new CGI;    ##### this is the actual call

######## collect inputs as needed #######
$skip = $query->param("got_file"); 

### This is another package so that we can use the file copy function
use File::Copy;

print "Content-Type: text/html\n\n";

## 
print "Disabled for security"; exit; ##comment out this line for it to work

$script = "$ENV{'SCRIPT_NAME'}";

unless ($skip eq 1) {
print "<center><form action=\"$script\" method=\"post\" enctype=\"multipart/form-data\">";
print "<input type=\"file\" name=\"file2upload\"><p>";
print "<input type=\"hidden\" name=\"got_file\" value=\"1\">";
print "<input type=\"submit\" name=submit> </form>";
exit;
} else { &process_file }
exit;
############################################################
sub process_file	{
## Manage the upload >>>

$prefix = "xxxx";  ## to avoid overwriting existing files we will use a prefix for uploaded files
$datapath = "/home/ck/public_html";  ## This is the base directory where all uploads will be placed
$folder = "uploaded_files";  ## this is the folder where uploads will be placed within the $datapath


my $filename = $query->param("file2upload"); ######## collect inputs as needed #######
$CGI::POST_MAX = 1024 * 5000; ### sets 5 MB maximum size
my $safe_filename_characters = "a-zA-Z0-9_.-";

if ( !$filename ) { 
print "There was a problem uploading your file. Perhaps you have exceeded 5MB. ";
exit;
}

my ( $name, $path, $extension ) = fileparse ( $filename, '\..*' );
$filename = $name . $extension;
$filename =~ s/^.*\\//g;
$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;
$filename = "$prefix\_$filename";


my $upload_filehandle = $query->upload("file2upload"); ######## collect inputs as needed #######

unless (-e "$datapath\/$folder")	{ mkdir ("$datapath\/$folder", 0777); }

#### Now we will copy the file in its destination by either of two methods


### Method 1: the short one using the File::Copy included earlier
copy ($upload_filehandle, "$datapath\/$folder\/$filename"); 


### Method 2: the long one but without using any packages (no "copy" function)
# open ( UPLOADFILE, ">$datapath\/$folder\/$filename" ) or die "$!";
# binmode UPLOADFILE;
# while ( <$upload_filehandle> ) { print UPLOADFILE "$_"; }
# close UPLOADFILE;


chmod(0775, "$datapath\/$folder\/$filename");

print "<p><center>$datapath\/$folder\/$filename<p>";

print "<p><center>DONE";
exit;
}
##############################################################


