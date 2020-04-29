read -p 'Enter your file name: ' file_name
echo "The name of the file is $file_name"
git add $file_name

echo "Now showing the results of git status"
git status
read -p 'Do you wish to continue? (Y or N) ' continue

if [ "$continue" = "N" ]; then
	echo "I will NOT continue. Will exit now"
	exit 1

fi

echo "I made it this far. Moving on"
read -p "Enter your commit message: " commit_message
git commit -m $commit_message

echo "Now showing the results of git status"
git status

read -p 'Do you wish to continue? (Y or N) ' continue2
if [ "$continue2" = "N" ]; then
	echo "I will NOT continue. Will exit now"
	exit 1
fi

git push