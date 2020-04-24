grep "\d" apollo13.txt | wc -l > apollo_out.txt
man grep |col -b | grep -E 'c, --|Only a count' | tr '\n' ' '