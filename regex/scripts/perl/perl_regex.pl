#!usr/bin/perl

use strict;
use warnings;

my $t = time;
open(my $f, "../../files/results.csv") or die("No hay archivo");

my $match = 0;
my $nomatch = 0;

while(<$f>){
    chomp;
    if(m/(^\d{4,4}).*?,(.*?),(.*?),(\d+),(\d),/){ # // → to use regex, [] → escapa a \d
        if($5>$4){
            printf("%s|%s (%d) - (%d) %s \n",$1, $2, $4, $5, $3)
        }
        # print $_."\n";
        $match++;
    }else{
        $nomatch++
    }
}

close($f);

printf("\nSe encontraton %d matches - %d no matches\n", $match, $nomatch);
printf("Tardo %d seg.\n", time()-$t)
