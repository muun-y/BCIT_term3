python driver.py abcd1234 -s "Test Data to be encrypted"

python driver.py abcd1234 -f "inputFile.txt"

python driver.py -f "inputFile.txt" abcd1234

python driver.py abcd1234 --file "inputFile.txt"

python driver.py abcd1234 -f "inputFile.txt" -m en

python driver.py abcd1234 -f "inputFile.txt" -m de

python driver.py abcd1234 -f "inputFile.txt" -m de --output print

python driver.py abcd1234 -s "b\x85\xc8\xd2\xbd\xab\x14\x97\xae" -m de --output "outputFile.txt"