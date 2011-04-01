#!/usr/bin/perl

########################
# history of updates
# 2011/3/13 23:43 V1.001 indexpc.html$B$NI=<(M^@)BP1~(B (tnx:nanakochi123456)
# 2011/3/13 23:17 initial release(mnakajim tnx:nanakochi123456)


use File::Basename qw/dirname/;
BEGIN { require (dirname(__FILE__) . "/fatlib.pl") }
use PlannedBlackoutJP::Util qw/is_galapagos/;

$location='indexpc.html';

if(is_galapagos \%ENV) {
	$location='indexm.html';
}

print "Content-type: text/html;charset=utf-8\n\n";

open (READ,$location);

while (<READ>) {
	s/<meta http-equiv="refresh" content=".*$//;
	print;
}
